from __future__ import annotations

import json

import httpx
import pytest
import respx

from apt_terminal.errors import AuthError
from apt_terminal.registry.client import RegistryClient
from tests.conftest import REGISTRY_URL, envelope


def _persona(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "p1",
        "slug": "ada",
        "name": "Ada",
        "modelPrompt": "You are Ada.",
    }
    base.update(overrides)
    return base


def test_persona_list(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/personas").mock(
        return_value=httpx.Response(200, json=envelope([_persona()]))
    )
    rows = registry.persona_list()
    assert rows[0].slug == "ada"


def test_persona_get_by_id(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/personas/p1").mock(
        return_value=httpx.Response(200, json=envelope(_persona()))
    )
    p = registry.persona_get("p1")
    assert p.id == "p1"


def test_persona_get_falls_back_to_slug(
    mock_router: respx.MockRouter, registry: RegistryClient
) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/personas/ada").mock(
        return_value=httpx.Response(404, json={"error": "not found"})
    )
    mock_router.get(f"{REGISTRY_URL}/api/admin/personas/by-slug/ada").mock(
        return_value=httpx.Response(200, json=envelope(_persona()))
    )
    p = registry.persona_get("ada")
    assert p.slug == "ada"


def test_persona_create(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    route = mock_router.post(f"{REGISTRY_URL}/api/admin/personas").mock(
        return_value=httpx.Response(200, json=envelope(_persona()))
    )
    p = registry.persona_create({"slug": "ada", "name": "Ada", "modelPrompt": "..."})
    assert p.slug == "ada"
    body = json.loads(route.calls.last.request.read())
    assert body == {"slug": "ada", "name": "Ada", "modelPrompt": "..."}


def test_persona_update(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.put(f"{REGISTRY_URL}/api/admin/personas/p1").mock(
        return_value=httpx.Response(200, json=envelope(_persona(name="Ada Lovelace")))
    )
    p = registry.persona_update("p1", {"name": "Ada Lovelace"})
    assert p.name == "Ada Lovelace"


def test_persona_delete(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.delete(f"{REGISTRY_URL}/api/admin/personas/p1").mock(
        return_value=httpx.Response(204)
    )
    registry.persona_delete("p1")


def test_persona_unauthorized(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/personas").mock(
        return_value=httpx.Response(403, json={"error": "forbidden"})
    )
    with pytest.raises(AuthError):
        registry.persona_list()


def test_whoami_and_set_display_name(
    mock_router: respx.MockRouter, registry: RegistryClient
) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/auth/me").mock(
        return_value=httpx.Response(200, json=envelope({"id": "u1", "displayName": "old"}))
    )
    u = registry.whoami()
    assert u.id == "u1"

    mock_router.patch(f"{REGISTRY_URL}/api/auth/me").mock(
        return_value=httpx.Response(200, json=envelope({"id": "u1", "displayName": "new"}))
    )
    updated = registry.set_display_name("new")
    assert updated.displayName == "new"


def test_keys_list_create_revoke(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/keys").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "k1", "name": "ci"}]))
    )
    keys = registry.keys_list()
    assert keys[0].id == "k1"

    mock_router.post(f"{REGISTRY_URL}/api/keys").mock(
        return_value=httpx.Response(
            200, json=envelope({"key": {"id": "k2", "name": "ci"}, "rawKey": "secret"})
        )
    )
    created = registry.keys_create("ci")
    assert created.rawKey == "secret"

    mock_router.delete(f"{REGISTRY_URL}/api/keys/k2").mock(return_value=httpx.Response(204))
    registry.keys_revoke("k2")
