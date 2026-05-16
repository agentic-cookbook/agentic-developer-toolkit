from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def _item(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"id": "i1", "listId": "l1", "position": 0, "value": "x"}
    base.update(overrides)
    return base


def test_list_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/lists").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "l1", "name": "todo"}]))
    )
    rows = storage.list_list("b1")
    assert rows[0].name == "todo"


def test_list_create(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.post(f"{STORAGE_URL}/api/buckets/b1/lists").mock(
        return_value=httpx.Response(200, json=envelope({"id": "l1", "name": "todo"}))
    )
    lst = storage.list_create("b1", "todo", description="d")
    assert lst.id == "l1"


def test_list_delete(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/lists/todo").mock(
        return_value=httpx.Response(204)
    )
    storage.list_delete("b1", "todo")


def test_list_items(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/lists/todo/items").mock(
        return_value=httpx.Response(
            200,
            json=envelope([_item(id="i1", position=0), _item(id="i2", position=1)]),
        )
    )
    rows = storage.list_items("b1", "todo")
    assert [i.id for i in rows] == ["i1", "i2"]


def test_list_append(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/lists/todo/items").mock(
        return_value=httpx.Response(200, json=envelope(_item()))
    )
    item = storage.list_append("b1", "todo", "x", position=0)
    assert item.id == "i1"
    body = json.loads(route.calls.last.request.read())
    assert body == {"value": "x", "position": 0}


def test_list_remove_item(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/lists/todo/items/i1").mock(
        return_value=httpx.Response(204)
    )
    storage.list_remove_item("b1", "todo", "i1")
