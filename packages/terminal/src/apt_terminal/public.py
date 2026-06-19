from __future__ import annotations

import json
from collections.abc import Callable
from typing import Annotated, Any

import typer

from apt_terminal.auth import Session
from apt_terminal.errors import AptError
from apt_terminal.generated.api.public import (
    get_public_personas_slug,
    get_public_users_slug,
)
from apt_terminal.output import emit_json, emit_table

JsonOpt = Annotated[bool, typer.Option("--json", help="Raw JSON output")]


def _run(op: Any, slug: str, session: Session, json_out: bool) -> None:
    # Use _get_kwargs + raw httpx to avoid field-drift errors in the generated
    # response parser (generated models may require fields absent from the live API).
    client = session.public_client()
    kwargs = op._get_kwargs(slug)
    raw = client.get_httpx_client().request(**kwargs)
    if raw.status_code >= 400:
        raise AptError(f"HTTP {raw.status_code}", exit_code=1)
    try:
        payload = raw.json()
    except ValueError:
        payload = None
    emit_json(payload) if json_out else emit_table([payload] if isinstance(payload, dict) else [])


def build_public_app(session_getter: Callable[[], Session]) -> typer.Typer:
    app = typer.Typer(name="public", help="Unauthenticated public lookups", no_args_is_help=True)

    @app.command("persona")
    def persona(slug: str, json_: JsonOpt = False) -> None:
        _run(get_public_personas_slug, slug, session_getter(), json_)

    @app.command("user")
    def user(slug: str, json_: JsonOpt = False) -> None:
        _run(get_public_users_slug, slug, session_getter(), json_)

    return app
