from __future__ import annotations

import contextlib
import os
from typing import Any

import httpx

from apt_terminal import config as config_mod
from apt_terminal import errors
from apt_terminal.config import Config, Profile
from apt_terminal.errors import AuthError
from apt_terminal.generated import AuthenticatedClient, Client


def extract_refresh_cookie(headers: httpx.Headers) -> str | None:
    """Pull refresh_token out of a Set-Cookie header (httpx exposes it raw)."""
    for value in headers.get_list("set-cookie"):
        first = value.split(";", 1)[0].strip()
        if first.startswith("refresh_token="):
            return first[len("refresh_token="):].strip('"')
    return None


class Session:
    """Owns the auth lifecycle and builds generated clients for the engine."""

    def __init__(self, profile: Profile, config: Config) -> None:
        self.profile = profile
        self.config = config

    @property
    def base_url(self) -> str:
        return os.environ.get("APT_BASE_URL") or self.profile.base_url

    def login(self, email: str, password: str) -> str:
        resp = httpx.post(
            f"{self.base_url}/auth/login",
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
            f"{self.base_url}/auth/refresh",
            headers={
                "Authorization": f"Bearer {self.profile.access_token or ''}",
                "Cookie": f"refresh_token={self.profile.refresh_token}",
            },
        )
        if resp.status_code != 200:
            return False
        access = resp.json().get("accessToken")
        # Defensive: use the new cookie if the server rotated it; fall back to
        # the stored token for servers that don't rotate on every call.
        new_refresh = extract_refresh_cookie(resp.headers) or self.profile.refresh_token
        if not access:
            return False
        self.profile.access_token = access
        self.profile.refresh_token = new_refresh
        config_mod.save(self.config)
        return True

    def logout(self) -> None:
        if self.profile.refresh_token:
            with contextlib.suppress(httpx.HTTPError):
                httpx.post(
                    f"{self.base_url}/auth/revoke",
                    headers={
                        "Cookie": f"refresh_token={self.profile.refresh_token}",
                        "Content-Type": "application/json",
                    },
                    content="{}",
                )
        self.profile.access_token = None
        self.profile.refresh_token = None
        config_mod.save(self.config)

    def whoami(self) -> dict[str, Any]:
        client = self.client_factory()
        resp = client.get_httpx_client().get("/auth/me")
        if resp.status_code == 401 and self.refresh():
            resp = self.client_factory().get_httpx_client().get("/auth/me")
        if resp.status_code != 200:
            raise AuthError("not logged in or session expired")
        result: dict[str, Any] = resp.json()
        return result

    def client_factory(self) -> AuthenticatedClient:
        token = os.environ.get("APT_TOKEN") or self.profile.access_token
        if not token:
            raise AuthError("not logged in — run 'apt auth login'")
        return AuthenticatedClient(base_url=self.base_url, token=token)

    def public_client(self) -> Client:
        return Client(base_url=self.base_url)


def _message(resp: httpx.Response, fallback: str) -> str:
    try:
        body = resp.json()
    except ValueError:
        return fallback
    return errors._message_from_body(body, fallback)
