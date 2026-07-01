from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetCustomerCustomersResponse200Item")



@_attrs_define
class GetCustomerCustomersResponse200Item:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            external_id (Union[None, str]):
            email (Union[None, str]):
            display_name (Union[None, str]):
            slug (str):
            avatar_url (str):
            public_profile_enabled (bool):
            token_version (int):
            preferred_mfa_method (Union[None, str]):
            mfa_failed_attempts (int):
            mfa_locked_until (Union[None, str]):
            deleted_at (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    external_id: Union[None, str]
    email: Union[None, str]
    display_name: Union[None, str]
    slug: str
    avatar_url: str
    public_profile_enabled: bool
    token_version: int
    preferred_mfa_method: Union[None, str]
    mfa_failed_attempts: int
    mfa_locked_until: Union[None, str]
    deleted_at: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        external_id: Union[None, str]
        external_id = self.external_id

        email: Union[None, str]
        email = self.email

        display_name: Union[None, str]
        display_name = self.display_name

        slug = self.slug

        avatar_url = self.avatar_url

        public_profile_enabled = self.public_profile_enabled

        token_version = self.token_version

        preferred_mfa_method: Union[None, str]
        preferred_mfa_method = self.preferred_mfa_method

        mfa_failed_attempts = self.mfa_failed_attempts

        mfa_locked_until: Union[None, str]
        mfa_locked_until = self.mfa_locked_until

        deleted_at: Union[None, str]
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
            "publicProfileEnabled": public_profile_enabled,
            "tokenVersion": token_version,
            "preferredMfaMethod": preferred_mfa_method,
            "mfaFailedAttempts": mfa_failed_attempts,
            "mfaLockedUntil": mfa_locked_until,
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

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("externalId"))


        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))


        def _parse_display_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        display_name = _parse_display_name(d.pop("displayName"))


        slug = d.pop("slug")

        avatar_url = d.pop("avatarUrl")

        public_profile_enabled = d.pop("publicProfileEnabled")

        token_version = d.pop("tokenVersion")

        def _parse_preferred_mfa_method(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preferred_mfa_method = _parse_preferred_mfa_method(d.pop("preferredMfaMethod"))


        mfa_failed_attempts = d.pop("mfaFailedAttempts")

        def _parse_mfa_locked_until(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        mfa_locked_until = _parse_mfa_locked_until(d.pop("mfaLockedUntil"))


        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_customer_customers_response_200_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            external_id=external_id,
            email=email,
            display_name=display_name,
            slug=slug,
            avatar_url=avatar_url,
            public_profile_enabled=public_profile_enabled,
            token_version=token_version,
            preferred_mfa_method=preferred_mfa_method,
            mfa_failed_attempts=mfa_failed_attempts,
            mfa_locked_until=mfa_locked_until,
            deleted_at=deleted_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_customer_customers_response_200_item

