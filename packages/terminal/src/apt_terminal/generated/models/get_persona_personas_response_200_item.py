from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetPersonaPersonasResponse200Item")



@_attrs_define
class GetPersonaPersonasResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            user_id (Union[None, str]):
            slug (str):
            name (str):
            description (Union[None, str]):
            visibility (str):
            model (str):
            service_id (Union[None, str]):
            app_id (Union[None, str]):
            model_prompt (str):
            voice (Union[None, str]):
            character (Union[None, str]):
            examples (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    user_id: Union[None, str]
    slug: str
    name: str
    description: Union[None, str]
    visibility: str
    model: str
    service_id: Union[None, str]
    app_id: Union[None, str]
    model_prompt: str
    voice: Union[None, str]
    character: Union[None, str]
    examples: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        user_id: Union[None, str]
        user_id = self.user_id

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

        model_prompt = self.model_prompt

        voice: Union[None, str]
        voice = self.voice

        character: Union[None, str]
        character = self.character

        examples: Union[None, str]
        examples = self.examples

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "userId": user_id,
            "slug": slug,
            "name": name,
            "description": description,
            "visibility": visibility,
            "model": model,
            "serviceId": service_id,
            "appId": app_id,
            "modelPrompt": model_prompt,
            "voice": voice,
            "character": character,
            "examples": examples,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        def _parse_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_id = _parse_user_id(d.pop("userId"))


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

        get_persona_personas_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            user_id=user_id,
            slug=slug,
            name=name,
            description=description,
            visibility=visibility,
            model=model,
            service_id=service_id,
            app_id=app_id,
            model_prompt=model_prompt,
            voice=voice,
            character=character,
            examples=examples,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_persona_personas_response_200_item

