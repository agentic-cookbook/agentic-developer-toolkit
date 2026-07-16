from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutPersonaPersonasIdResponse200")



@_attrs_define
class PutPersonaPersonasIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (Union[None, str]):
            owner_kind (str):
            owner_id (str):
            slug (str):
            name (str):
            description (Union[None, str]):
            visibility (str):
            model (str):
            service_id (Union[None, str]):
            app_id (Union[None, str]):
            avatar_attachment_id (Union[None, str]):
            model_prompt (str):
            voice (Union[None, str]):
            character (Union[None, str]):
            examples (Union[None, str]):
            created_at (str):
            updated_at (str):
            owned_ecosystem_id (Union[None, Unset, str]):
     """

    id: str
    user_id: Union[None, str]
    owner_kind: str
    owner_id: str
    slug: str
    name: str
    description: Union[None, str]
    visibility: str
    model: str
    service_id: Union[None, str]
    app_id: Union[None, str]
    avatar_attachment_id: Union[None, str]
    model_prompt: str
    voice: Union[None, str]
    character: Union[None, str]
    examples: Union[None, str]
    created_at: str
    updated_at: str
    owned_ecosystem_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id: Union[None, str]
        user_id = self.user_id

        owner_kind = self.owner_kind

        owner_id = self.owner_id

        slug = self.slug

        name = self.name

        description: Union[None, str]
        description = self.description

        visibility = self.visibility

        model = self.model

        service_id: Union[None, str]
        service_id = self.service_id

        app_id: Union[None, str]
        app_id = self.app_id

        avatar_attachment_id: Union[None, str]
        avatar_attachment_id = self.avatar_attachment_id

        model_prompt = self.model_prompt

        voice: Union[None, str]
        voice = self.voice

        character: Union[None, str]
        character = self.character

        examples: Union[None, str]
        examples = self.examples

        created_at = self.created_at

        updated_at = self.updated_at

        owned_ecosystem_id: Union[None, Unset, str]
        if isinstance(self.owned_ecosystem_id, Unset):
            owned_ecosystem_id = UNSET
        else:
            owned_ecosystem_id = self.owned_ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ownerKind": owner_kind,
            "ownerId": owner_id,
            "slug": slug,
            "name": name,
            "description": description,
            "visibility": visibility,
            "model": model,
            "serviceId": service_id,
            "appId": app_id,
            "avatarAttachmentId": avatar_attachment_id,
            "modelPrompt": model_prompt,
            "voice": voice,
            "character": character,
            "examples": examples,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if owned_ecosystem_id is not UNSET:
            field_dict["ownedEcosystemId"] = owned_ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_id = _parse_user_id(d.pop("userId"))


        owner_kind = d.pop("ownerKind")

        owner_id = d.pop("ownerId")

        slug = d.pop("slug")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))


        visibility = d.pop("visibility")

        model = d.pop("model")

        def _parse_service_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        service_id = _parse_service_id(d.pop("serviceId"))


        def _parse_app_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        app_id = _parse_app_id(d.pop("appId"))


        def _parse_avatar_attachment_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar_attachment_id = _parse_avatar_attachment_id(d.pop("avatarAttachmentId"))


        model_prompt = d.pop("modelPrompt")

        def _parse_voice(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        voice = _parse_voice(d.pop("voice"))


        def _parse_character(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        character = _parse_character(d.pop("character"))


        def _parse_examples(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        examples = _parse_examples(d.pop("examples"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_owned_ecosystem_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owned_ecosystem_id = _parse_owned_ecosystem_id(d.pop("ownedEcosystemId", UNSET))


        put_persona_personas_id_response_200 = cls(
            id=id,
            user_id=user_id,
            owner_kind=owner_kind,
            owner_id=owner_id,
            slug=slug,
            name=name,
            description=description,
            visibility=visibility,
            model=model,
            service_id=service_id,
            app_id=app_id,
            avatar_attachment_id=avatar_attachment_id,
            model_prompt=model_prompt,
            voice=voice,
            character=character,
            examples=examples,
            created_at=created_at,
            updated_at=updated_at,
            owned_ecosystem_id=owned_ecosystem_id,
        )

        return put_persona_personas_id_response_200

