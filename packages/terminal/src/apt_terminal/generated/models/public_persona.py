from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.public_persona_visibility import PublicPersonaVisibility
from typing import cast

if TYPE_CHECKING:
  from ..models.public_owner_type_0 import PublicOwnerType0





T = TypeVar("T", bound="PublicPersona")



@_attrs_define
class PublicPersona:
    """ 
        Attributes:
            slug (str):
            name (str):
            description (None | str):
            model_prompt (str):
            voice (None | str):
            character (None | str):
            examples (None | str):
            visibility (PublicPersonaVisibility):
            created_at (str):
            owner (None | PublicOwnerType0):
     """

    slug: str
    name: str
    description: None | str
    model_prompt: str
    voice: None | str
    character: None | str
    examples: None | str
    visibility: PublicPersonaVisibility
    created_at: str
    owner: None | PublicOwnerType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_owner_type_0 import PublicOwnerType0
        slug = self.slug

        name = self.name

        description: None | str
        description = self.description

        model_prompt = self.model_prompt

        voice: None | str
        voice = self.voice

        character: None | str
        character = self.character

        examples: None | str
        examples = self.examples

        visibility = self.visibility.value

        created_at = self.created_at

        owner: dict[str, Any] | None
        if isinstance(self.owner, PublicOwnerType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slug": slug,
            "name": name,
            "description": description,
            "modelPrompt": model_prompt,
            "voice": voice,
            "character": character,
            "examples": examples,
            "visibility": visibility,
            "createdAt": created_at,
            "owner": owner,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_owner_type_0 import PublicOwnerType0
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        model_prompt = d.pop("modelPrompt")

        def _parse_voice(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        voice = _parse_voice(d.pop("voice"))


        def _parse_character(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        character = _parse_character(d.pop("character"))


        def _parse_examples(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        examples = _parse_examples(d.pop("examples"))


        visibility = PublicPersonaVisibility(d.pop("visibility"))




        created_at = d.pop("createdAt")

        def _parse_owner(data: object) -> None | PublicOwnerType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_public_owner_type_0 = PublicOwnerType0.from_dict(data)



                return componentsschemas_public_owner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicOwnerType0, data)

        owner = _parse_owner(d.pop("owner"))


        public_persona = cls(
            slug=slug,
            name=name,
            description=description,
            model_prompt=model_prompt,
            voice=voice,
            character=character,
            examples=examples,
            visibility=visibility,
            created_at=created_at,
            owner=owner,
        )


        public_persona.additional_properties = d
        return public_persona

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
