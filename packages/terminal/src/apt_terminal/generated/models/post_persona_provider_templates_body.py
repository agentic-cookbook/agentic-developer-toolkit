from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_persona_provider_templates_body_provider_kind import PostPersonaProviderTemplatesBodyProviderKind
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonaProviderTemplatesBody")



@_attrs_define
class PostPersonaProviderTemplatesBody:
    """ 
        Attributes:
            provider_kind (PostPersonaProviderTemplatesBodyProviderKind):
            name (str):
            base_url (str):
            documentation_url (Union[None, Unset, str]):
            status_url (Union[None, Unset, str]):
            models (Union[Unset, list[str]]): Model names. On create: the initial model list. On update: the FULL desired
                set (matching rows kept, missing inserted, absent deleted); omit to leave models unchanged.
     """

    provider_kind: PostPersonaProviderTemplatesBodyProviderKind
    name: str
    base_url: str
    documentation_url: Union[None, Unset, str] = UNSET
    status_url: Union[None, Unset, str] = UNSET
    models: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider_kind = self.provider_kind.value

        name = self.name

        base_url = self.base_url

        documentation_url: Union[None, Unset, str]
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        status_url: Union[None, Unset, str]
        if isinstance(self.status_url, Unset):
            status_url = UNSET
        else:
            status_url = self.status_url

        models: Union[Unset, list[str]] = UNSET
        if not isinstance(self.models, Unset):
            models = self.models




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "providerKind": provider_kind,
            "name": name,
            "baseUrl": base_url,
        })
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if status_url is not UNSET:
            field_dict["statusUrl"] = status_url
        if models is not UNSET:
            field_dict["models"] = models

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_kind = PostPersonaProviderTemplatesBodyProviderKind(d.pop("providerKind"))




        name = d.pop("name")

        base_url = d.pop("baseUrl")

        def _parse_documentation_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl", UNSET))


        def _parse_status_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_url = _parse_status_url(d.pop("statusUrl", UNSET))


        models = cast(list[str], d.pop("models", UNSET))


        post_persona_provider_templates_body = cls(
            provider_kind=provider_kind,
            name=name,
            base_url=base_url,
            documentation_url=documentation_url,
            status_url=status_url,
            models=models,
        )


        post_persona_provider_templates_body.additional_properties = d
        return post_persona_provider_templates_body

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
