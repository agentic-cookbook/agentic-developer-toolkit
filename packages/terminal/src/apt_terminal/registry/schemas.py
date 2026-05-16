from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict


class _Base(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)


Visibility = Literal["public", "unlisted", "private"]


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


class Persona(_Base):
    id: str | None = None
    userId: str | None = None
    slug: str
    name: str
    description: str | None = None
    modelPrompt: str
    voice: str | None = None
    character: str | None = None
    examples: str | None = None
    serviceId: str | None = None
    model: str | None = None
    visibility: Visibility | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class PersonaService(_Base):
    id: str
    userId: str | None = None
    name: str
    templateId: str | None = None
    baseUrl: str | None = None
    status: str | None = None
    createdAt: datetime | None = None
    updatedAt: datetime | None = None


class ServiceTemplate(_Base):
    id: str
    name: str
    provider: str | None = None
    defaultBaseUrl: str | None = None


class ModelInfo(_Base):
    id: str
    name: str | None = None


class ServerVersion(_Base):
    version: str
    extra: dict[str, Any] | None = None
