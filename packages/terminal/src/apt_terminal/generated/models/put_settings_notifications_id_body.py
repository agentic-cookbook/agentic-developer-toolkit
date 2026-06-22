from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutSettingsNotificationsIdBody")



@_attrs_define
class PutSettingsNotificationsIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            category (Union[Unset, str]):
            email (Union[Unset, bool]):
            sms (Union[Unset, bool]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    email: Union[Unset, bool] = UNSET
    sms: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        category = self.category

        email = self.email

        sms = self.sms


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if category is not UNSET:
            field_dict["category"] = category
        if email is not UNSET:
            field_dict["email"] = email
        if sms is not UNSET:
            field_dict["sms"] = sms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        category = d.pop("category", UNSET)

        email = d.pop("email", UNSET)

        sms = d.pop("sms", UNSET)

        put_settings_notifications_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            category=category,
            email=email,
            sms=sms,
        )

        return put_settings_notifications_id_body

