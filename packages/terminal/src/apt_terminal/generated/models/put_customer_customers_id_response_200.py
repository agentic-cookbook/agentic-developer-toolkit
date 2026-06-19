from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutCustomerCustomersIdResponse200")



@_attrs_define
class PutCustomerCustomersIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            external_id (None | str):
            email (None | str):
            display_name (None | str):
            slug (None | str):
            avatar_url (str):
            token_version (int):
            deleted_at (None | str):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    external_id: None | str
    email: None | str
    display_name: None | str
    slug: None | str
    avatar_url: str
    token_version: int
    deleted_at: None | str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        external_id: None | str
        external_id = self.external_id

        email: None | str
        email = self.email

        display_name: None | str
        display_name = self.display_name

        slug: None | str
        slug = self.slug

        avatar_url = self.avatar_url

        token_version = self.token_version

        deleted_at: None | str
        deleted_at = self.deleted_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "externalId": external_id,
            "email": email,
            "displayName": display_name,
            "slug": slug,
            "avatarUrl": avatar_url,
            "tokenVersion": token_version,
            "deletedAt": deleted_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("externalId"))


        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))


        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("displayName"))


        def _parse_slug(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        slug = _parse_slug(d.pop("slug"))


        avatar_url = d.pop("avatarUrl")

        token_version = d.pop("tokenVersion")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_customer_customers_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            external_id=external_id,
            email=email,
            display_name=display_name,
            slug=slug,
            avatar_url=avatar_url,
            token_version=token_version,
            deleted_at=deleted_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_customer_customers_id_response_200

