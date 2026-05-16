from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def test_memory_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/memory").mock(
        return_value=httpx.Response(200, json=envelope([{"name": "scratch", "content": "hello"}]))
    )
    rows = storage.memory_list("b1")
    assert rows[0].name == "scratch"


def test_memory_get(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/memory/scratch").mock(
        return_value=httpx.Response(200, json=envelope({"name": "scratch", "content": "hello"}))
    )
    m = storage.memory_get("b1", "scratch")
    assert m.content == "hello"


def test_memory_set(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.put(f"{STORAGE_URL}/api/buckets/b1/memory/scratch").mock(
        return_value=httpx.Response(200, json=envelope({"name": "scratch", "content": "world"}))
    )
    m = storage.memory_set("b1", "scratch", "world", size_limit=4096)
    assert m.content == "world"
    body = json.loads(route.calls.last.request.read())
    assert body == {"content": "world", "sizeLimit": 4096}


def test_memory_delete(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/memory/scratch").mock(
        return_value=httpx.Response(204)
    )
    storage.memory_delete("b1", "scratch")
