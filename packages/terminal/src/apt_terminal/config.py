from __future__ import annotations

import contextlib
import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

import tomli_w

from apt_terminal.errors import ConfigError

DEFAULT_BASE_URL = "https://api.agenticdeveloperstorage.com"


@dataclass
class Profile:
    name: str
    base_url: str = DEFAULT_BASE_URL
    access_token: str | None = None
    refresh_token: str | None = None


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
            base_url=str(body.get("base_url") or DEFAULT_BASE_URL),
            access_token=body.get("access_token"),
            refresh_token=body.get("refresh_token"),
        )
    return cfg


def save(cfg: Config) -> None:
    cfg.path.parent.mkdir(parents=True, exist_ok=True)
    out: dict[str, object] = {
        "default_profile": cfg.default_profile,
        "profiles": {name: _dump_profile(p) for name, p in cfg.profiles.items()},
    }
    cfg.path.write_bytes(tomli_w.dumps(out).encode("utf-8"))
    with contextlib.suppress(OSError):
        cfg.path.chmod(0o600)


def apply_env_overrides(profile: Profile) -> Profile:
    env = os.environ
    if v := env.get("APT_BASE_URL"):
        profile.base_url = v
    if v := env.get("APT_TOKEN"):
        profile.access_token = v
    return profile


def _dump_profile(p: Profile) -> dict[str, object]:
    out: dict[str, object] = {"base_url": p.base_url}
    if p.access_token:
        out["access_token"] = p.access_token
    if p.refresh_token:
        out["refresh_token"] = p.refresh_token
    return out
