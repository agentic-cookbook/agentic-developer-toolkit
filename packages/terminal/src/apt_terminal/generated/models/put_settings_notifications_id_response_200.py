from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutSettingsNotificationsIdResponse200")



@_attrs_define
class PutSettingsNotificationsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
            category (str):
            email (bool):
            sms (bool):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: None | str
    owner_id: str
    category: str
    email: bool
    sms: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        category = self.category

        email = self.email

        sms = self.sms

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "category": category,
            "email": email,
            "sms": sms,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        category = d.pop("category")

        email = d.pop("email")

        sms = d.pop("sms")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_settings_notifications_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            category=category,
            email=email,
            sms=sms,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_settings_notifications_id_response_200

