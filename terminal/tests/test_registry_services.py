from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.registry.client import RegistryClient
from tests.conftest import REGISTRY_URL, envelope


def test_service_list(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/persona-services").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "s1", "name": "openai-prod"}]))
    )
    rows = registry.service_list()
    assert rows[0].id == "s1"


def test_service_create(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    route = mock_router.post(f"{REGISTRY_URL}/api/admin/persona-services").mock(
        return_value=httpx.Response(200, json=envelope({"id": "s1", "name": "openai-prod"}))
    )
    s = registry.service_create(
        template_id="t1", name="openai-prod", api_key="sk-...", base_url="https://x"
    )
    assert s.id == "s1"
    body = json.loads(route.calls.last.request.read())
    assert body == {
        "templateId": "t1",
        "name": "openai-prod",
        "apiKey": "sk-...",
        "baseUrl": "https://x",
    }


def test_service_update(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.patch(f"{REGISTRY_URL}/api/admin/persona-services/s1").mock(
        return_value=httpx.Response(200, json=envelope({"id": "s1", "name": "renamed"}))
    )
    s = registry.service_update("s1", name="renamed")
    assert s.name == "renamed"


def test_service_delete(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.delete(f"{REGISTRY_URL}/api/admin/persona-services/s1").mock(
        return_value=httpx.Response(204)
    )
    registry.service_delete("s1")


def test_service_test(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.post(f"{REGISTRY_URL}/api/admin/persona-services/s1/connect").mock(
        return_value=httpx.Response(200, json=envelope({"ok": True}))
    )
    out = registry.service_test("s1")
    assert out == {"ok": True}


def test_service_models(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/persona-services/s1/models").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "gpt-4o", "name": "GPT-4o"}]))
    )
    rows = registry.service_models("s1")
    assert rows[0].id == "gpt-4o"


def test_service_models_refresh(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.post(f"{REGISTRY_URL}/api/admin/persona-services/s1/models/refresh").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "gpt-4o", "name": "GPT-4o"}]))
    )
    rows = registry.service_models_refresh("s1")
    assert rows[0].id == "gpt-4o"


def test_templates_list(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/persona-service-templates").mock(
        return_value=httpx.Response(
            200, json=envelope([{"id": "t1", "name": "OpenAI", "provider": "openai"}])
        )
    )
    rows = registry.templates_list()
    assert rows[0].provider == "openai"


def test_template_models(mock_router: respx.MockRouter, registry: RegistryClient) -> None:
    mock_router.get(f"{REGISTRY_URL}/api/admin/persona-service-templates/t1/models").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "gpt-4o", "name": "GPT-4o"}]))
    )
    rows = registry.template_models("t1")
    assert rows[0].id == "gpt-4o"
