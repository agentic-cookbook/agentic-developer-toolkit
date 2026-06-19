from __future__ import annotations

import os
from pathlib import Path

from apt_terminal import config as c


def test_default_profile_uses_default_base_url(tmp_path):
    cfg = c.Config(path=tmp_path / "config.toml")
    p = cfg.profile()
    assert p.name == "default"
    assert p.base_url == c.DEFAULT_BASE_URL
    assert p.access_token is None


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "config.toml"
    cfg = c.Config(path=path, default_profile="work")
    p = cfg.profile("work")
    p.base_url = "https://example.test"
    p.access_token = "acc"
    p.refresh_token = "ref"
    c.save(cfg)

    again = c.load(path)
    assert again.default_profile == "work"
    q = again.profile("work")
    assert (q.base_url, q.access_token, q.refresh_token) == (
        "https://example.test", "acc", "ref",
    )


def test_save_sets_0600(tmp_path):
    path = tmp_path / "config.toml"
    cfg = c.Config(path=path)
    cfg.profile().access_token = "x"
    c.save(cfg)
    assert (path.stat().st_mode & 0o777) == 0o600


def test_env_overrides(monkeypatch, tmp_path):
    cfg = c.Config(path=tmp_path / "config.toml")
    p = cfg.profile()
    monkeypatch.setenv("APT_BASE_URL", "https://env.test")
    monkeypatch.setenv("APT_TOKEN", "env-token")
    c.apply_env_overrides(p)
    assert p.base_url == "https://env.test"
    assert p.access_token == "env-token"


def test_config_path_env_override(monkeypatch):
    monkeypatch.setenv("APT_CONFIG", "/tmp/custom/apt.toml")
    assert c.config_path() == Path("/tmp/custom/apt.toml")
