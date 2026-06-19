from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PatchPersonaServicesIdBody")



@_attrs_define
class PatchPersonaServicesIdBody:
    """ 
        Attributes:
            name (str | Unset):
            base_url (str | Unset):
            api_key (str | Unset): Plaintext provider key; stored, never returned
     """

    name: str | Unset = UNSET
    base_url: str | Unset = UNSET
    api_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        base_url = self.base_url

        api_key = self.api_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        api_key = d.pop("apiKey", UNSET)

        patch_persona_services_id_body = cls(
            name=name,
            base_url=base_url,
            api_key=api_key,
        )


        patch_persona_services_id_body.additional_properties = d
        return patch_persona_services_id_body

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
