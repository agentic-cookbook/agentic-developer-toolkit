from __future__ import annotations

from typing import Any

from apt_terminal.errors import NotFoundError
from apt_terminal.http import HttpClient
from apt_terminal.registry.schemas import (
    ApiKey,
    ApiKeyCreated,
    ModelInfo,
    Persona,
    PersonaService,
    ServerVersion,
    ServiceTemplate,
    User,
)


def _data(payload: Any) -> Any:
    if isinstance(payload, dict) and "data" in payload:
        return payload["data"]
    return payload


class RegistryClient:
    """Backend (authenticated) registry client."""

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

    # ---- personas (admin) --------------------------------------------
    def persona_list(self) -> list[Persona]:
        rows = _data(self.http.get("/api/admin/personas")) or []
        return [Persona.model_validate(r) for r in rows]

    def persona_get(self, ident: str) -> Persona:
        # Try as id first, fall back to slug.
        try:
            return Persona.model_validate(_data(self.http.get(f"/api/admin/personas/{ident}")))
        except NotFoundError:
            return Persona.model_validate(
                _data(self.http.get(f"/api/admin/personas/by-slug/{ident}"))
            )

    def persona_create(self, body: dict[str, Any]) -> Persona:
        return Persona.model_validate(_data(self.http.post("/api/admin/personas", json=body)))

    def persona_update(self, persona_id: str, body: dict[str, Any]) -> Persona:
        return Persona.model_validate(
            _data(self.http.put(f"/api/admin/personas/{persona_id}", json=body))
        )

    def persona_delete(self, persona_id: str) -> None:
        self.http.delete(f"/api/admin/personas/{persona_id}")

    # ---- persona services --------------------------------------------
    def service_list(self) -> list[PersonaService]:
        rows = _data(self.http.get("/api/admin/persona-services")) or []
        return [PersonaService.model_validate(r) for r in rows]

    def service_create(
        self,
        *,
        template_id: str,
        name: str,
        api_key: str,
        base_url: str | None = None,
    ) -> PersonaService:
        body: dict[str, Any] = {"templateId": template_id, "name": name, "apiKey": api_key}
        if base_url:
            body["baseUrl"] = base_url
        return PersonaService.model_validate(
            _data(self.http.post("/api/admin/persona-services", json=body))
        )

    def service_update(
        self,
        service_id: str,
        *,
        name: str | None = None,
        base_url: str | None = None,
        api_key: str | None = None,
    ) -> PersonaService:
        body: dict[str, Any] = {}
        if name is not None:
            body["name"] = name
        if base_url is not None:
            body["baseUrl"] = base_url
        if api_key is not None:
            body["apiKey"] = api_key
        return PersonaService.model_validate(
            _data(self.http.patch(f"/api/admin/persona-services/{service_id}", json=body))
        )

    def service_delete(self, service_id: str) -> None:
        self.http.delete(f"/api/admin/persona-services/{service_id}")

    def service_test(self, service_id: str) -> dict[str, Any]:
        result = self.http.post(f"/api/admin/persona-services/{service_id}/connect")
        out = _data(result)
        return out if isinstance(out, dict) else {"result": out}

    def service_models(self, service_id: str) -> list[ModelInfo]:
        rows = _data(self.http.get(f"/api/admin/persona-services/{service_id}/models")) or []
        return [ModelInfo.model_validate(r) for r in rows]

    def service_models_refresh(self, service_id: str) -> list[ModelInfo]:
        rows = (
            _data(self.http.post(f"/api/admin/persona-services/{service_id}/models/refresh")) or []
        )
        return [ModelInfo.model_validate(r) for r in rows]

    # ---- service templates -------------------------------------------
    def templates_list(self) -> list[ServiceTemplate]:
        rows = _data(self.http.get("/api/admin/persona-service-templates")) or []
        return [ServiceTemplate.model_validate(r) for r in rows]

    def template_models(self, template_id: str) -> list[ModelInfo]:
        rows = (
            _data(self.http.get(f"/api/admin/persona-service-templates/{template_id}/models")) or []
        )
        return [ModelInfo.model_validate(r) for r in rows]


class RegistryPublicClient:
    """Unauthenticated public-API client (api.agenticpersonaregistry.com)."""

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    def public_persona(self, slug: str) -> Persona:
        return Persona.model_validate(_data(self.http.get(f"/personas/{slug}")))

    def search(
        self,
        *,
        query: str | None = None,
        service: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if query:
            params["q"] = query
        if service:
            params["service"] = service
        if limit is not None:
            params["limit"] = limit
        if cursor:
            params["cursor"] = cursor
        result = self.http.get("/personas", params=params)
        return result if isinstance(result, dict) else {"data": result}

    def services(self) -> list[ServiceTemplate]:
        rows = _data(self.http.get("/services")) or []
        return [ServiceTemplate.model_validate(r) for r in rows]

    def version(self) -> ServerVersion:
        result = self.http.get("/version")
        body = _data(result)
        if not isinstance(body, dict):
            body = {"version": str(body)}
        return ServerVersion.model_validate(body)
