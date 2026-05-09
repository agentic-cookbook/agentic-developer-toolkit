from __future__ import annotations

from typing import Any

from apt_terminal.errors import NotFoundError
from apt_terminal.http import HttpClient
from apt_terminal.storage.schemas import (
    ApiKey,
    ApiKeyCreated,
    Bucket,
    Counter,
    Event,
    Keyword,
    KeywordLink,
    KvEntry,
    ListItem,
    ListResource,
    MemoryBlock,
    QueueMessage,
    QueueResource,
    User,
)


def _data(payload: Any) -> Any:
    if isinstance(payload, dict) and "data" in payload:
        return payload["data"]
    return payload


class StorageClient:
    def __init__(self, http: HttpClient) -> None:
        self.http = http

    # ---- auth / keys --------------------------------------------------
    def whoami(self) -> User:
        return User.model_validate(_data(self.http.get("/api/auth/me")))

    def set_display_name(self, name: str) -> User:
        return User.model_validate(
            _data(self.http.patch("/api/auth/me", json={"displayName": name}))
        )

    def keys_list(self) -> list[ApiKey]:
        rows = _data(self.http.get("/api/keys")) or []
        return [ApiKey.model_validate(r) for r in rows]

    def keys_create(
        self, name: str, *, scopes: list[str] | None = None, expires_at: str | None = None
    ) -> ApiKeyCreated:
        body: dict[str, Any] = {"name": name}
        if scopes:
            body["scopes"] = scopes
        if expires_at:
            body["expiresAt"] = expires_at
        return ApiKeyCreated.model_validate(_data(self.http.post("/api/keys", json=body)))

    def keys_revoke(self, key_id: str) -> None:
        self.http.delete(f"/api/keys/{key_id}")

    # ---- buckets ------------------------------------------------------
    def bucket_list(self) -> list[Bucket]:
        rows = _data(self.http.get("/api/buckets")) or []
        return [Bucket.model_validate(r) for r in rows]

    def bucket_create(self, name: str, *, description: str | None = None) -> Bucket:
        body: dict[str, Any] = {"name": name}
        if description is not None:
            body["description"] = description
        return Bucket.model_validate(_data(self.http.post("/api/buckets", json=body)))

    def bucket_get(self, bucket_id: str) -> Bucket:
        return Bucket.model_validate(_data(self.http.get(f"/api/buckets/{bucket_id}")))

    def bucket_update(
        self, bucket_id: str, *, name: str | None = None, description: str | None = None
    ) -> Bucket:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        return Bucket.model_validate(_data(self.http.patch(f"/api/buckets/{bucket_id}", json=body)))

    def bucket_delete(self, bucket_id: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}")

    def resolve_bucket(self, name_or_id: str) -> Bucket:
        """Look up a bucket by either name or id."""
        # Try as id first (cheap if it is one).
        try:
            return self.bucket_get(name_or_id)
        except NotFoundError:
            pass
        for b in self.bucket_list():
            if b.name == name_or_id:
                return b
        raise NotFoundError(f"bucket not found: {name_or_id}")

    # ---- lists --------------------------------------------------------
    def list_list(self, bucket_id: str) -> list[ListResource]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/lists")) or []
        return [ListResource.model_validate(r) for r in rows]

    def list_create(
        self, bucket_id: str, name: str, *, description: str | None = None
    ) -> ListResource:
        body: dict[str, Any] = {"name": name}
        if description is not None:
            body["description"] = description
        return ListResource.model_validate(
            _data(self.http.post(f"/api/buckets/{bucket_id}/lists", json=body))
        )

    def list_delete(self, bucket_id: str, name: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}/lists/{name}")

    def list_items(self, bucket_id: str, name: str) -> list[ListItem]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/lists/{name}/items")) or []
        return [ListItem.model_validate(r) for r in rows]

    def list_append(
        self, bucket_id: str, name: str, value: Any, *, position: int | None = None
    ) -> ListItem:
        body: dict[str, Any] = {"value": value}
        if position is not None:
            body["position"] = position
        return ListItem.model_validate(
            _data(self.http.post(f"/api/buckets/{bucket_id}/lists/{name}/items", json=body))
        )

    def list_remove_item(self, bucket_id: str, name: str, item_id: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}/lists/{name}/items/{item_id}")

    # ---- kv -----------------------------------------------------------
    def kv_list(self, bucket_id: str) -> list[KvEntry]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/kv")) or []
        return [KvEntry.model_validate(r) for r in rows]

    def kv_get(self, bucket_id: str, key: str) -> KvEntry:
        return KvEntry.model_validate(_data(self.http.get(f"/api/buckets/{bucket_id}/kv/{key}")))

    def kv_set(self, bucket_id: str, key: str, value: Any) -> KvEntry:
        return KvEntry.model_validate(
            _data(self.http.put(f"/api/buckets/{bucket_id}/kv/{key}", json={"value": value}))
        )

    def kv_delete(self, bucket_id: str, key: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}/kv/{key}")

    # ---- counters -----------------------------------------------------
    def counter_list(self, bucket_id: str) -> list[Counter]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/counters")) or []
        return [Counter.model_validate(r) for r in rows]

    def counter_get(self, bucket_id: str, name: str) -> Counter:
        return Counter.model_validate(
            _data(self.http.get(f"/api/buckets/{bucket_id}/counters/{name}"))
        )

    def counter_incr(self, bucket_id: str, name: str, *, delta: int = 1) -> Counter:
        return Counter.model_validate(
            _data(
                self.http.post(
                    f"/api/buckets/{bucket_id}/counters/{name}/incr", json={"delta": delta}
                )
            )
        )

    def counter_set(self, bucket_id: str, name: str, value: int) -> Counter:
        return Counter.model_validate(
            _data(
                self.http.post(
                    f"/api/buckets/{bucket_id}/counters/{name}/set", json={"value": str(value)}
                )
            )
        )

    def counter_reset(self, bucket_id: str, name: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}/counters/{name}")

    # ---- events -------------------------------------------------------
    def event_log(
        self,
        bucket_id: str,
        payload: Any,
        *,
        stream: str | None = None,
        occurred_at: str | None = None,
    ) -> Event:
        body: dict[str, Any] = {"payload": payload}
        if stream:
            body["stream"] = stream
        if occurred_at:
            body["occurredAt"] = occurred_at
        return Event.model_validate(
            _data(self.http.post(f"/api/buckets/{bucket_id}/events", json=body))
        )

    def event_query(
        self,
        bucket_id: str,
        *,
        stream: str | None = None,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
    ) -> list[Event]:
        params: dict[str, Any] = {}
        if stream:
            params["stream"] = stream
        if since:
            params["since"] = since
        if until:
            params["until"] = until
        if limit is not None:
            params["limit"] = limit
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/events", params=params)) or []
        return [Event.model_validate(r) for r in rows]

    # ---- queues -------------------------------------------------------
    def queue_list(self, bucket_id: str) -> list[QueueResource]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/queues")) or []
        return [QueueResource.model_validate(r) for r in rows]

    def queue_push(
        self, bucket_id: str, name: str, payload: Any, *, visible_at: str | None = None
    ) -> QueueMessage:
        body: dict[str, Any] = {"payload": payload}
        if visible_at:
            body["visibleAt"] = visible_at
        return QueueMessage.model_validate(
            _data(self.http.post(f"/api/buckets/{bucket_id}/queues/{name}/enqueue", json=body))
        )

    def queue_pop(
        self, bucket_id: str, name: str, *, visibility_timeout_sec: int | None = None
    ) -> QueueMessage | None:
        body: dict[str, Any] = {}
        if visibility_timeout_sec is not None:
            body["visibilityTimeoutSec"] = visibility_timeout_sec
        result = _data(self.http.post(f"/api/buckets/{bucket_id}/queues/{name}/dequeue", json=body))
        if not result:
            return None
        return QueueMessage.model_validate(result)

    def queue_ack(self, bucket_id: str, name: str, message_id: str) -> None:
        self.http.post(f"/api/buckets/{bucket_id}/queues/{name}/ack/{message_id}")

    def queue_nack(
        self,
        bucket_id: str,
        name: str,
        message_id: str,
        *,
        delay_sec: int | None = None,
        dead: bool = False,
    ) -> None:
        body: dict[str, Any] = {}
        if delay_sec is not None:
            body["delaySec"] = delay_sec
        if dead:
            body["dead"] = True
        self.http.post(
            f"/api/buckets/{bucket_id}/queues/{name}/nack/{message_id}", json=body or None
        )

    # ---- memory -------------------------------------------------------
    def memory_list(self, bucket_id: str) -> list[MemoryBlock]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/memory")) or []
        return [MemoryBlock.model_validate(r) for r in rows]

    def memory_get(self, bucket_id: str, name: str) -> MemoryBlock:
        return MemoryBlock.model_validate(
            _data(self.http.get(f"/api/buckets/{bucket_id}/memory/{name}"))
        )

    def memory_set(
        self, bucket_id: str, name: str, content: str, *, size_limit: int | None = None
    ) -> MemoryBlock:
        body: dict[str, Any] = {"content": content}
        if size_limit is not None:
            body["sizeLimit"] = size_limit
        return MemoryBlock.model_validate(
            _data(self.http.put(f"/api/buckets/{bucket_id}/memory/{name}", json=body))
        )

    def memory_delete(self, bucket_id: str, name: str) -> None:
        self.http.delete(f"/api/buckets/{bucket_id}/memory/{name}")

    # ---- keywords -----------------------------------------------------
    def keyword_list(self, bucket_id: str) -> list[Keyword]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/keywords")) or []
        return [Keyword.model_validate(r) for r in rows]

    def keyword_tag(
        self, bucket_id: str, keyword: str, *, target_kind: str, target_id: str
    ) -> KeywordLink:
        return KeywordLink.model_validate(
            _data(
                self.http.post(
                    f"/api/buckets/{bucket_id}/keywords/{keyword}/links",
                    json={"targetKind": target_kind, "targetId": target_id},
                )
            )
        )

    def keyword_untag(
        self, bucket_id: str, keyword: str, *, target_kind: str, target_id: str
    ) -> None:
        self.http.request(
            "DELETE",
            f"/api/buckets/{bucket_id}/keywords/{keyword}/links",
            params={"targetKind": target_kind, "targetId": target_id},
        )

    def keyword_items(self, bucket_id: str, keyword: str) -> list[KeywordLink]:
        rows = _data(self.http.get(f"/api/buckets/{bucket_id}/keywords/{keyword}/items")) or []
        return [KeywordLink.model_validate(r) for r in rows]
