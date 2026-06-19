from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostDocumentBlocksBody")



@_attrs_define
class PostDocumentBlocksBody:
    """ 
        Attributes:
            document_id (str):
            position (str):
            block_type (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            content_text (str | Unset):
            content_meta (str | Unset):
            is_deleted (bool | Unset):
            last_op_id (None | str | Unset):
     """

    document_id: str
    position: str
    block_type: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    content_text: str | Unset = UNSET
    content_meta: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    last_op_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        position = self.position

        block_type = self.block_type

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        content_text = self.content_text

        content_meta = self.content_meta

        is_deleted = self.is_deleted

        last_op_id: None | str | Unset
        if isinstance(self.last_op_id, Unset):
            last_op_id = UNSET
        else:
            last_op_id = self.last_op_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "documentId": document_id,
            "position": position,
            "blockType": block_type,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if content_text is not UNSET:
            field_dict["contentText"] = content_text
        if content_meta is not UNSET:
            field_dict["contentMeta"] = content_meta
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if last_op_id is not UNSET:
            field_dict["lastOpId"] = last_op_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId")

        position = d.pop("position")

        block_type = d.pop("blockType")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        content_text = d.pop("contentText", UNSET)

        content_meta = d.pop("contentMeta", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_last_op_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_op_id = _parse_last_op_id(d.pop("lastOpId", UNSET))


        post_document_blocks_body = cls(
            document_id=document_id,
            position=position,
            block_type=block_type,
            deleted_at=deleted_at,
            owner_id=owner_id,
            content_text=content_text,
            content_meta=content_meta,
            is_deleted=is_deleted,
            last_op_id=last_op_id,
        )

        return post_document_blocks_body

