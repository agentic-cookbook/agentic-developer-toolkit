from __future__ import annotations

from typing import Annotated

import typer

from apt_terminal import __version__
from apt_terminal import config as config_mod
from apt_terminal.errors import AptError
from apt_terminal.output import die, emit_kv, emit_text
from apt_terminal.registry.commands import app as registry_app
from apt_terminal.storage.commands import app as storage_app

app = typer.Typer(
    name="apt",
    help="CLI for agenticregistry + my-agentic-storage",
    no_args_is_help=True,
    add_completion=False,
)

app.add_typer(storage_app, name="storage")
app.add_typer(registry_app, name="registry")


config_app = typer.Typer(help="Inspect and edit local config", no_args_is_help=True)
app.add_typer(config_app, name="config")


def _version_callback(value: bool) -> None:
    if value:
        emit_text(f"apt {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p", help="Config profile to use"),
    ] = None,
    quiet: Annotated[
        bool, typer.Option("--quiet", "-q", help="Suppress non-essential output")
    ] = False,
    verbose: Annotated[bool, typer.Option("--verbose", "-V", help="Verbose output")] = False,
    version: Annotated[
        bool | None,
        typer.Option(
            "--version", callback=_version_callback, is_eager=True, help="Print version and exit"
        ),
    ] = None,
) -> None:
    cfg = config_mod.load()
    name = profile or cfg.default_profile
    p = cfg.profile(name)
    config_mod.apply_env_overrides(p)
    ctx.ensure_object(dict)
    ctx.obj["config"] = cfg
    ctx.obj["profile"] = p
    ctx.obj["quiet"] = quiet
    ctx.obj["verbose"] = verbose


@config_app.command("show")
def config_show(ctx: typer.Context) -> None:
    """Print the active profile (keys redacted)."""
    p = ctx.obj["profile"]
    emit_kv(
        [
            ("profile", p.name),
            ("storage.url", p.storage.url),
            ("storage.key", _redact(p.storage.key)),
            ("registry.backend.url", p.registry_backend.url),
            ("registry.backend.key", _redact(p.registry_backend.key)),
            ("registry.public.url", p.registry_public.url),
            ("pinned_bucket", p.pinned_bucket),
        ]
    )


@config_app.command("path")
def config_path_cmd() -> None:
    """Print the config file path."""
    emit_text(str(config_mod.config_path()))


@config_app.command("edit")
def config_edit() -> None:
    """Open the config file in $EDITOR."""
    import os
    import subprocess

    path = config_mod.config_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.touch(mode=0o600)
    editor = os.environ.get("EDITOR", "vi")
    subprocess.call([editor, str(path)])


def _redact(key: str | None) -> str | None:
    if not key:
        return None
    if len(key) <= 8:
        return "***"
    return f"{key[:4]}…{key[-4:]}"


def _run() -> None:
    try:
        app()
    except AptError as exc:
        die(str(exc), code=exc.exit_code)


if __name__ == "__main__":
    _run()
