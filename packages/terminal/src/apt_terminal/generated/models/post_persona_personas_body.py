from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonaPersonasBody")



@_attrs_define
class PostPersonaPersonasBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            model (str):
            model_prompt (str):
            description (Union[None, Unset, str]):
            visibility (Union[Unset, str]):
            service_id (Union[None, Unset, str]):
            app_id (Union[None, Unset, str]):
            avatar_attachment_id (Union[None, Unset, str]):
            voice (Union[None, Unset, str]):
            character (Union[None, Unset, str]):
            examples (Union[None, Unset, str]):
            id (Union[Unset, str]):
     """

    slug: str
    name: str
    model: str
    model_prompt: str
    description: Union[None, Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    service_id: Union[None, Unset, str] = UNSET
    app_id: Union[None, Unset, str] = UNSET
    avatar_attachment_id: Union[None, Unset, str] = UNSET
    voice: Union[None, Unset, str] = UNSET
    character: Union[None, Unset, str] = UNSET
    examples: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        model = self.model

        model_prompt = self.model_prompt

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        visibility = self.visibility

        service_id: Union[None, Unset, str]
        if isinstance(self.service_id, Unset):
            service_id = UNSET
        else:
            service_id = self.service_id

        app_id: Union[None, Unset, str]
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        avatar_attachment_id: Union[None, Unset, str]
        if isinstance(self.avatar_attachment_id, Unset):
            avatar_attachment_id = UNSET
        else:
            avatar_attachment_id = self.avatar_attachment_id

        voice: Union[None, Unset, str]
        if isinstance(self.voice, Unset):
            voice = UNSET
        else:
            voice = self.voice

        character: Union[None, Unset, str]
        if isinstance(self.character, Unset):
            character = UNSET
        else:
            character = self.character

        examples: Union[None, Unset, str]
        if isinstance(self.examples, Unset):
            examples = UNSET
        else:
            examples = self.examples

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "name": name,
            "model": model,
            "modelPrompt": model_prompt,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if avatar_attachment_id is not UNSET:
            field_dict["avatarAttachmentId"] = avatar_attachment_id
        if voice is not UNSET:
            field_dict["voice"] = voice
        if character is not UNSET:
            field_dict["character"] = character
        if examples is not UNSET:
            field_dict["examples"] = examples
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        model = d.pop("model")

        model_prompt = d.pop("modelPrompt")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        visibility = d.pop("visibility", UNSET)

        def _parse_service_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_id = _parse_service_id(d.pop("serviceId", UNSET))


        def _parse_app_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_id = _parse_app_id(d.pop("appId", UNSET))


        def _parse_avatar_attachment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        avatar_attachment_id = _parse_avatar_attachment_id(d.pop("avatarAttachmentId", UNSET))


        def _parse_voice(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        voice = _parse_voice(d.pop("voice", UNSET))


        def _parse_character(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        character = _parse_character(d.pop("character", UNSET))


        def _parse_examples(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        examples = _parse_examples(d.pop("examples", UNSET))


        id = d.pop("id", UNSET)

        post_persona_personas_body = cls(
            slug=slug,
            name=name,
            model=model,
            model_prompt=model_prompt,
            description=description,
            visibility=visibility,
            service_id=service_id,
            app_id=app_id,
            avatar_attachment_id=avatar_attachment_id,
            voice=voice,
            character=character,
            examples=examples,
            id=id,
        )

        return post_persona_personas_body

