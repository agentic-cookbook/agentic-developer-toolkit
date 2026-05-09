from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path
from typing import Annotated, Any

import tomli_w
import typer

from apt_terminal import config as config_mod
from apt_terminal.errors import AptError, AuthError, ConfigError
from apt_terminal.http import HttpClient
from apt_terminal.output import confirm, emit_json, emit_kv, emit_table, emit_text, warn
from apt_terminal.registry.client import RegistryClient, RegistryPublicClient

app = typer.Typer(help="Administer agenticregistry", no_args_is_help=True)


JsonOpt = Annotated[bool, typer.Option("--json", "-j", help="Emit raw JSON")]
YesOpt = Annotated[bool, typer.Option("--yes", "-y", help="Skip confirmation")]

# fields a persona spec accepts via --from FILE or `persona edit`
PERSONA_FIELDS = (
    "slug",
    "name",
    "description",
    "modelPrompt",
    "voice",
    "character",
    "examples",
    "serviceId",
    "model",
    "visibility",
)


# ---------------------------------------------------------------------------
# helpers


def _client(ctx: typer.Context) -> RegistryClient:
    p = ctx.obj["profile"]
    if not p.registry_backend.key:
        raise AuthError("registry key not set; run `apt registry login`")
    return RegistryClient(HttpClient(p.registry_backend.url, key=p.registry_backend.key))


def _public(ctx: typer.Context) -> RegistryPublicClient:
    p = ctx.obj["profile"]
    return RegistryPublicClient(HttpClient(p.registry_public.url))


def _maybe_json(as_json: bool, value: Any) -> bool:
    if as_json:
        emit_json(value)
        return True
    return False


def _read_spec_file(path: Path) -> dict[str, Any]:
    text = path.read_text()
    if path.suffix in {".toml", ".tml"}:
        return dict(tomllib.loads(text))
    return dict(json.loads(text))


# ---------------------------------------------------------------------------
# auth & keys


@app.command()
def login(ctx: typer.Context) -> None:
    """Save a registry API key into the active profile."""
    p = ctx.obj["profile"]
    cfg = ctx.obj["config"]
    url = typer.prompt("Registry backend URL", default=p.registry_backend.url)
    key = typer.prompt("API key (paste)", hide_input=True)
    p.registry_backend.url = url.strip()
    p.registry_backend.key = key.strip()
    config_mod.save(cfg)
    emit_text(f"saved → {cfg.path}")


@app.command()
def whoami(ctx: typer.Context, as_json: JsonOpt = False) -> None:
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


user_app = typer.Typer(help="User profile", no_args_is_help=True)
app.add_typer(user_app, name="user")


@user_app.command("set-name")
def user_set_name(ctx: typer.Context, name: str, as_json: JsonOpt = False) -> None:
    user = _client(ctx).set_display_name(name)
    if _maybe_json(as_json, user.model_dump(mode="json")):
        return
    emit_text(f"displayName → {user.displayName}")


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
    scopes: Annotated[list[str] | None, typer.Option("--scope")] = None,
    expires: Annotated[str | None, typer.Option("--expires")] = None,
    as_json: JsonOpt = False,
) -> None:
    created = _client(ctx).keys_create(name, scopes=scopes, expires_at=expires)
    if _maybe_json(as_json, created.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("id", created.key.id),
            ("name", created.key.name),
            ("rawKey", created.rawKey),
            ("scopes", created.key.scopes),
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
# personas

persona_app = typer.Typer(help="Personas (admin)", no_args_is_help=True)
app.add_typer(persona_app, name="persona")


@persona_app.command("list")
def persona_list(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    rows = _client(ctx).persona_list()
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["slug", "name", "visibility", "model", "updatedAt"],
    )


@persona_app.command("get")
@persona_app.command("show")
def persona_get(ctx: typer.Context, slug_or_id: str, as_json: JsonOpt = False) -> None:
    p = _client(ctx).persona_get(slug_or_id)
    if _maybe_json(as_json, p.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("slug", p.slug),
            ("name", p.name),
            ("description", p.description),
            ("model", p.model),
            ("serviceId", p.serviceId),
            ("visibility", p.visibility),
            ("voice", p.voice),
            ("character", p.character),
            ("modelPrompt", _truncate(p.modelPrompt, 200)),
        ]
    )


def _truncate(s: str | None, n: int) -> str | None:
    if s is None:
        return None
    if len(s) <= n:
        return s
    return s[:n] + "…"


def _persona_body_from_flags(
    *,
    slug: str | None,
    name: str | None,
    description: str | None,
    prompt: str | None,
    voice: str | None,
    character: str | None,
    examples: str | None,
    service_id: str | None,
    model: str | None,
    visibility: str | None,
    base: dict[str, Any] | None = None,
) -> dict[str, Any]:
    body = dict(base or {})
    if slug is not None:
        body["slug"] = slug
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if prompt is not None:
        body["modelPrompt"] = prompt
    if voice is not None:
        body["voice"] = voice
    if character is not None:
        body["character"] = character
    if examples is not None:
        body["examples"] = examples
    if service_id is not None:
        body["serviceId"] = service_id
    if model is not None:
        body["model"] = model
    if visibility is not None:
        body["visibility"] = visibility
    return body


