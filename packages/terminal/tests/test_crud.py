from __future__ import annotations

import httpx
import pytest
import respx
import typer
from typer.testing import CliRunner

from apt_terminal import config as c
from apt_terminal import crud
from apt_terminal import resources as r
from apt_terminal.auth import Session
from apt_terminal.errors import AptError

BASE = "https://api.test"
runner = CliRunner()


def _session(tmp_path) -> Session:
    cfg = c.Config(path=tmp_path / "config.toml")
    p = cfg.profile()
    p.base_url = BASE
    p.access_token = "acc"
    return Session(profile=p, config=cfg)


def test_parse_set_coerces_json():
    assert crud.parse_set(["name=foo", "n=5", "flag=true"]) == {
        "name": "foo", "n": 5, "flag": True,
    }


def test_build_body_rejects_unknown_field():
    from apt_terminal.generated.models.post_persona_services_body import (
        PostPersonaServicesBody,
    )
    with pytest.raises(AptError):
        crud.build_body(PostPersonaServicesBody, ["bogus=1"])


def test_build_body_builds_model():
    from apt_terminal.generated.models.post_persona_services_body import (
        PostPersonaServicesBody,
    )
    body = crud.build_body(
        PostPersonaServicesBody,
        ["name=svc", "provider_kind=openai", "base_url=https://o.test"],
    )
    assert body.name == "svc"
    assert body.to_dict()["providerKind"] == "openai"


@respx.mock
def test_list_renders_json(tmp_path):
    services = next(res for res in r.PERSONA if res.name == "services")
    app = crud.build_resource_app(services, lambda: _session(tmp_path))
    respx.get(f"{BASE}/persona/services").mock(
        return_value=httpx.Response(200, json=[
            {"id": "1", "name": "svc", "providerKind": "openai",
             "baseUrl": "https://o.test", "status": "ok"},
        ])
    )
    res = runner.invoke(app, ["list", "--json"])
    assert res.exit_code == 0, res.output
    assert '"id": "1"' in res.output


@respx.mock
def test_create_posts_body(tmp_path):
    services = next(res for res in r.PERSONA if res.name == "services")
    app = crud.build_resource_app(services, lambda: _session(tmp_path))
    route = respx.post(f"{BASE}/persona/services").mock(
        return_value=httpx.Response(201, json={"id": "9", "name": "svc",
            "providerKind": "openai", "baseUrl": "https://o.test", "status": "new"})
    )
    res = runner.invoke(app, [
        "create", "--set", "name=svc", "--set", "provider_kind=openai",
        "--set", "base_url=https://o.test", "--json",
    ])
    assert res.exit_code == 0, res.output
    assert route.called
    sent = route.calls.last.request
    assert b'"providerKind": "openai"' in sent.content


@respx.mock
def test_401_triggers_refresh_then_retry(tmp_path):
    sess = _session(tmp_path)
    sess.profile.refresh_token = "ref"
    services = next(res for res in r.PERSONA if res.name == "services")
    app = crud.build_resource_app(services, lambda: sess)
    respx.get(f"{BASE}/persona/services").mock(side_effect=[
        httpx.Response(401, json={"error": {"message": "expired"}}),
        httpx.Response(200, json=[]),
    ])
    respx.post(f"{BASE}/auth/refresh").mock(
        return_value=httpx.Response(200, json={"accessToken": "acc2"},
            headers={"set-cookie": "refresh_token=ref2; HttpOnly"})
    )
    res = runner.invoke(app, ["list", "--json"])
    assert res.exit_code == 0, res.output
    assert sess.profile.access_token == "acc2"


@respx.mock
def test_error_status_exits_nonzero(tmp_path):
    services = next(res for res in r.PERSONA if res.name == "services")
    app = crud.build_resource_app(services, lambda: _session(tmp_path))
    respx.get(f"{BASE}/persona/services").mock(
        return_value=httpx.Response(400, json={"error": {"message": "bad"}})
    )
    res = runner.invoke(app, ["list"])
    assert res.exit_code != 0
