from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Any

import typer

from apt_terminal import config as config_mod
from apt_terminal.errors import AuthError, ConfigError
from apt_terminal.http import HttpClient
from apt_terminal.output import confirm, emit_json, emit_kv, emit_table, emit_text, warn
from apt_terminal.storage.client import StorageClient

app = typer.Typer(help="Administer my-agentic-storage", no_args_is_help=True)


# ---------------------------------------------------------------------------
# helpers


def _client(ctx: typer.Context) -> StorageClient:
    p = ctx.obj["profile"]
    if not p.storage.key:
        raise AuthError("storage key not set; run `apt storage login`")
    return StorageClient(HttpClient(p.storage.url, key=p.storage.key))


def _resolve_bucket_id(ctx: typer.Context, override: str | None) -> str:
    p = ctx.obj["profile"]
    name_or_id = override or p.pinned_bucket
    if not name_or_id:
        raise ConfigError(
            "no bucket specified; pass --bucket or run `apt storage bucket use <name|id>`"
        )
    client = _client(ctx)
    return client.resolve_bucket(name_or_id).id


def _parse_value(raw: str) -> Any:
    if raw.startswith("@"):
        raw = Path(raw[1:]).expanduser().read_text()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def _read_content(raw: str) -> str:
    if raw.startswith("@"):
        return Path(raw[1:]).expanduser().read_text()
    return raw


def _maybe_json(as_json: bool, value: Any) -> bool:
    if as_json:
        emit_json(value)
        return True
    return False


# ---------------------------------------------------------------------------
# auth & keys

BucketOpt = Annotated[str | None, typer.Option("--bucket", "-b", help="Bucket name or id")]
JsonOpt = Annotated[bool, typer.Option("--json", "-j", help="Emit raw JSON")]
YesOpt = Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation")]


@app.command()
def login(ctx: typer.Context) -> None:
    """Save a storage API key into the active profile."""
    p = ctx.obj["profile"]
    cfg = ctx.obj["config"]
    url = typer.prompt("Storage base URL", default=p.storage.url)
    key = typer.prompt("API key (paste)", hide_input=True)
    p.storage.url = url.strip()
    p.storage.key = key.strip()
    config_mod.save(cfg)
    emit_text(f"saved → {cfg.path}")


@app.command()
def whoami(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    """Show the authenticated user."""
    user = _client(ctx).whoami()
    if _maybe_json(as_json, user.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("id", user.id),
            ("github", user.githubLogin),
            ("email", user.email),
            ("displayName", user.displayName),
        ]
    )


keys_app = typer.Typer(help="API key management", no_args_is_help=True)
app.add_typer(keys_app, name="keys")


@keys_app.command("list")
def keys_list(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    keys = _client(ctx).keys_list()
    if _maybe_json(as_json, [k.model_dump(mode="json") for k in keys]):
        return
    emit_table(
        [k.model_dump(mode="json") for k in keys],
        columns=["id", "name", "keyPrefix", "scopes", "expiresAt", "createdAt"],
    )


@keys_app.command("create")
def keys_create(
    ctx: typer.Context,
    name: str,
    scopes: Annotated[
        list[str] | None,
        typer.Option("--scope", help="Scope string (repeatable), e.g. bucket:<id>:read"),
    ] = None,
    expires: Annotated[str | None, typer.Option("--expires", help="ISO timestamp")] = None,
    as_json: JsonOpt = False,
) -> None:
    """Create a new API key. Raw key shown once."""
    created = _client(ctx).keys_create(name, scopes=scopes, expires_at=expires)
    if _maybe_json(as_json, created.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("id", created.key.id),
            ("name", created.key.name),
            ("rawKey", created.rawKey),
            ("scopes", created.key.scopes),
            ("expiresAt", created.key.expiresAt),
        ]
    )
    warn("save the raw key — it is shown only once")


@keys_app.command("revoke")
def keys_revoke(ctx: typer.Context, key_id: str, yes: YesOpt = False) -> None:
    if not confirm(f"revoke key {key_id}?", assume_yes=yes):
        raise typer.Exit(1)
    _client(ctx).keys_revoke(key_id)
    emit_text("revoked")


# ---------------------------------------------------------------------------
# buckets

bucket_app = typer.Typer(help="Buckets", no_args_is_help=True)
app.add_typer(bucket_app, name="bucket")