@persona_app.command("create")
def persona_create(
    ctx: typer.Context,
    from_file: Annotated[
        Path | None, typer.Option("--from", help="TOML or JSON spec; flags override")
    ] = None,
    slug: Annotated[str | None, typer.Option("--slug")] = None,
    name: Annotated[str | None, typer.Option("--name")] = None,
    description: Annotated[str | None, typer.Option("--description")] = None,
    prompt: Annotated[str | None, typer.Option("--prompt", help="modelPrompt")] = None,
    voice: Annotated[str | None, typer.Option("--voice")] = None,
    character: Annotated[str | None, typer.Option("--character")] = None,
    examples: Annotated[str | None, typer.Option("--examples")] = None,
    service_id: Annotated[str | None, typer.Option("--service-id")] = None,
    model: Annotated[str | None, typer.Option("--model")] = None,
    visibility: Annotated[str | None, typer.Option("--visibility")] = None,
    as_json: JsonOpt = False,
) -> None:
    base = _read_spec_file(from_file) if from_file else None
    body = _persona_body_from_flags(
        slug=slug,
        name=name,
        description=description,
        prompt=prompt,
        voice=voice,
        character=character,
        examples=examples,
        service_id=service_id,
        model=model,
        visibility=visibility,
        base=base,
    )
    if "slug" not in body or "name" not in body or "modelPrompt" not in body:
        raise ConfigError("persona create requires at minimum slug, name, modelPrompt")
    created = _client(ctx).persona_create(body)
    if _maybe_json(as_json, created.model_dump(mode="json")):
        return
    emit_text(f"created persona {created.slug} ({created.id})")


@persona_app.command("update")
def persona_update(
    ctx: typer.Context,
    slug_or_id: str,
    from_file: Annotated[Path | None, typer.Option("--from")] = None,
    slug: Annotated[str | None, typer.Option("--slug")] = None,
    name: Annotated[str | None, typer.Option("--name")] = None,
    description: Annotated[str | None, typer.Option("--description")] = None,
    prompt: Annotated[str | None, typer.Option("--prompt")] = None,
    voice: Annotated[str | None, typer.Option("--voice")] = None,
    character: Annotated[str | None, typer.Option("--character")] = None,
    examples: Annotated[str | None, typer.Option("--examples")] = None,
    service_id: Annotated[str | None, typer.Option("--service-id")] = None,
    model: Annotated[str | None, typer.Option("--model")] = None,
    visibility: Annotated[str | None, typer.Option("--visibility")] = None,
    as_json: JsonOpt = False,
) -> None:
    client = _client(ctx)
    existing = client.persona_get(slug_or_id)
    if existing.id is None:
        raise AptError("persona has no id; cannot update")
    base = _read_spec_file(from_file) if from_file else None
    body = _persona_body_from_flags(
        slug=slug,
        name=name,
        description=description,
        prompt=prompt,
        voice=voice,
        character=character,
        examples=examples,
        service_id=service_id,
        model=model,
        visibility=visibility,
        base=base,
    )
    if not body:
        raise ConfigError("nothing to update; pass --from or any field flag")
    updated = client.persona_update(existing.id, body)
    if _maybe_json(as_json, updated.model_dump(mode="json")):
        return
    emit_text(f"updated persona {updated.slug}")


@persona_app.command("delete")
def persona_delete(ctx: typer.Context, slug_or_id: str, yes: YesOpt = False) -> None:
    client = _client(ctx)
    p = client.persona_get(slug_or_id)
    if p.id is None:
        raise AptError("persona has no id")
    if not confirm(f"delete persona {p.slug} ({p.id})?", assume_yes=yes):
        raise typer.Exit(1)
    client.persona_delete(p.id)
    emit_text(f"deleted {p.slug}")


@persona_app.command("edit")
def persona_edit(ctx: typer.Context, slug_or_id: str) -> None:
    """Open the persona in $EDITOR as TOML; save back via PUT."""
    client = _client(ctx)
    persona = client.persona_get(slug_or_id)
    if persona.id is None:
        raise AptError("persona has no id; cannot edit")
    body = {f: getattr(persona, f) for f in PERSONA_FIELDS if getattr(persona, f) is not None}
    text = tomli_w.dumps(body)
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".toml", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(text)
        tmp_path = Path(tmp.name)
    try:
        subprocess.call([editor, str(tmp_path)])
        new_text = tmp_path.read_text()
        if new_text == text:
            emit_text("no changes")
            return
        new_body = dict(tomllib.loads(new_text))
    finally:
        tmp_path.unlink(missing_ok=True)
    updated = client.persona_update(persona.id, new_body)
    emit_text(f"updated persona {updated.slug}")


# ---------------------------------------------------------------------------
# public discovery


