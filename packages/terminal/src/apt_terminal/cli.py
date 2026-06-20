from __future__ import annotations

from typing import Annotated

import httpx
import typer

from apt_terminal import __version__, auth_commands, crud, public
from apt_terminal import config as config_mod
from apt_terminal.auth import Session
from apt_terminal.errors import AptError
from apt_terminal.output import die, emit_kv, emit_text
from apt_terminal.resources import ALL_DOMAINS, AUTH_TOKENS

app = typer.Typer(
    name="apt",
    help="CLI for the Agentic Developer backend",
    no_args_is_help=True,
    add_completion=False,
)

_STATE: dict[str, object] = {}


def get_session() -> Session:
    cfg: config_mod.Config = _STATE["config"]  # type: ignore[assignment]
    profile: config_mod.Profile = _STATE["profile"]  # type: ignore[assignment]
    return Session(profile=profile, config=cfg)


# auth group (hand-written login/etc. + the tokens resource)
auth_app = auth_commands.build_auth_app(get_session)
for res in AUTH_TOKENS:
    auth_app.add_typer(crud.build_resource_app(res, get_session), name=res.name)
app.add_typer(auth_app, name="auth")

# resource domains
for domain, resources in ALL_DOMAINS.items():
    domain_app = typer.Typer(name=domain, help=f"{domain} resources", no_args_is_help=True)
    for res in resources:
        domain_app.add_typer(crud.build_resource_app(res, get_session), name=res.name)
    app.add_typer(domain_app, name=domain)

# public + config
app.add_typer(public.build_public_app(get_session), name="public")
config_app = typer.Typer(help="Inspect and edit local config", no_args_is_help=True)
app.add_typer(config_app, name="config")


def _version_callback(value: bool) -> None:
    if value:
        emit_text(f"apt {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    profile: Annotated[str | None, typer.Option("--profile", "-p", help="Config profile")] = None,
    version: Annotated[
        bool | None,
        typer.Option("--version", callback=_version_callback, is_eager=True, help="Print version"),
    ] = None,
) -> None:
    cfg = config_mod.load()
    p = cfg.profile(profile or cfg.default_profile)
    _STATE["config"] = cfg
    _STATE["profile"] = p


@config_app.command("show")
def config_show() -> None:
    p: config_mod.Profile = _STATE["profile"]  # type: ignore[assignment]
    emit_kv([
        ("profile", p.name),
        ("base_url", p.base_url),
        ("logged_in", "yes" if p.access_token else "no"),
    ])


@config_app.command("path")
def config_path_cmd() -> None:
    emit_text(str(config_mod.config_path()))


def _run() -> None:
    try:
        app()
    except AptError as exc:
        die(str(exc), code=exc.exit_code)
    except httpx.HTTPError as exc:
        die(f"network error: {exc}", code=1)


if __name__ == "__main__":
    _run()
