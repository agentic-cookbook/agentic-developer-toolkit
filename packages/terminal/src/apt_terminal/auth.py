from __future__ import annotations

import httpx

from apt_terminal import config as config_mod
from apt_terminal.config import Config, Profile
from apt_terminal.errors import AuthError
from apt_terminal.generated import AuthenticatedClient, Client


def extract_refresh_cookie(headers: httpx.Headers) -> str | None:
    """Pull refresh_token out of a Set-Cookie header (httpx exposes it raw)."""
    for value in headers.get_list("set-cookie"):
        first = value.split(";", 1)[0].strip()
        if first.startswith("refresh_token="):
            return first[len("refresh_token="):]
    return None


class Session:
    """Owns the auth lifecycle and builds generated clients for the engine."""

    def __init__(self, profile: Profile, config: Config) -> None:
        self.profile = profile
        self.config = config

    def login(self, email: str, password: str) -> str:
        resp = httpx.post(
            f"{self.profile.base_url}/auth/login",
            json={"email": email, "password": password, "rememberMe": False},
        )
        if resp.status_code != 200:
            raise AuthError(_message(resp, "login failed"))
        data = resp.json()
        access = data.get("accessToken")
        refresh = extract_refresh_cookie(resp.headers)
        if not access or not refresh:
            raise AuthError("login succeeded but tokens were missing from the response")
        self.profile.access_token = access
        self.profile.refresh_token = refresh
        config_mod.save(self.config)
        return str(data.get("user", {}).get("email", email))

    def refresh(self) -> bool:
        if not self.profile.refresh_token:
            return False
        resp = httpx.post(
            f"{self.profile.base_url}/auth/refresh",
            headers={
                "Authorization": f"Bearer {self.profile.access_token or ''}",
                "Cookie": f"refresh_token={self.profile.refresh_token}",
            },
        )
        if resp.status_code != 200:
            return False
        access = resp.json().get("accessToken")
        new_refresh = extract_refresh_cookie(resp.headers) or self.profile.refresh_token
        if not access:
            return False
        self.profile.access_token = access
        self.profile.refresh_token = new_refresh
        config_mod.save(self.config)
        return True

    def logout(self) -> None:
        if self.profile.refresh_token:
            try:
                httpx.post(
                    f"{self.profile.base_url}/auth/revoke",
                    headers={
                        "Cookie": f"refresh_token={self.profile.refresh_token}",
                        "Content-Type": "application/json",
                    },
                    content="{}",
                )
            except httpx.HTTPError:
                pass
        self.profile.access_token = None
        self.profile.refresh_token = None
        config_mod.save(self.config)

    def whoami(self) -> dict:
        client = self.client_factory()
        resp = client.get_httpx_client().get("/auth/me")
        if resp.status_code != 200:
            raise AuthError("not logged in or session expired")
        return resp.json()

    def client_factory(self) -> AuthenticatedClient:
        if not self.profile.access_token:
            raise AuthError("not logged in — run 'apt auth login'")
        return AuthenticatedClient(
            base_url=self.profile.base_url, token=self.profile.access_token
        )

    def public_client(self) -> Client:
        return Client(base_url=self.profile.base_url)


def _message(resp: httpx.Response, fallback: str) -> str:
    try:
        body = resp.json()
    except ValueError:
        return fallback
    if isinstance(body, dict):
        if isinstance(body.get("error"), dict):
            return str(body["error"].get("message") or fallback)
        return str(body.get("title") or body.get("message") or fallback)
    return fallback
