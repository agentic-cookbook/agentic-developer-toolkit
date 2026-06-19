from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetPersonaModelsIdResponse200")



@_attrs_define
class GetPersonaModelsIdResponse200:
    """ 
        Attributes:
            id (str):
            template_id (str):
            name (str):
            created_at (str):
     """

    id: str
    template_id: str
    name: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        name = self.name

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "templateId": template_id,
            "name": name,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("templateId")

        name = d.pop("name")

        created_at = d.pop("createdAt")

        get_persona_models_id_response_200 = cls(
            id=id,
            template_id=template_id,
            name=name,
            created_at=created_at,
        )

        return get_persona_models_id_response_200

