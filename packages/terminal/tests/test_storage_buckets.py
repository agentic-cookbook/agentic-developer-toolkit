from __future__ import annotations

import json

import httpx
import pytest
import respx

from apt_terminal.errors import AuthError, NotFoundError
from apt_terminal.storage.client import StorageClient
from tests.conftest import STORAGE_URL, envelope


def test_bucket_list(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets").mock(
        return_value=httpx.Response(
            200,
            json=envelope([{"id": "b1", "name": "alpha"}, {"id": "b2", "name": "beta"}]),
        )
    )
    rows = storage.bucket_list()
    assert [b.id for b in rows] == ["b1", "b2"]
    assert rows[0].name == "alpha"


def test_bucket_create(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    route = mock_router.post(f"{STORAGE_URL}/api/buckets").mock(
        return_value=httpx.Response(
            200, json=envelope({"id": "b1", "name": "alpha", "description": "d"})
        )
    )
    b = storage.bucket_create("alpha", description="d")
    assert b.id == "b1"
    body = json.loads(route.calls.last.request.read())
    assert body == {"name": "alpha", "description": "d"}


def test_bucket_get(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/b1").mock(
        return_value=httpx.Response(200, json=envelope({"id": "b1", "name": "alpha"}))
    )
    b = storage.bucket_get("b1")
    assert b.name == "alpha"


def test_bucket_update(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.patch(f"{STORAGE_URL}/api/buckets/b1").mock(
        return_value=httpx.Response(200, json=envelope({"id": "b1", "name": "renamed"}))
    )
    b = storage.bucket_update("b1", name="renamed")
    assert b.name == "renamed"


def test_bucket_delete(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.delete(f"{STORAGE_URL}/api/buckets/b1").mock(return_value=httpx.Response(204))
    storage.bucket_delete("b1")


def test_resolve_bucket_by_name_falls_back_to_list(
    mock_router: respx.MockRouter, storage: StorageClient
) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/alpha").mock(
        return_value=httpx.Response(404, json={"error": "not found"})
    )
    mock_router.get(f"{STORAGE_URL}/api/buckets").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "b1", "name": "alpha"}]))
    )
    b = storage.resolve_bucket("alpha")
    assert b.id == "b1"


def test_resolve_bucket_missing_raises(
    mock_router: respx.MockRouter, storage: StorageClient
) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets/ghost").mock(
        return_value=httpx.Response(404, json={"error": "nope"})
    )
    mock_router.get(f"{STORAGE_URL}/api/buckets").mock(
        return_value=httpx.Response(200, json=envelope([]))
    )
    with pytest.raises(NotFoundError):
        storage.resolve_bucket("ghost")


def test_unauthorized_maps_to_auth_error(
    mock_router: respx.MockRouter, storage: StorageClient
) -> None:
    mock_router.get(f"{STORAGE_URL}/api/buckets").mock(
        return_value=httpx.Response(401, json={"error": "bad token"})
    )
    with pytest.raises(AuthError):
        storage.bucket_list()


def test_whoami(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/auth/me").mock(
        return_value=httpx.Response(200, json=envelope({"id": "u1", "email": "u@example"}))
    )
    u = storage.whoami()
    assert u.id == "u1"


def test_keys_list_create_revoke(mock_router: respx.MockRouter, storage: StorageClient) -> None:
    mock_router.get(f"{STORAGE_URL}/api/keys").mock(
        return_value=httpx.Response(200, json=envelope([{"id": "k1", "name": "ci"}]))
    )
    keys = storage.keys_list()
    assert keys[0].id == "k1"

    mock_router.post(f"{STORAGE_URL}/api/keys").mock(
        return_value=httpx.Response(
            200,
            json=envelope({"key": {"id": "k2", "name": "ci"}, "rawKey": "raw-secret"}),
        )
    )
    created = storage.keys_create("ci", scopes=["read"])
    assert created.rawKey == "raw-secret"
    assert created.key.id == "k2"

    mock_router.delete(f"{STORAGE_URL}/api/keys/k2").mock(return_value=httpx.Response(204))
    storage.keys_revoke("k2")
