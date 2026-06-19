from __future__ import annotations

import httpx
import respx
from typer.testing import CliRunner

from apt_terminal import cli

runner = CliRunner()


def test_help_lists_domains(monkeypatch, tmp_path):
    monkeypatch.setenv("APT_CONFIG", str(tmp_path / "config.toml"))
    res = runner.invoke(cli.app, ["--help"])
    assert res.exit_code == 0
    for group in ("auth", "persona", "public", "config"):
        assert group in res.output


def test_persona_services_mounted(monkeypatch, tmp_path):
    monkeypatch.setenv("APT_CONFIG", str(tmp_path / "config.toml"))
    res = runner.invoke(cli.app, ["persona", "services", "--help"])
    assert res.exit_code == 0
    assert "create" in res.output and "connect" in res.output


@respx.mock
def test_persona_services_list_end_to_end(monkeypatch, tmp_path):
    cfgfile = tmp_path / "config.toml"
    cfgfile.write_text(
        'default_profile = "default"\n[profiles.default]\n'
        'base_url = "https://api.test"\naccess_token = "acc"\n'
    )
    monkeypatch.setenv("APT_CONFIG", str(cfgfile))
    respx.get("https://api.test/persona/services").mock(
        return_value=httpx.Response(200, json=[{"id": "1", "name": "svc"}])
    )
    res = runner.invoke(cli.app, ["persona", "services", "list", "--json"])
    assert res.exit_code == 0, res.output
    assert '"id": "1"' in res.output
