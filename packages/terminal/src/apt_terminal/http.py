from __future__ import annotations

from typing import Any

import httpx

from apt_terminal.errors import ApiError, AuthError, NotFoundError


class HttpClient:
    """Thin wrapper around httpx.Client with bearer auth + JSON helpers."""

    def __init__(self, base_url: str, *, key: str | None = None, timeout: float = 30.0) -> None:
        headers: dict[str, str] = {"Accept": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers=headers,
            timeout=timeout,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> HttpClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Any | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        try:
            r = self._client.request(method, path, json=json, params=params)
        except httpx.HTTPError as exc:
            raise ApiError(0, str(exc)) from exc

        if r.status_code == 204:
            return None
        if r.status_code == 401 or r.status_code == 403:
            raise AuthError(_extract_message(r) or f"unauthorized ({r.status_code})")
        if r.status_code == 404:
            raise NotFoundError(_extract_message(r) or "not found")
        if r.status_code >= 400:
            raise ApiError(r.status_code, _extract_message(r) or r.text, _safe_json(r))
        return _safe_json(r)

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, *, json: Any | None = None) -> Any:
        return self.request("POST", path, json=json)

    def put(self, path: str, *, json: Any | None = None) -> Any:
        return self.request("PUT", path, json=json)

    def patch(self, path: str, *, json: Any | None = None) -> Any:
        return self.request("PATCH", path, json=json)

    def delete(self, path: str) -> Any:
        return self.request("DELETE", path)


def _safe_json(r: httpx.Response) -> Any:
    try:
        return r.json()
    except ValueError:
        return None


def _extract_message(r: httpx.Response) -> str | None:
    body = _safe_json(r)
    if isinstance(body, dict):
        for key in ("error", "message", "detail"):
            v = body.get(key)
            if isinstance(v, str):
                return v
    return None
