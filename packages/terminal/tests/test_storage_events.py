from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def _event(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "e1",
        "bucketId": "b1",
        "streamName": "s1",
        "payload": {"x": 1},
    }
    base.update(overrides)
    return base


def test_event_log(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/events").mock(
        return_value=httpx.Response(200, json=envelope(_event()))
    )
    e = storage.event_log("b1", {"x": 1}, stream="s1")
    assert e.id == "e1"
    body = json.loads(route.calls.last.request.read())
    assert body == {"payload": {"x": 1}, "stream": "s1"}


def test_event_query_with_filters(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.get(f"{STORAGE_URL}/api/buckets/b1/events").mock(
        return_value=httpx.Response(200, json=envelope([_event()]))
    )
    rows = storage.event_query("b1", stream="s1", limit=10)
    assert rows[0].id == "e1"
    qs = route.calls.last.request.url.params
    assert qs["stream"] == "s1"
    assert qs["limit"] == "10"


def test_event_query_no_results(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/events").mock(
        return_value=httpx.Response(200, json=envelope([]))
    )
    rows = storage.event_query("b1")
    assert rows == []
