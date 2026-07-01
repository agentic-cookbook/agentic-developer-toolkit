from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostCustomerCustomersBody")



@_attrs_define
class PostCustomerCustomersBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            external_id (Union[None, Unset, str]):
            email (Union[None, Unset, str]):
            display_name (Union[None, Unset, str]):
            slug (Union[Unset, str]):
            avatar_url (Union[Unset, str]):
            public_profile_enabled (Union[Unset, bool]):
            token_version (Union[Unset, int]):
            preferred_mfa_method (Union[None, Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    public_profile_enabled: Union[Unset, bool] = UNSET
    token_version: Union[Unset, int] = UNSET
    preferred_mfa_method: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        slug = self.slug

        avatar_url = self.avatar_url

        public_profile_enabled = self.public_profile_enabled

        token_version = self.token_version

        preferred_mfa_method: Union[None, Unset, str]
        if isinstance(self.preferred_mfa_method, Unset):
            preferred_mfa_method = UNSET
        else:
            preferred_mfa_method = self.preferred_mfa_method

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if public_profile_enabled is not UNSET:
            field_dict["publicProfileEnabled"] = public_profile_enabled
        if token_version is not UNSET:
            field_dict["tokenVersion"] = token_version
        if preferred_mfa_method is not UNSET:
            field_dict["preferredMfaMethod"] = preferred_mfa_method
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))


        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        slug = d.pop("slug", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        public_profile_enabled = d.pop("publicProfileEnabled", UNSET)

        token_version = d.pop("tokenVersion", UNSET)

        def _parse_preferred_mfa_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_mfa_method = _parse_preferred_mfa_method(d.pop("preferredMfaMethod", UNSET))


        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_customer_customers_body = cls(
            ecosystem_id=ecosystem_id,
            external_id=external_id,
            email=email,
            display_name=display_name,
            slug=slug,
            avatar_url=avatar_url,
            public_profile_enabled=public_profile_enabled,
            token_version=token_version,
            preferred_mfa_method=preferred_mfa_method,
            deleted_at=deleted_at,
        )

        return post_customer_customers_body

