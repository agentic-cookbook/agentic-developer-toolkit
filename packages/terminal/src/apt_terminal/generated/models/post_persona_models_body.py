from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostPersonaModelsBody")



@_attrs_define
class PostPersonaModelsBody:
    """ 
        Attributes:
            template_id (str):
            name (str):
     """

    template_id: str
    name: str





    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "templateId": template_id,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("templateId")

        name = d.pop("name")

        post_persona_models_body = cls(
            template_id=template_id,
            name=name,
        )

        return post_persona_models_body

