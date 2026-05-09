from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def _queue(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"id": "q1", "bucketId": "b1", "name": "jobs"}
    base.update(overrides)
    return base


def _msg(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {
        "id": "m1",
        "queueId": "q1",
        "payload": {"x": 1},
        "status": "pending",
        "attemptCount": 0,
    }
    base.update(overrides)
    return base


def test_queue_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/queues").mock(
        return_value=httpx.Response(200, json=envelope([_queue()]))
    )
    rows = storage.queue_list("b1")
    assert rows[0].name == "jobs"


def test_queue_push(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/queues/jobs/enqueue").mock(
        return_value=httpx.Response(200, json=envelope(_msg()))
    )
    msg = storage.queue_push("b1", "jobs", {"x": 1})
    assert msg.id == "m1"
    body = json.loads(route.calls.last.request.read())
    assert body == {"payload": {"x": 1}}


def test_queue_pop_returns_message(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.post(f"{STORAGE_URL}/api/buckets/b1/queues/jobs/dequeue").mock(
        return_value=httpx.Response(200, json=envelope(_msg()))
    )
    msg = storage.queue_pop("b1", "jobs", visibility_timeout_sec=30)
    assert msg is not None
    assert msg.id == "m1"


def test_queue_pop_empty_returns_none(
    mock_router: respx.MockRouter, storage: StorageClient
) -> None:
    mock_router.post(f"{STORAGE_URL}/api/buckets/b1/queues/jobs/dequeue").mock(
        return_value=httpx.Response(200, json=envelope(None))
    )
    msg = storage.queue_pop("b1", "jobs")
    assert msg is None


def test_queue_ack(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.post(f"{STORAGE_URL}/api/buckets/b1/queues/jobs/ack/m1").mock(
        return_value=httpx.Response(204)
    )
    storage.queue_ack("b1", "jobs", "m1")


def test_queue_nack_with_dead(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/queues/jobs/nack/m1").mock(
        return_value=httpx.Response(204)
    )
    storage.queue_nack("b1", "jobs", "m1", dead=True)
    body = json.loads(route.calls.last.request.read())
    assert body == {"dead": True}
