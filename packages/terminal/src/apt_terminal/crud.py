from __future__ import annotations

import json
from collections.abc import Callable
from typing import Annotated, Any

import attrs
import typer

from apt_terminal.auth import Session
from apt_terminal.errors import AptError
from apt_terminal.output import emit_json, emit_table, emit_text
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
    known = {f.name for f in attrs.fields(model)}
    kwargs = parse_set(pairs)
    unknown = set(kwargs) - known
    if unknown:
        allowed = ", ".join(sorted(known - {"additional_properties"}))
        raise AptError(f"unknown field(s): {', '.join(sorted(unknown))}. allowed: {allowed}")
    try:
        return model(**kwargs)
    except TypeError as exc:
        raise AptError(f"invalid fields for {model.__name__}: {exc}") from exc


def _render(data: Any, json_out: bool) -> None:
    if data is None:
        return
    if json_out:
        emit_json(data)
        return
    if isinstance(data, list):
        if data and all(isinstance(item, dict) for item in data):
            emit_table(data)
        else:
            for item in data:
                emit_text(item if isinstance(item, str) else json.dumps(item, default=str))
        return
    if isinstance(data, dict):
        emit_table([data])
        return
    emit_text(str(data))


def _error_message(content: bytes, status: int) -> str:
    try:
        body = json.loads(content.decode() or "{}")
    except (ValueError, AttributeError):
        return f"HTTP {status}"
    if isinstance(body, dict):
        if isinstance(body.get("error"), dict):
            return str(body["error"].get("message") or f"HTTP {status}")
        return str(body.get("title") or body.get("message") or f"HTTP {status}")
    return f"HTTP {status}"


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
        raise AptError(_error_message(resp.content, resp.status_code))

    try:
        data = resp.json()
    except ValueError:
        data = None
    _render(data, json_out)


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
        @app.command("create")
        def create(set_: SetOpt = None, json_: JsonOpt = False) -> None:
            body = build_body(res.create_body, set_ or [])
            execute(ops.create, session=session_getter(), body=body, json_out=json_)

    if ops.update is not None and res.update_body is not None:
        @app.command("update")
        def update(id: str, set_: SetOpt = None, json_: JsonOpt = False) -> None:
            body = build_body(res.update_body, set_ or [])
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
