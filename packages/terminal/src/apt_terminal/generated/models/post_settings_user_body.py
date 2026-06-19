from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostSettingsUserBody")



@_attrs_define
class PostSettingsUserBody:
    """ 
        Attributes:
            key (str):
            value (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
     """

    key: str
    value: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "value": value,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        post_settings_user_body = cls(
            key=key,
            value=value,
            deleted_at=deleted_at,
            owner_id=owner_id,
        )

        return post_settings_user_body

