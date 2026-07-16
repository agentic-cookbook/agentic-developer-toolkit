from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetSettingsNotificationsResponse200Item")



@_attrs_define
class GetSettingsNotificationsResponse200Item:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            ecosystem_id (str):
            category (str):
            email (bool):
            sms (bool):
            in_app (bool):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    ecosystem_id: str
    category: str
    email: bool
    sms: bool
    in_app: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        category = self.category

        email = self.email

        sms = self.sms

        in_app = self.in_app

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ecosystemId": ecosystem_id,
            "category": category,
            "email": email,
            "sms": sms,
            "inApp": in_app,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        ecosystem_id = d.pop("ecosystemId")

        category = d.pop("category")

        email = d.pop("email")

        sms = d.pop("sms")

        in_app = d.pop("inApp")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_settings_notifications_response_200_item = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            category=category,
            email=email,
            sms=sms,
            in_app=in_app,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_settings_notifications_response_200_item

