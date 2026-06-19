from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostPersonaPersonasBody")



@_attrs_define
class PostPersonaPersonasBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            model (str):
            model_prompt (str):
            owner_id (str | Unset):
            description (None | str | Unset):
            visibility (str | Unset):
            service_id (None | str | Unset):
            app_id (None | str | Unset):
            voice (None | str | Unset):
            character (None | str | Unset):
            examples (None | str | Unset):
            id (str | Unset):
     """

    slug: str
    name: str
    model: str
    model_prompt: str
    owner_id: str | Unset = UNSET
    description: None | str | Unset = UNSET
    visibility: str | Unset = UNSET
    service_id: None | str | Unset = UNSET
    app_id: None | str | Unset = UNSET
    voice: None | str | Unset = UNSET
    character: None | str | Unset = UNSET
    examples: None | str | Unset = UNSET
    id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        model = self.model

        model_prompt = self.model_prompt

        owner_id = self.owner_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        visibility = self.visibility

        service_id: None | str | Unset
        if isinstance(self.service_id, Unset):
            service_id = UNSET
        else:
            service_id = self.service_id

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        voice: None | str | Unset
        if isinstance(self.voice, Unset):
            voice = UNSET
        else:
            voice = self.voice

        character: None | str | Unset
        if isinstance(self.character, Unset):
            character = UNSET
        else:
            character = self.character

        examples: None | str | Unset
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
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
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

        owner_id = d.pop("ownerId", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        visibility = d.pop("visibility", UNSET)

        def _parse_service_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_id = _parse_service_id(d.pop("serviceId", UNSET))


        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("appId", UNSET))


        def _parse_voice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice = _parse_voice(d.pop("voice", UNSET))


        def _parse_character(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        character = _parse_character(d.pop("character", UNSET))


        def _parse_examples(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        examples = _parse_examples(d.pop("examples", UNSET))


        id = d.pop("id", UNSET)

        post_persona_personas_body = cls(
            slug=slug,
            name=name,
            model=model,
            model_prompt=model_prompt,
            owner_id=owner_id,
            description=description,
            visibility=visibility,
            service_id=service_id,
            app_id=app_id,
            voice=voice,
            character=character,
            examples=examples,
            id=id,
        )

        return post_persona_personas_body

