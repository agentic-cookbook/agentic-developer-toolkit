from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostSettingsNotificationsBody")



@_attrs_define
class PostSettingsNotificationsBody:
    """ 
        Attributes:
            category (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            email (Union[Unset, bool]):
            sms (Union[Unset, bool]):
            in_app (Union[Unset, bool]):
     """

    category: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    email: Union[Unset, bool] = UNSET
    sms: Union[Unset, bool] = UNSET
    in_app: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        email = self.email

        sms = self.sms

        in_app = self.in_app


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "category": category,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if email is not UNSET:
            field_dict["email"] = email
        if sms is not UNSET:
            field_dict["sms"] = sms
        if in_app is not UNSET:
            field_dict["inApp"] = in_app

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        email = d.pop("email", UNSET)

        sms = d.pop("sms", UNSET)

        in_app = d.pop("inApp", UNSET)

        post_settings_notifications_body = cls(
            category=category,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            email=email,
            sms=sms,
            in_app=in_app,
        )

        return post_settings_notifications_body

