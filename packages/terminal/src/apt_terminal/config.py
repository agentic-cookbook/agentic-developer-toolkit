from __future__ import annotations

import contextlib
import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

import tomli_w

from apt_terminal.errors import ConfigError

DEFAULT_STORAGE_URL = "https://api.myagenticstorage.com"
DEFAULT_REGISTRY_BACKEND_URL = "https://backend.agenticpersonaregistry.com"
DEFAULT_REGISTRY_PUBLIC_URL = "https://api.agenticpersonaregistry.com"


@dataclass
class ServiceConfig:
    url: str
    key: str | None = None


@dataclass
class Profile:
    name: str
    storage: ServiceConfig = field(default_factory=lambda: ServiceConfig(url=DEFAULT_STORAGE_URL))
    registry_backend: ServiceConfig = field(
        default_factory=lambda: ServiceConfig(url=DEFAULT_REGISTRY_BACKEND_URL)
    )
    registry_public: ServiceConfig = field(
        default_factory=lambda: ServiceConfig(url=DEFAULT_REGISTRY_PUBLIC_URL)
    )
    pinned_bucket: str | None = None


@dataclass
class Config:
    path: Path
    default_profile: str = "default"
    profiles: dict[str, Profile] = field(default_factory=dict)

    def profile(self, name: str | None = None) -> Profile:
        n = name or self.default_profile
        if n not in self.profiles:
            self.profiles[n] = Profile(name=n)
        return self.profiles[n]


def config_path() -> Path:
    override = os.environ.get("APT_CONFIG")
    if override:
        return Path(override).expanduser()
    xdg = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg).expanduser() if xdg else Path.home() / ".config"
    return base / "apt" / "config.toml"


def load(path: Path | None = None) -> Config:
    p = path or config_path()
    if not p.exists():
        return Config(path=p)
    try:
        with p.open("rb") as f:
            raw = tomllib.load(f)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise ConfigError(f"failed to read {p}: {exc}") from exc

    cfg = Config(path=p, default_profile=raw.get("default_profile", "default"))
    for name, body in (raw.get("profiles") or {}).items():
        cfg.profiles[name] = Profile(
            name=name,
            storage=_load_service(body.get("storage"), DEFAULT_STORAGE_URL),
            registry_backend=_load_service(
                body.get("registry_backend"), DEFAULT_REGISTRY_BACKEND_URL
            ),
            registry_public=_load_service(body.get("registry_public"), DEFAULT_REGISTRY_PUBLIC_URL),
            pinned_bucket=body.get("pinned_bucket"),
        )
    return cfg


def save(cfg: Config) -> None:
    cfg.path.parent.mkdir(parents=True, exist_ok=True)
    out: dict[str, object] = {
        "default_profile": cfg.default_profile,
        "profiles": {name: _dump_profile(p) for name, p in cfg.profiles.items()},
    }
    data = tomli_w.dumps(out).encode("utf-8")
    cfg.path.write_bytes(data)
    with contextlib.suppress(OSError):
        cfg.path.chmod(0o600)


def apply_env_overrides(profile: Profile) -> Profile:
    env = os.environ
    if v := env.get("APT_STORAGE_URL"):
        profile.storage.url = v
    if v := env.get("APT_STORAGE_KEY"):
        profile.storage.key = v
    if v := env.get("APT_REGISTRY_URL"):
        profile.registry_backend.url = v
    if v := env.get("APT_REGISTRY_PUBLIC_URL"):
        profile.registry_public.url = v
    if v := env.get("APT_REGISTRY_KEY"):
        profile.registry_backend.key = v
    return profile


def _load_service(body: object, default_url: str) -> ServiceConfig:
    if not isinstance(body, dict):
        return ServiceConfig(url=default_url)
    return ServiceConfig(
        url=str(body.get("url") or default_url),
        key=body.get("key"),
    )


def _dump_profile(p: Profile) -> dict[str, object]:
    out: dict[str, object] = {
        "storage": _dump_service(p.storage),
        "registry_backend": _dump_service(p.registry_backend),
        "registry_public": _dump_service(p.registry_public),
    }
    if p.pinned_bucket:
        out["pinned_bucket"] = p.pinned_bucket
    return out


def _dump_service(s: ServiceConfig) -> dict[str, object]:
    out: dict[str, object] = {"url": s.url}
    if s.key:
        out["key"] = s.key
    return out
