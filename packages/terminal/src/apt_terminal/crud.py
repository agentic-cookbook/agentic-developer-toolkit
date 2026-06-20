from __future__ import annotations

import json
from collections.abc import Callable
from typing import Annotated, Any

import attrs
import typer

from apt_terminal import errors
from apt_terminal.auth import Session
from apt_terminal.errors import AptError
from apt_terminal.output import render
from apt_terminal.resources import Action, Resource

SetOpt = Annotated[list[str] | None, typer.Option("--set", help="FIELD=VALUE (repeatable)")]
JsonOpt = Annotated[bool, typer.Option("--json", help="Raw JSON output")]


def parse_set(pairs: list[str]) -> dict[str, object]:
    out: dict[str, object] = {}
    for pair in pairs:
        if "=" not in pair:
            raise AptError(f"--set expects FIELD=VALUE, got {pair!r}")
        key, _, raw = pair.partition("=")
        try:
            out[key.strip()] = json.loads(raw)
        except json.JSONDecodeError:
            out[key.strip()] = raw
    return out


def build_body(model: type, pairs: list[str]) -> object:
    try:
        known = {f.name for f in attrs.fields(model)}
    except Exception as exc:  # not an attrs class, etc.
        raise AptError(f"{model.__name__} is not a valid request body: {exc}") from exc
    kwargs = parse_set(pairs)
    unknown = set(kwargs) - known
    if unknown:
        allowed = ", ".join(sorted(known - {"additional_properties"}))
        raise AptError(f"unknown field(s): {', '.join(sorted(unknown))}. allowed: {allowed}")
    try:
        return model(**kwargs)
    except TypeError as exc:
        raise AptError(
            f"invalid fields for {model.__name__}: {exc}. "
            f"Note: --set values are JSON-parsed (true/false/null/numbers become typed); "
            f"quote a literal, e.g. --set name='\"true\"'."
        ) from exc


def execute(
    op: Any,
    *,
    session: Session,
    path_args: tuple[Any, ...] = (),
    body: object | None = None,
    json_out: bool = False,
) -> None:
    """Call op via raw httpx, retry once on 401, then render or raise."""

    def call(client: Any) -> Any:
        # Build the request from the generated op's own kwargs (keeps routes +
        # body serialization in one place), but issue it with raw httpx and
        # render the server's raw JSON below. We deliberately do NOT use the
        # generated sync_detailed(): its strict attrs from_dict() raises on any
        # field drift between the spec and the live server (which we know
        # exists, e.g. auth token vs accessToken), and a display tool should
        # show whatever the server actually returned.
        kwargs = op._get_kwargs(*path_args, **({"body": body} if body is not None else {}))
        return client.get_httpx_client().request(**kwargs)

    client = session.client_factory()
    resp = call(client)

    if resp.status_code == 401 and session.refresh():
        client = session.client_factory()
        resp = call(client)

    if resp.status_code >= 400:
        raise errors.error_for_status(resp.status_code, errors.message_from_bytes(resp.content, f"HTTP {resp.status_code}"))

    try:
        data = resp.json()
    except ValueError:
        data = None
    render(data, json_out)


def build_resource_app(res: Resource, session_getter: Callable[[], Session]) -> typer.Typer:
    app = typer.Typer(name=res.name, help=f"{res.domain} {res.name}", no_args_is_help=True)
    ops = res.ops

    if ops.list_ is not None:
        @app.command("list")
        def list_(json_: JsonOpt = False) -> None:
            execute(ops.list_, session=session_getter(), json_out=json_)
        app.command("ls", hidden=True)(list_)

    if ops.get is not None:
        @app.command("get")
        def get(id: str, json_: JsonOpt = False) -> None:
            execute(ops.get, session=session_getter(), path_args=(id,), json_out=json_)

    if ops.create is not None and res.create_body is not None:
        _create_body: type = res.create_body

        @app.command("create")
        def create(set_: SetOpt = None, json_: JsonOpt = False) -> None:
            body = build_body(_create_body, set_ or [])
            execute(ops.create, session=session_getter(), body=body, json_out=json_)

    if ops.update is not None and res.update_body is not None:
        _update_body: type = res.update_body

        @app.command("update")
        def update(id: str, set_: SetOpt = None, json_: JsonOpt = False) -> None:
            body = build_body(_update_body, set_ or [])
            execute(ops.update, session=session_getter(), path_args=(id,), body=body, json_out=json_)

    if ops.delete is not None:
        @app.command("delete")
        def delete(id: str, json_: JsonOpt = False) -> None:
            execute(ops.delete, session=session_getter(), path_args=(id,), json_out=json_)
        app.command("rm", hidden=True)(delete)

    for action in res.actions:
        _register_action(app, action, session_getter)

    return app


def _register_action(app: typer.Typer, action: Action, session_getter: Callable[[], Session]) -> None:
    @app.command(action.name, help=action.help)
    def _action(id: str, json_: JsonOpt = False) -> None:
        execute(action.op, session=session_getter(), path_args=(id,), json_out=json_)
