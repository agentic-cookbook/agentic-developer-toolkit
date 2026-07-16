from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_persona_services_body_provider_kind import PostPersonaServicesBodyProviderKind
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostPersonaServicesBody")



@_attrs_define
class PostPersonaServicesBody:
    """ 
        Attributes:
            name (str):
            provider_kind (PostPersonaServicesBodyProviderKind):
            base_url (str):
            template_id (Union[Unset, str]):
            api_key (Union[Unset, str]): Plaintext provider key; stored, never returned
     """

    name: str
    provider_kind: PostPersonaServicesBodyProviderKind
    base_url: str
    template_id: Union[Unset, str] = UNSET
    api_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_kind = self.provider_kind.value

        base_url = self.base_url

        template_id = self.template_id

        api_key = self.api_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "providerKind": provider_kind,
            "baseUrl": base_url,
        })
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        provider_kind = PostPersonaServicesBodyProviderKind(d.pop("providerKind"))




        base_url = d.pop("baseUrl")

        template_id = d.pop("templateId", UNSET)

        api_key = d.pop("apiKey", UNSET)

        post_persona_services_body = cls(
            name=name,
            provider_kind=provider_kind,
            base_url=base_url,
            template_id=template_id,
            api_key=api_key,
        )


        post_persona_services_body.additional_properties = d
        return post_persona_services_body

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
