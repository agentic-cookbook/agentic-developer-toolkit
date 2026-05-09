from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def test_kv_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/kv").mock(
        return_value=httpx.Response(200, json=envelope([{"key": "k1", "value": "v1"}]))
    )
    rows = storage.kv_list("b1")
    assert rows[0].key == "k1"


def test_kv_get(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/kv/k1").mock(
        return_value=httpx.Response(200, json=envelope({"key": "k1", "value": "v1"}))
    )
    entry = storage.kv_get("b1", "k1")
    assert entry.value == "v1"


def test_kv_set(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.put(f"{STORAGE_URL}/api/buckets/b1/kv/k1").mock(
        return_value=httpx.Response(200, json=envelope({"key": "k1", "value": {"a": 1}}))
    )
    entry = storage.kv_set("b1", "k1", {"a": 1})
    assert entry.value == {"a": 1}
    body = json.loads(route.calls.last.request.read())
    assert body == {"value": {"a": 1}}


def test_kv_delete(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/kv/k1").mock(return_value=httpx.Response(204))
    storage.kv_delete("b1", "k1")
