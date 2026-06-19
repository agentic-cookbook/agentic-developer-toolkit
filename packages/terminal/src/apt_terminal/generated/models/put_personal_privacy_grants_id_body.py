from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonalPrivacyGrantsIdBody")



@_attrs_define
class PutPersonalPrivacyGrantsIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            target_table (str | Unset):
            target_id (str | Unset):
            audience_mask (int | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    target_table: str | Unset = UNSET
    target_id: str | Unset = UNSET
    audience_mask: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        target_table = self.target_table

        target_id = self.target_id

        audience_mask = self.audience_mask


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if target_table is not UNSET:
            field_dict["targetTable"] = target_table
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if audience_mask is not UNSET:
            field_dict["audienceMask"] = audience_mask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        target_table = d.pop("targetTable", UNSET)

        target_id = d.pop("targetId", UNSET)

        audience_mask = d.pop("audienceMask", UNSET)

        put_personal_privacy_grants_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            target_table=target_table,
            target_id=target_id,
            audience_mask=audience_mask,
        )

        return put_personal_privacy_grants_id_body

