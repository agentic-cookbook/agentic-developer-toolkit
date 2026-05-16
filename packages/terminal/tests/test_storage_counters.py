from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def _counter(value: int) -> dict[str, object]:
    return {"name": "hits", "value": str(value)}


def test_counter_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/counters").mock(
        return_value=httpx.Response(200, json=envelope([_counter(3)]))
    )
    rows = storage.counter_list("b1")
    assert rows[0].name == "hits"


def test_counter_get(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/counters/hits").mock(
        return_value=httpx.Response(200, json=envelope(_counter(3)))
    )
    c = storage.counter_get("b1", "hits")
    assert c.value == "3"


def test_counter_incr(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/counters/hits/incr").mock(
        return_value=httpx.Response(200, json=envelope(_counter(4)))
    )
    c = storage.counter_incr("b1", "hits", delta=1)
    assert c.value == "4"
    body = json.loads(route.calls.last.request.read())
    assert body == {"delta": 1}


def test_counter_set(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/counters/hits/set").mock(
        return_value=httpx.Response(200, json=envelope(_counter(10)))
    )
    c = storage.counter_set("b1", "hits", 10)
    assert c.value == "10"
    body = json.loads(route.calls.last.request.read())
    assert body == {"value": "10"}


def test_counter_reset(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/counters/hits").mock(
        return_value=httpx.Response(204)
    )
    storage.counter_reset("b1", "hits")
