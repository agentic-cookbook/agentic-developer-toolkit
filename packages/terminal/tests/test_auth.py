from __future__ import annotations

import httpx
import pytest
import respx

from apt_terminal import config as c
from apt_terminal.auth import Session, extract_refresh_cookie
from apt_terminal.errors import AuthError

BASE = "https://api.test"


def _session(tmp_path) -> Session:
    cfg = c.Config(path=tmp_path / "config.toml")
    p = cfg.profile()
    p.base_url = BASE
    return Session(profile=p, config=cfg)


def test_extract_refresh_cookie_from_set_cookie():
    h = httpx.Headers({"set-cookie": "refresh_token=abc123; HttpOnly; Path=/"})
    assert extract_refresh_cookie(h) == "abc123"


@respx.mock
def test_login_stores_tokens_and_saves(tmp_path):
    s = _session(tmp_path)
    respx.post(f"{BASE}/auth/login").mock(
        return_value=httpx.Response(
            200,
            json={"accessToken": "acc1", "user": {"email": "u@x.test"}},
            headers={"set-cookie": "refresh_token=ref1; HttpOnly"},
        )
    )
    email = s.login("u@x.test", "pw")
    assert email == "u@x.test"
    assert s.profile.access_token == "acc1"
    assert s.profile.refresh_token == "ref1"
    # persisted to disk
    assert c.load(s.config.path).profile().access_token == "acc1"


@respx.mock
def test_login_failure_raises(tmp_path):
    s = _session(tmp_path)
    respx.post(f"{BASE}/auth/login").mock(
        return_value=httpx.Response(401, json={"title": "bad creds"})
    )
    with pytest.raises(AuthError):
        s.login("u@x.test", "wrong")


@respx.mock
def test_refresh_updates_access_token(tmp_path):
    s = _session(tmp_path)
    s.profile.access_token = "old"
    s.profile.refresh_token = "ref1"
    respx.post(f"{BASE}/auth/refresh").mock(
        return_value=httpx.Response(
            200,
            json={"accessToken": "acc2"},
            headers={"set-cookie": "refresh_token=ref2; HttpOnly"},
        )
    )
    assert s.refresh() is True
    assert s.profile.access_token == "acc2"
    assert s.profile.refresh_token == "ref2"


def test_refresh_without_token_returns_false(tmp_path):
    s = _session(tmp_path)
    assert s.refresh() is False


def test_client_factory_requires_token(tmp_path):
    s = _session(tmp_path)
    with pytest.raises(AuthError):
        s.client_factory()


def test_client_factory_builds_authed(tmp_path):
    s = _session(tmp_path)
    s.profile.access_token = "acc"
    client = s.client_factory()
    assert client.token == "acc"
    assert client._base_url == BASE
