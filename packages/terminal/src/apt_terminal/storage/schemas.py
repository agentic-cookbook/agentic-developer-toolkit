from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class _Base(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class User(_Base):
    id: str
    githubLogin: str | None = None
    email: str | None = None
    displayName: str | None = None
    avatarUrl: str | None = None
    createdAt: datetime | None = None


class ApiKey(_Base):
    id: str
    keyPrefix: str | None = None
    name: str
    scopes: list[str] | None = None
    expiresAt: datetime | None = None
    createdAt: datetime | None = None


class ApiKeyCreated(_Base):
    key: ApiKey
    rawKey: str


class Bucket(_Base):
    id: str
    name: str
    description: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class ListResource(_Base):
    id: str
    name: str
    description: str | None = None
    createdAt: datetime | None = None


class ListItem(_Base):
    id: str
    listId: str
    position: int
    value: Any
    createdAt: datetime | None = None


class KvEntry(_Base):
    key: str
    value: Any
    updatedAt: datetime | None = None


class Counter(_Base):
    name: str
    value: str
    updatedAt: datetime | None = None


class Event(_Base):
    id: str
    bucketId: str
    streamName: str
    payload: Any
    occurredAt: datetime | None = None


class QueueResource(_Base):
    id: str
    bucketId: str
    name: str
    createdAt: datetime | None = None


class QueueMessage(_Base):
    id: str
    queueId: str
    payload: Any
    status: str
    attemptCount: int
    visibleAt: datetime | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class MemoryBlock(_Base):
    name: str
    content: str
    sizeLimit: int | None = None
    updatedAt: datetime | None = None


class Keyword(_Base):
    id: str
    bucketId: str
    name: str
    createdAt: datetime | None = None


class KeywordLink(_Base):
    id: str | None = None
    keywordId: str | None = None
    targetKind: str
    targetId: str
    createdAt: datetime | None = None
