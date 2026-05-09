from __future__ import annotations

import httpx
import respx

from apt_terminal.registry.client import RegistryPublicClient
from tests.conftest import REGISTRY_PUBLIC_URL, envelope


def test_public_persona(
    mock_router: respx.MockRouter, registry_public: RegistryPublicClient
) -> None:
    mock_router.get(f"{REGISTRY_PUBLIC_URL}/personas/ada").mock(
        return_value=httpx.Response(
            200,
            json=envelope({"slug": "ada", "name": "Ada", "modelPrompt": "..."}),
        )
    )
    p = registry_public.public_persona("ada")
    assert p.slug == "ada"


def test_search_with_params(
    mock_router: respx.MockRouter, registry_public: RegistryPublicClient
) -> None:
    route = mock_router.get(f"{REGISTRY_PUBLIC_URL}/personas").mock(
        return_value=httpx.Response(
            200,
            json={"data": [{"slug": "ada", "name": "Ada", "modelPrompt": "..."}], "next": None},
        )
    )
    out = registry_public.search(query="ada", service="openai", limit=5)
    assert isinstance(out, dict)
    qs = route.calls.last.request.url.params
    assert qs["q"] == "ada"
    assert qs["service"] == "openai"
    assert qs["limit"] == "5"


def test_search_wraps_bare_list(
    mock_router: respx.MockRouter, registry_public: RegistryPublicClient
) -> None:
    mock_router.get(f"{REGISTRY_PUBLIC_URL}/personas").mock(
        return_value=httpx.Response(
            200, json=[{"slug": "ada", "name": "Ada", "modelPrompt": "..."}]
        )
    )
    out = registry_public.search()
    assert "data" in out


def test_services(mock_router: respx.MockRouter, registry_public: RegistryPublicClient) -> None:
    mock_router.get(f"{REGISTRY_PUBLIC_URL}/services").mock(
        return_value=httpx.Response(
            200, json=envelope([{"id": "t1", "name": "OpenAI", "provider": "openai"}])
        )
    )
    rows = registry_public.services()
    assert rows[0].id == "t1"


def test_version_dict(mock_router: respx.MockRouter, registry_public: RegistryPublicClient) -> None:
    mock_router.get(f"{REGISTRY_PUBLIC_URL}/version").mock(
        return_value=httpx.Response(200, json=envelope({"version": "1.2.3"}))
    )
    v = registry_public.version()
    assert v.version == "1.2.3"


def test_version_string_payload(
    mock_router: respx.MockRouter, registry_public: RegistryPublicClient
) -> None:
    mock_router.get(f"{REGISTRY_PUBLIC_URL}/version").mock(
        return_value=httpx.Response(200, json={"data": "1.2.3"})
    )
    v = registry_public.version()
    assert v.version == "1.2.3"
