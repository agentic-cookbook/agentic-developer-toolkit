from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostPersonaServiceTemplatesResponse201")



@_attrs_define
class PostPersonaServiceTemplatesResponse201:
    """ 
        Attributes:
            id (str):
            provider_kind (str):
            name (str):
            base_url (str):
            documentation_url (Union[None, str]):
            status_url (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    provider_kind: str
    name: str
    base_url: str
    documentation_url: Union[None, str]
    status_url: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_kind = self.provider_kind

        name = self.name

        base_url = self.base_url

        documentation_url: Union[None, str]
        documentation_url = self.documentation_url

        status_url: Union[None, str]
        status_url = self.status_url

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "providerKind": provider_kind,
            "name": name,
            "baseUrl": base_url,
            "documentationUrl": documentation_url,
            "statusUrl": status_url,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        provider_kind = d.pop("providerKind")

        name = d.pop("name")

        base_url = d.pop("baseUrl")

        def _parse_documentation_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl"))


        def _parse_status_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_url = _parse_status_url(d.pop("statusUrl"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_persona_service_templates_response_201 = cls(
            id=id,
            provider_kind=provider_kind,
            name=name,
            base_url=base_url,
            documentation_url=documentation_url,
            status_url=status_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_persona_service_templates_response_201

