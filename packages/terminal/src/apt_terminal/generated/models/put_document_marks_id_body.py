from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutDocumentMarksIdBody")



@_attrs_define
class PutDocumentMarksIdBody:
    """ 
        Attributes:
            block_id (str | Unset):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            mark_type (str | Unset):
            start_anchor (str | Unset):
            end_anchor (str | Unset):
            mark_data (str | Unset):
            is_deleted (bool | Unset):
     """

    block_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    mark_type: str | Unset = UNSET
    start_anchor: str | Unset = UNSET
    end_anchor: str | Unset = UNSET
    mark_data: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        block_id = self.block_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        mark_type = self.mark_type

        start_anchor = self.start_anchor

        end_anchor = self.end_anchor

        mark_data = self.mark_data

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if mark_type is not UNSET:
            field_dict["markType"] = mark_type
        if start_anchor is not UNSET:
            field_dict["startAnchor"] = start_anchor
        if end_anchor is not UNSET:
            field_dict["endAnchor"] = end_anchor
        if mark_data is not UNSET:
            field_dict["markData"] = mark_data
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_id = d.pop("blockId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        mark_type = d.pop("markType", UNSET)

        start_anchor = d.pop("startAnchor", UNSET)

        end_anchor = d.pop("endAnchor", UNSET)

        mark_data = d.pop("markData", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        put_document_marks_id_body = cls(
            block_id=block_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            mark_type=mark_type,
            start_anchor=start_anchor,
            end_anchor=end_anchor,
            mark_data=mark_data,
            is_deleted=is_deleted,
        )

        return put_document_marks_id_body

