from __future__ import annotations

import json

import httpx
import respx

from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def _keyword(**overrides: object) -> dict[str, object]:
    base: dict[str, object] = {"id": "kw1", "bucketId": "b1", "name": "tag-a"}
    base.update(overrides)
    return base


def test_keyword_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/keywords").mock(
        return_value=httpx.Response(200, json=envelope([_keyword()]))
    )
    rows = storage.keyword_list("b1")
    assert rows[0].name == "tag-a"


def test_keyword_tag(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets/b1/keywords/tag-a/links").mock(
        return_value=httpx.Response(
            200, json=envelope({"targetKind": "kv_entry", "targetId": "k1"})
        )
    )
    link = storage.keyword_tag("b1", "tag-a", target_kind="kv_entry", target_id="k1")
    assert link.targetId == "k1"
    body = json.loads(route.calls.last.request.read())
    assert body == {"targetKind": "kv_entry", "targetId": "k1"}


def test_keyword_untag(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.delete(f"{STORAGE_URL}/api/buckets/b1/keywords/tag-a/links").mock(
        return_value=httpx.Response(204)
    )
    storage.keyword_untag("b1", "tag-a", target_kind="kv_entry", target_id="k1")
    qs = route.calls.last.request.url.params
    assert qs["targetKind"] == "kv_entry"
    assert qs["targetId"] == "k1"


def test_keyword_items(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1/keywords/tag-a/items").mock(
        return_value=httpx.Response(
            200, json=envelope([{"targetKind": "kv_entry", "targetId": "k1"}])
        )
    )
    rows = storage.keyword_items("b1", "tag-a")
    assert rows[0].targetId == "k1"
