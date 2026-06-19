from __future__ import annotations

import httpx
import respx
from typer.testing import CliRunner

from apt_terminal import config as c
from apt_terminal import public
from apt_terminal.auth import Session

BASE = "https://api.test"
runner = CliRunner()


def _session(tmp_path) -> Session:
    cfg = c.Config(path=tmp_path / "config.toml")
    cfg.profile().base_url = BASE
    return Session(profile=cfg.profile(), config=cfg)


@respx.mock
def test_public_persona(tmp_path):
    app = public.build_public_app(lambda: _session(tmp_path))
    respx.get(f"{BASE}/public/personas/zed").mock(
        return_value=httpx.Response(200, json={"slug": "zed", "name": "Zed"})
    )
    res = runner.invoke(app, ["persona", "zed", "--json"])
    assert res.exit_code == 0, res.output
    assert "zed" in res.output


@respx.mock
def test_public_user(tmp_path):
    app = public.build_public_app(lambda: _session(tmp_path))
    respx.get(f"{BASE}/public/users/zed").mock(
        return_value=httpx.Response(200, json={"slug": "zed", "name": "Zed"})
    )
    res = runner.invoke(app, ["user", "zed", "--json"])
    assert res.exit_code == 0, res.output
    assert "zed" in res.output