@bucket_app.command("list")
def bucket_list(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    rows = _client(ctx).bucket_list()
    if _maybe_json(as_json, [b.model_dump(mode="json") for b in rows]):
        return
    emit_table(
        [b.model_dump(mode="json") for b in rows],
        columns=["id", "name", "description", "createdAt"],
    )


@bucket_app.command("create")
def bucket_create(
    ctx: typer.Context,
    name: str,
    description: Annotated[str | None, typer.Option("--description", "-d")] = None,
    as_json: JsonOpt = False,
) -> None:
    b = _client(ctx).bucket_create(name, description=description)
    if _maybe_json(as_json, b.model_dump(mode="json")):
        return
    emit_kv([("id", b.id), ("name", b.name), ("description", b.description)])


@bucket_app.command("get")
def bucket_get(ctx: typer.Context, name_or_id: str, as_json: JsonOpt = False) -> None:
    b = _client(ctx).resolve_bucket(name_or_id)
    if _maybe_json(as_json, b.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("id", b.id),
            ("name", b.name),
            ("description", b.description),
            ("createdAt", b.createdAt),
            ("updatedAt", b.updatedAt),
        ]
    )


@bucket_app.command("update")
def bucket_update(
    ctx: typer.Context,
    name_or_id: str,
    name: Annotated[str | None, typer.Option("--name", "-n")] = None,
    description: Annotated[str | None, typer.Option("--description", "-d")] = None,
    as_json: JsonOpt = False,
) -> None:
    client = _client(ctx)
    b = client.resolve_bucket(name_or_id)
    updated = client.bucket_update(b.id, name=name, description=description)
    if _maybe_json(as_json, updated.model_dump(mode="json")):
        return
    emit_kv([("id", updated.id), ("name", updated.name), ("description", updated.description)])


@bucket_app.command("delete")
def bucket_delete(ctx: typer.Context, name_or_id: str, yes: YesOpt = False) -> None:
    client = _client(ctx)
    b = client.resolve_bucket(name_or_id)
    if not confirm(f"delete bucket {b.name} ({b.id}) and all its data?", assume_yes=yes):
        raise typer.Exit(1)
    client.bucket_delete(b.id)
    emit_text(f"deleted {b.name}")


@bucket_app.command("use")
def bucket_use(ctx: typer.Context, name_or_id: str) -> None:
    """Pin a bucket so subsequent per-bucket commands can omit --bucket."""
    cfg = ctx.obj["config"]
    p = ctx.obj["profile"]
    bucket = _client(ctx).resolve_bucket(name_or_id)
    p.pinned_bucket = bucket.id
    config_mod.save(cfg)
    emit_text(f"pinned → {bucket.name} ({bucket.id})")


# ---------------------------------------------------------------------------
# lists

list_app = typer.Typer(help="Lists", no_args_is_help=True)
app.add_typer(list_app, name="list")


@list_app.command("ls")
def list_ls(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).list_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["id", "name", "description"])


