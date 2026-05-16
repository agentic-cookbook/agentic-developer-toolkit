from __future__ import annotations

from pathlib import Path

import pytest

from apt_terminal import config as cfgmod
from apt_terminal.config import (
    DEFAULT_REGISTRY_BACKEND_URL,
    DEFAULT_STORAGE_URL,
    Config,
    Profile,
    ServiceConfig,
    apply_env_overrides,
    config_path,
    load,
    save,
)


def test_config_path_uses_apt_config_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    target = tmp_path / "custom.toml"
    monkeypatch.setenv("APT_CONFIG", str(target))
    assert config_path() == target


def test_config_path_uses_xdg(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.delenv("APT_CONFIG", raising=False)
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    assert config_path() == tmp_path / "apt" / "config.toml"


def test_load_missing_returns_empty(tmp_path: Path) -> None:
    p = tmp_path / "nope.toml"
    cfg = load(p)
    assert cfg.path == p
    assert cfg.profiles == {}


def test_save_then_load_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "config.toml"
    cfg = Config(path=path, default_profile="default")
    profile = Profile(
        name="default",
        storage=ServiceConfig(url="https://s.example", key="storage-secret"),
        pinned_bucket="my-bucket",
    )
    cfg.profiles["default"] = profile
    save(cfg)

    loaded = load(path)
    assert loaded.default_profile == "default"
    p = loaded.profiles["default"]
    assert p.storage.url == "https://s.example"
    assert p.storage.key == "storage-secret"
    assert p.pinned_bucket == "my-bucket"
    assert p.registry_backend.url == DEFAULT_REGISTRY_BACKEND_URL


def test_save_sets_mode_0600(tmp_path: Path) -> None:
    path = tmp_path / "config.toml"
    cfg = Config(path=path)
    cfg.profiles["default"] = Profile(name="default")
    save(cfg)
    mode = path.stat().st_mode & 0o777
    assert mode == 0o600


def test_profile_creates_default_on_demand() -> None:
    cfg = Config(path=Path("/tmp/x"))
    p = cfg.profile()
    assert p.name == "default"
    assert p.storage.url == DEFAULT_STORAGE_URL


def test_apply_env_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APT_STORAGE_URL", "https://override-storage")
    monkeypatch.setenv("APT_STORAGE_KEY", "k1")
    monkeypatch.setenv("APT_REGISTRY_URL", "https://override-registry")
    monkeypatch.setenv("APT_REGISTRY_KEY", "k2")
    monkeypatch.setenv("APT_REGISTRY_PUBLIC_URL", "https://override-public")

    p = Profile(name="default")
    apply_env_overrides(p)
    assert p.storage.url == "https://override-storage"
    assert p.storage.key == "k1"
    assert p.registry_backend.url == "https://override-registry"
    assert p.registry_backend.key == "k2"
    assert p.registry_public.url == "https://override-public"


def test_load_corrupt_toml_raises(tmp_path: Path) -> None:
    path = tmp_path / "config.toml"
    path.write_text("not = valid = toml")
    with pytest.raises(cfgmod.ConfigError):
        load(path)