@app.command()
def search(
    ctx: typer.Context,
    query: Annotated[str | None, typer.Argument()] = None,
    service: Annotated[str | None, typer.Option("--service")] = None,
    limit: Annotated[int | None, typer.Option("--limit", "-n")] = None,
    cursor: Annotated[str | None, typer.Option("--cursor")] = None,
    as_json: JsonOpt = False,
) -> None:
    """Search public personas (no auth)."""
    result = _public(ctx).search(query=query, service=service, limit=limit, cursor=cursor)
    if _maybe_json(as_json, result):
        return
    items = result.get("data") or []
    emit_table(items, columns=["slug", "name", "model"])
    next_cursor = result.get("nextCursor")
    if next_cursor:
        emit_text(f"next: --cursor {next_cursor}")


@app.command("public-get")
def public_get(ctx: typer.Context, slug: str, as_json: JsonOpt = False) -> None:
    """Fetch a public persona by slug (no auth)."""
    p = _public(ctx).public_persona(slug)
    if _maybe_json(as_json, p.model_dump(mode="json")):
        return
    emit_kv(
        [
            ("slug", p.slug),
            ("name", p.name),
            ("description", p.description),
            ("modelPrompt", _truncate(p.modelPrompt, 200)),
        ]
    )


@app.command()
def version(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    """Show registry server version."""
    v = _public(ctx).version()
    if _maybe_json(as_json, v.model_dump(mode="json")):
        return
    emit_text(v.version)


# ---------------------------------------------------------------------------
# persona services

service_app = typer.Typer(help="Persona services (LLM connections)", no_args_is_help=True)
app.add_typer(service_app, name="service")


@service_app.command("list")
def service_list(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    rows = _client(ctx).service_list()
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["id", "name", "templateId", "status", "baseUrl"],
    )


@service_app.command("templates")
def service_templates(ctx: typer.Context, as_json: JsonOpt = False) -> None:
    rows = _client(ctx).templates_list()
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table(
        [r.model_dump(mode="json") for r in rows],
        columns=["id", "name", "provider", "defaultBaseUrl"],
    )


@service_app.command("add")
def service_add(
    ctx: typer.Context,
    template: Annotated[str, typer.Option("--template", help="Service-template id")],
    name: Annotated[str, typer.Option("--name")],
    api_key: Annotated[str | None, typer.Option("--api-key")] = None,
    api_key_stdin: Annotated[bool, typer.Option("--api-key-stdin")] = False,
    base_url: Annotated[str | None, typer.Option("--base-url")] = None,
    as_json: JsonOpt = False,
) -> None:
    if api_key_stdin:
        api_key = sys.stdin.read().strip()
    if not api_key:
        api_key = typer.prompt("Provider API key", hide_input=True)
    svc = _client(ctx).service_create(
        template_id=template, name=name, api_key=api_key, base_url=base_url
    )
    if _maybe_json(as_json, svc.model_dump(mode="json")):
        return
    emit_text(f"added service {svc.name} ({svc.id})")


@service_app.command("update")
def service_update(
    ctx: typer.Context,
    service_id: str,
    name: Annotated[str | None, typer.Option("--name")] = None,
    api_key: Annotated[str | None, typer.Option("--api-key")] = None,
    api_key_stdin: Annotated[bool, typer.Option("--api-key-stdin")] = False,
    base_url: Annotated[str | None, typer.Option("--base-url")] = None,
    as_json: JsonOpt = False,
) -> None:
    if api_key_stdin:
        api_key = sys.stdin.read().strip()
    svc = _client(ctx).service_update(service_id, name=name, base_url=base_url, api_key=api_key)
    if _maybe_json(as_json, svc.model_dump(mode="json")):
        return
    emit_text(f"updated {svc.name}")


@service_app.command("test")
def service_test(ctx: typer.Context, service_id: str, as_json: JsonOpt = False) -> None:
    """Validate connectivity by hitting the provider."""
    result = _client(ctx).service_test(service_id)
    if _maybe_json(as_json, result):
        return
    emit_kv(list(result.items()))


@service_app.command("delete")
def service_delete(ctx: typer.Context, service_id: str, yes: YesOpt = False) -> None:
    if not confirm(f"delete service {service_id}?", assume_yes=yes):
        raise typer.Exit(1)
    _client(ctx).service_delete(service_id)
    emit_text("deleted")


models_app = typer.Typer(help="Service models", no_args_is_help=True)
service_app.add_typer(models_app, name="models")


@models_app.callback(invoke_without_command=True)
def service_models_default(
    ctx: typer.Context, service_id: Annotated[str | None, typer.Argument()] = None
) -> None:
    """List models for a service (default action)."""
    if ctx.invoked_subcommand is not None:
        return
    if not service_id:
        raise ConfigError("usage: apt registry service models <service-id>")
    rows = _client(ctx).service_models(service_id)
    emit_table([r.model_dump(mode="json") for r in rows], columns=["id", "name"])


@models_app.command("refresh")
def service_models_refresh(ctx: typer.Context, service_id: str, as_json: JsonOpt = False) -> None:
    rows = _client(ctx).service_models_refresh(service_id)
    if _maybe_json(as_json, [r.model_dump(mode="json") for r in rows]):
        return
    emit_table([r.model_dump(mode="json") for r in rows], columns=["id", "name"])
