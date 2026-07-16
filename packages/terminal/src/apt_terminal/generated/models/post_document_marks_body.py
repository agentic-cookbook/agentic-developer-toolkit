from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDocumentMarksBody")



@_attrs_define
class PostDocumentMarksBody:
    """ 
        Attributes:
            block_id (str):
            mark_type (str):
            start_anchor (str):
            end_anchor (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            mark_data (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    block_id: str
    mark_type: str
    start_anchor: str
    end_anchor: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    mark_data: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        block_id = self.block_id

        mark_type = self.mark_type

        start_anchor = self.start_anchor

        end_anchor = self.end_anchor

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        mark_data = self.mark_data

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "blockId": block_id,
            "markType": mark_type,
            "startAnchor": start_anchor,
            "endAnchor": end_anchor,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if mark_data is not UNSET:
            field_dict["markData"] = mark_data
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        block_id = d.pop("blockId")

        mark_type = d.pop("markType")

        start_anchor = d.pop("startAnchor")

        end_anchor = d.pop("endAnchor")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        mark_data = d.pop("markData", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        post_document_marks_body = cls(
            block_id=block_id,
            mark_type=mark_type,
            start_anchor=start_anchor,
            end_anchor=end_anchor,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            mark_data=mark_data,
            is_deleted=is_deleted,
        )

        return post_document_marks_body