@list_app.command("new")
def list_new(
    ctx: typer.Context,
    name: str,
    description: Annotated[str | None, typer.Option("--description", "-d")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    r = _client(ctx).list_create(bid, name, description=description)
    if _maybe_json(as_json, r.model_dump(mode="json")):
        return
    emit_text(f"created list {r.name}")


@list_app.command("rm")
def list_rm(ctx: typer.Context, name: str, bucket: BucketOpt = None, yes: YesOpt = False) -> None:
    if not confirm(f"delete list {name} (and items)?", assume_yes=yes):
        raise typer.Exit(1)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).list_delete(bid, name)
    emit_text("deleted")


@list_app.command("show")
def list_show(
    ctx: typer.Context, name: str, bucket: BucketOpt = None, as_json: JsonOpt = False
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    items = _client(ctx).list_items(bid, name)
    if _maybe_json(as_json, [i.model_dump(mode="json") for i in items]):
        return
    emit_table([i.model_dump(mode="json") for i in items], columns=["id", "position", "value"])


@list_app.command("append")
def list_append(
    ctx: typer.Context,
    name: str,
    value: str,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    item = _client(ctx).list_append(bid, name, _parse_value(value))
    if _maybe_json(as_json, item.model_dump(mode="json")):
        return
    emit_text(f"appended id={item.id} position={item.position}")


@list_app.command("remove-item")
def list_remove_item(
    ctx: typer.Context, name: str, item_id: str, bucket: BucketOpt = None, yes: YesOpt = False
) -> None:
    if not confirm(f"delete item {item_id} from {name}?", assume_yes=yes):
        raise typer.Exit(1)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).list_remove_item(bid, name, item_id)
    emit_text("deleted")


# ---------------------------------------------------------------------------
# kv

kv_app = typer.Typer(help="Key/value", no_args_is_help=True)
app.add_typer(kv_app, name="kv")


@kv_app.command("ls")
def kv_ls(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).kv_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["key", "value", "updatedAt"])


@kv_app.command("get")
def kv_get(
    ctx: typer.Context, key: str, bucket: BucketOpt = None, as_json: JsonOpt = False
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    entry = _client(ctx).kv_get(bid, key)
    if _maybe_json(as_json, entry.model_dump(mode="json")):
        return
    emit_text(json.dumps(entry.value, indent=2, default=str))


@kv_app.command("set")
def kv_set(
    ctx: typer.Context,
    key: str,
    value: str,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    entry = _client(ctx).kv_set(bid, key, _parse_value(value))
    if _maybe_json(as_json, entry.model_dump(mode="json")):
        return
    emit_text(f"set {entry.key}")


@kv_app.command("delete")
def kv_delete(ctx: typer.Context, key: str, bucket: BucketOpt = None, yes: YesOpt = False) -> None:
    if not confirm(f"delete kv {key}?", assume_yes=yes):
        raise typer.Exit(1)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).kv_delete(bid, key)
    emit_text("deleted")


# ---------------------------------------------------------------------------
# counters

counter_app = typer.Typer(help="Counters", no_args_is_help=True)
app.add_typer(counter_app, name="counter")


@counter_app.command("ls")
def counter_ls(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).counter_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["name", "value", "updatedAt"])


@counter_app.command("get")
def counter_get(
    ctx: typer.Context, name: str, bucket: BucketOpt = None, as_json: JsonOpt = False
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    c = _client(ctx).counter_get(bid, name)
    if _maybe_json(as_json, c.model_dump(mode="json")):
        return
    emit_text(c.value)


@counter_app.command("incr")
def counter_incr(
    ctx: typer.Context,
    name: str,
    by: Annotated[int, typer.Option("--by", help="Amount (negative to decrement)")] = 1,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    c = _client(ctx).counter_incr(bid, name, delta=by)
    if _maybe_json(as_json, c.model_dump(mode="json")):
        return
    emit_text(c.value)


@counter_app.command("set")
def counter_set(
    ctx: typer.Context,
    name: str,
    value: int,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    c = _client(ctx).counter_set(bid, name, value)
    if _maybe_json(as_json, c.model_dump(mode="json")):
        return
    emit_text(c.value)


@counter_app.command("reset")
def counter_reset(
    ctx: typer.Context, name: str, bucket: BucketOpt = None, yes: YesOpt = False
) -> None:
    if not confirm(f"reset counter {name}?", assume_yes=yes):
        raise typer.Exit(1)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).counter_reset(bid, name)
    emit_text("reset")


# ---------------------------------------------------------------------------
# events

event_app = typer.Typer(help="Events", no_args_is_help=True)
app.add_typer(event_app, name="event")


@event_app.command("log")
def event_log(
    ctx: typer.Context,
    payload: str,
    stream: Annotated[str | None, typer.Option("--stream", "-s")] = None,
    at: Annotated[str | None, typer.Option("--at", help="ISO occurredAt")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    ev = _client(ctx).event_log(bid, _parse_value(payload), stream=stream, occurred_at=at)
    if _maybe_json(as_json, ev.model_dump(mode="json")):
        return
    emit_text(f"logged id={ev.id} stream={ev.streamName}")


@event_app.command("tail")
def event_tail(
    ctx: typer.Context,
    stream: Annotated[str | None, typer.Option("--stream", "-s")] = None,
    since: Annotated[str | None, typer.Option("--since")] = None,
    until: Annotated[str | None, typer.Option("--until")] = None,
    limit: Annotated[int | None, typer.Option("--limit", "-n")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).event_query(bid, stream=stream, since=since, until=until, limit=limit)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["occurredAt", "streamName", "payload"],
    )


# ---------------------------------------------------------------------------
# queues

queue_app = typer.Typer(help="Queues", no_args_is_help=True)
app.add_typer(queue_app, name="queue")


@queue_app.command("list")
def queue_list(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).queue_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["id", "name", "createdAt"])


@queue_app.command("push")
def queue_push(
    ctx: typer.Context,
    name: str,
    payload: str,
    visible_at: Annotated[str | None, typer.Option("--visible-at")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    msg = _client(ctx).queue_push(bid, name, _parse_value(payload), visible_at=visible_at)
    if _maybe_json(as_json, msg.model_dump(mode="json")):
        return
    emit_text(f"pushed id={msg.id}")


@queue_app.command("pop")
def queue_pop(
    ctx: typer.Context,
    name: str,
    timeout: Annotated[int | None, typer.Option("--timeout", help="Visibility timeout (s)")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    msg = _client(ctx).queue_pop(bid, name, visibility_timeout_sec=timeout)
    if msg is None:
        if as_json:
            emit_json(None)
        else:
            emit_text("(empty)")
        return
    if _maybe_json(as_json, msg.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("id", msg.id),
            ("payload", msg.payload),
            ("attemptCount", msg.attemptCount),
            ("visibleAt", msg.visibleAt),
        ]
    )


@queue_app.command("ack")
def queue_ack(ctx: typer.Context, name: str, message_id: str, bucket: BucketOpt = None) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).queue_ack(bid, name, message_id)
    emit_text("acked")


@queue_app.command("nack")
def queue_nack(
    ctx: typer.Context,
    name: str,
    message_id: str,
    delay: Annotated[int | None, typer.Option("--delay", help="Re-deliver delay (s)")] = None,
    dead: Annotated[bool, typer.Option("--dead", help="Move to dead-letter status")] = False,
    bucket: BucketOpt = None,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).queue_nack(bid, name, message_id, delay_sec=delay, dead=dead)
    emit_text("nacked")


# ---------------------------------------------------------------------------
# memory

memory_app = typer.Typer(help="Memory blocks", no_args_is_help=True)
app.add_typer(memory_app, name="memory")


@memory_app.command("ls")
def memory_ls(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).memory_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["name", "sizeLimit", "updatedAt"],
    )


@memory_app.command("get")
def memory_get(
    ctx: typer.Context, name: str, bucket: BucketOpt = None, as_json: JsonOpt = False
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    block = _client(ctx).memory_get(bid, name)
    if _maybe_json(as_json, block.model_dump(mode="json")):
        return
    emit_text(block.content)


@memory_app.command("set")
def memory_set(
    ctx: typer.Context,
    name: str,
    content: str,
    limit: Annotated[int | None, typer.Option("--limit", help="Max bytes")] = None,
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    block = _client(ctx).memory_set(bid, name, _read_content(content), size_limit=limit)
    if _maybe_json(as_json, block.model_dump(mode="json")):
        return
    emit_text(f"set memory {block.name} ({len(block.content)} bytes)")


@memory_app.command("rm")
def memory_rm(ctx: typer.Context, name: str, bucket: BucketOpt = None, yes: YesOpt = False) -> None:
    if not confirm(f"delete memory {name}?", assume_yes=yes):
        raise typer.Exit(1)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).memory_delete(bid, name)
    emit_text("deleted")


# ---------------------------------------------------------------------------
# keywords

keyword_app = typer.Typer(help="Keywords / tagging", no_args_is_help=True)
app.add_typer(keyword_app, name="keyword")


@keyword_app.command("ls")
def keyword_ls(ctx: typer.Context, bucket: BucketOpt = None, as_json: JsonOpt = False) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).keyword_list(bid)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["id", "name", "createdAt"])


def _split_target(spec: str) -> tuple[str, str]:
    if ":" not in spec:
        raise typer.BadParameter("expected <kind>:<id>")
    kind, _, target_id = spec.partition(":")
    return kind, target_id


@keyword_app.command("tag")
def keyword_tag(
    ctx: typer.Context,
    keyword: str,
    target: Annotated[str, typer.Argument(help="<kind>:<id>")],
    bucket: BucketOpt = None,
    as_json: JsonOpt = False,
) -> None:
    kind, tid = _split_target(target)
    bid = _resolve_bucket_id(ctx, bucket)
    link = _client(ctx).keyword_tag(bid, keyword, target_kind=kind, target_id=tid)
    if _maybe_json(as_json, link.model_dump(mode="json")):
        return
    emit_text(f"tagged {kind}:{tid} with #{keyword}")


@keyword_app.command("untag")
def keyword_untag(
    ctx: typer.Context,
    keyword: str,
    target: Annotated[str, typer.Argument(help="<kind>:<id>")],
    bucket: BucketOpt = None,
) -> None:
    kind, tid = _split_target(target)
    bid = _resolve_bucket_id(ctx, bucket)
    _client(ctx).keyword_untag(bid, keyword, target_kind=kind, target_id=tid)
    emit_text("untagged")


@keyword_app.command("items")
def keyword_items(
    ctx: typer.Context, keyword: str, bucket: BucketOpt = None, as_json: JsonOpt = False
) -> None:
    bid = _resolve_bucket_id(ctx, bucket)
    rows = _client(ctx).keyword_items(bid, keyword)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["targetKind", "targetId", "createdAt"],
    )
