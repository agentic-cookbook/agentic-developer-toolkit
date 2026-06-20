from __future__ import annotations

from collections.abc import Callable
from typing import Annotated

import typer

from apt_terminal.auth import Session
from apt_terminal.output import emit_json, emit_text


def build_auth_app(session_getter: Callable[[], Session]) -> typer.Typer:
    app = typer.Typer(name="auth", help="Authentication", no_args_is_help=True)

    @app.command("login")
    def login(
        email: Annotated[str, typer.Option(prompt=True)],
        password: Annotated[str, typer.Option(prompt=True, hide_input=True)],
    ) -> None:
        who = session_getter().login(email, password)
        emit_text(f"Logged in as {who}")

    @app.command("logout")
    def logout() -> None:
        session_getter().logout()
        emit_text("Logged out.")

    @app.command("whoami")
    def whoami() -> None:
        emit_json(session_getter().whoami())

    @app.command("refresh")
    def refresh() -> None:
        ok = session_getter().refresh()
        emit_text("Refreshed." if ok else "Could not refresh — run 'apt auth login'.")

    return app
