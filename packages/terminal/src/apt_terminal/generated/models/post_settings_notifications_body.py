from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostSettingsNotificationsBody")



@_attrs_define
class PostSettingsNotificationsBody:
    """ 
        Attributes:
            category (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            email (bool | Unset):
            sms (bool | Unset):
     """

    category: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    email: bool | Unset = UNSET
    sms: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        email = self.email

        sms = self.sms


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "category": category,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if email is not UNSET:
            field_dict["email"] = email
        if sms is not UNSET:
            field_dict["sms"] = sms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        email = d.pop("email", UNSET)

        sms = d.pop("sms", UNSET)

        post_settings_notifications_body = cls(
            category=category,
            deleted_at=deleted_at,
            owner_id=owner_id,
            email=email,
            sms=sms,
        )

        return post_settings_notifications_body

