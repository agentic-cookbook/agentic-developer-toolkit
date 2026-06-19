from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonaPersonasIdBody")



@_attrs_define
class PutPersonaPersonasIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            slug (str | Unset):
            name (str | Unset):
            description (None | str | Unset):
            visibility (str | Unset):
            model (str | Unset):
            service_id (None | str | Unset):
            app_id (None | str | Unset):
            model_prompt (str | Unset):
            voice (None | str | Unset):
            character (None | str | Unset):
            examples (None | str | Unset):
     """

    owner_id: str | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    visibility: str | Unset = UNSET
    model: str | Unset = UNSET
    service_id: None | str | Unset = UNSET
    app_id: None | str | Unset = UNSET
    model_prompt: str | Unset = UNSET
    voice: None | str | Unset = UNSET
    character: None | str | Unset = UNSET
    examples: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        slug = self.slug

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        visibility = self.visibility

        model = self.model

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

        model_prompt = self.model_prompt

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


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if model is not UNSET:
            field_dict["model"] = model
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if model_prompt is not UNSET:
            field_dict["modelPrompt"] = model_prompt
        if voice is not UNSET:
            field_dict["voice"] = voice
        if character is not UNSET:
            field_dict["character"] = character
        if examples is not UNSET:
            field_dict["examples"] = examples

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        visibility = d.pop("visibility", UNSET)

        model = d.pop("model", UNSET)

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


        model_prompt = d.pop("modelPrompt", UNSET)

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


        put_persona_personas_id_body = cls(
            owner_id=owner_id,
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
        )

        return put_persona_personas_id_body

