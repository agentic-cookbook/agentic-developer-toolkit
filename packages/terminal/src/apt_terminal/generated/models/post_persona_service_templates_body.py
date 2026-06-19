from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostPersonaServiceTemplatesBody")



@_attrs_define
class PostPersonaServiceTemplatesBody:
    """ 
        Attributes:
            provider_kind (str):
            name (str):
            base_url (str):
            documentation_url (None | str | Unset):
            status_url (None | str | Unset):
     """

    provider_kind: str
    name: str
    base_url: str
    documentation_url: None | str | Unset = UNSET
    status_url: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        provider_kind = self.provider_kind

        name = self.name

        base_url = self.base_url

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        status_url: None | str | Unset
        if isinstance(self.status_url, Unset):
            status_url = UNSET
        else:
            status_url = self.status_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "providerKind": provider_kind,
            "name": name,
            "baseUrl": base_url,
        })
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if status_url is not UNSET:
            field_dict["statusUrl"] = status_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_kind = d.pop("providerKind")

        name = d.pop("name")

        base_url = d.pop("baseUrl")

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl", UNSET))


        def _parse_status_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_url = _parse_status_url(d.pop("statusUrl", UNSET))


        post_persona_service_templates_body = cls(
            provider_kind=provider_kind,
            name=name,
            base_url=base_url,
            documentation_url=documentation_url,
            status_url=status_url,
        )

        return post_persona_service_templates_body

