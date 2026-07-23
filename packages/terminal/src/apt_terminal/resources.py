from __future__ import annotations

from dataclasses import dataclass
from types import ModuleType

# Generated operation modules (auth domain)
from apt_terminal.generated.api.auth import (
    delete_auth_tokens_id,
    get_auth_tokens,
    post_auth_tokens,
)

# Generated operation modules (persona domain)
from apt_terminal.generated.api.persona import (
    delete_persona_personas_id,
    delete_persona_services_id,
    get_persona_models,
    get_persona_personas,
    get_persona_personas_id,
    get_persona_provider_templates,
    get_persona_services,
    get_persona_services_id,
    get_persona_services_id_models,
    patch_persona_services_id,
    post_persona_personas,
    post_persona_services,
    post_persona_services_id_connect,
    post_persona_services_id_models_refresh,
    put_persona_personas_id,
)
from apt_terminal.generated.models.patch_persona_services_id_body import (
    PatchPersonaServicesIdBody,
)
from apt_terminal.generated.models.post_auth_tokens_body import PostAuthTokensBody
from apt_terminal.generated.models.post_persona_personas_body import (
    PostPersonaPersonasBody,
)
from apt_terminal.generated.models.post_persona_services_body import (
    PostPersonaServicesBody,
)
from apt_terminal.generated.models.put_persona_personas_id_body import (
    PutPersonaPersonasIdBody,
)


@dataclass(frozen=True)
class Ops:
    list_: ModuleType | None = None
    get: ModuleType | None = None
    create: ModuleType | None = None
    update: ModuleType | None = None
    delete: ModuleType | None = None


@dataclass(frozen=True)
class Action:
    name: str
    op: ModuleType
    help: str = ""


@dataclass(frozen=True)
class Resource:
    domain: str
    name: str
    ops: Ops
    create_body: type | None = None
    update_body: type | None = None
    actions: tuple[Action, ...] = ()


PERSONA: tuple[Resource, ...] = (
    Resource(
        domain="persona",
        name="services",
        ops=Ops(
            list_=get_persona_services,
            get=get_persona_services_id,
            create=post_persona_services,
            update=patch_persona_services_id,
            delete=delete_persona_services_id,
        ),
        create_body=PostPersonaServicesBody,
        update_body=PatchPersonaServicesIdBody,
        actions=(
            Action("connect", post_persona_services_id_connect, "Probe the provider connection"),
            Action("models", get_persona_services_id_models, "List the provider's models"),
            Action("models-refresh", post_persona_services_id_models_refresh, "Re-fetch the model catalog"),
        ),
    ),
    Resource(
        domain="persona",
        name="personas",
        ops=Ops(
            list_=get_persona_personas,
            get=get_persona_personas_id,
            create=post_persona_personas,
            update=put_persona_personas_id,
            delete=delete_persona_personas_id,
        ),
        create_body=PostPersonaPersonasBody,
        update_body=PutPersonaPersonasIdBody,
    ),
    Resource(
        domain="persona",
        name="models",
        ops=Ops(list_=get_persona_models),
    ),
    # `persona templates` now lists the redacting provider-templates catalog
    # (`get_persona_provider_templates`) because the raw service-templates
    # endpoint (`/persona/service-templates`) was removed from the backend.
    Resource(
        domain="persona",
        name="templates",
        ops=Ops(list_=get_persona_provider_templates),
    ),
)

AUTH_TOKENS: tuple[Resource, ...] = (
    Resource(
        domain="auth",
        name="tokens",
        ops=Ops(
            list_=get_auth_tokens,
            create=post_auth_tokens,
            delete=delete_auth_tokens_id,
        ),
        create_body=PostAuthTokensBody,
    ),
)

ALL_DOMAINS: dict[str, tuple[Resource, ...]] = {"persona": PERSONA}
