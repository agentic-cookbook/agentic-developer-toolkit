from __future__ import annotations

import httpx
import respx
from typer.testing import CliRunner

from apt_terminal import auth_commands, config as c
from apt_terminal.auth import Session

BASE = "https://api.test"
runner = CliRunner()


def _session(tmp_path) -> Session:
    cfg = c.Config(path=tmp_path / "config.toml")
    cfg.profile().base_url = BASE
    return Session(profile=cfg.profile(), config=cfg)


@respx.mock
def test_login_command(tmp_path):
    sess = _session(tmp_path)
    app = auth_commands.build_auth_app(lambda: sess)
    respx.post(f"{BASE}/auth/login").mock(
        return_value=httpx.Response(200, json={"accessToken": "a", "user": {"email": "u@x"}},
            headers={"set-cookie": "refresh_token=r; HttpOnly"})
    )
    res = runner.invoke(app, ["login", "--email", "u@x", "--password", "pw"])
    assert res.exit_code == 0, res.output
    assert sess.profile.access_token == "a"


@respx.mock
def test_whoami_command(tmp_path):
    sess = _session(tmp_path)
    sess.profile.access_token = "a"
    app = auth_commands.build_auth_app(lambda: sess)
    respx.get(f"{BASE}/auth/me").mock(
        return_value=httpx.Response(200, json={"email": "u@x", "id": "1"})
    )
    res = runner.invoke(app, ["whoami"])
    assert res.exit_code == 0, res.output
    assert "u@x" in res.output
