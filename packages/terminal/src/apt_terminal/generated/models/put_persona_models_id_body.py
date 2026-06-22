from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutPersonaModelsIdBody")



@_attrs_define
class PutPersonaModelsIdBody:
    """ 
        Attributes:
            template_id (Union[Unset, str]):
            name (Union[Unset, str]):
     """

    template_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("templateId", UNSET)

        name = d.pop("name", UNSET)

        put_persona_models_id_body = cls(
            template_id=template_id,
            name=name,
        )

        return put_persona_models_id_body

