from __future__ import annotations

from collections.abc import Iterator

import pytest
import respx

from apt_terminal.http import HttpClient
from apt_terminal.registry.client import RegistryClient, RegistryPublicClient
from apt_terminal.storage.client import StorageClient

STORAGE_URL = "https://api.test.storage"
REGISTRY_URL = "https://backend.test.registry"
REGISTRY_PUBLIC_URL = "https://api.test.registry"


@pytest.fixture
def mock_router() -> Iterator[respx.MockRouter]:
    with respx.mock(assert_all_called=False) as router:
        yield router


@pytest.fixture
def storage_http() -> Iterator[HttpClient]:
    http = HttpClient(STORAGE_URL, key="test-storage-key")
    try:
        yield http
    finally:
        http.close()


@pytest.fixture
def storage(storage_http: HttpClient) -> StorageClient:
    return StorageClient(storage_http)


@pytest.fixture
def registry_http() -> Iterator[HttpClient]:
    http = HttpClient(REGISTRY_URL, key="test-registry-key")
    try:
        yield http
    finally:
        http.close()


@pytest.fixture
def registry(registry_http: HttpClient) -> RegistryClient:
    return RegistryClient(registry_http)


@pytest.fixture
def registry_public_http() -> Iterator[HttpClient]:
    http = HttpClient(REGISTRY_PUBLIC_URL)
    try:
        yield http
    finally:
        http.close()


@pytest.fixture
def registry_public(registry_public_http: HttpClient) -> RegistryPublicClient:
    return RegistryPublicClient(registry_public_http)


def envelope(data: object) -> dict[str, object]:
    """Wrap a payload in the {"data": ...} envelope used by both APIs."""
    return {"data": data}
