from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDocumentBlocksBody")



@_attrs_define
class PostDocumentBlocksBody:
    """ 
        Attributes:
            document_id (str):
            position (str):
            block_type (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            content_text (Union[Unset, str]):
            content_meta (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
            last_op_id (Union[None, Unset, str]):
     """

    document_id: str
    position: str
    block_type: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    content_text: Union[Unset, str] = UNSET
    content_meta: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    last_op_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        position = self.position

        block_type = self.block_type

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        content_text = self.content_text

        content_meta = self.content_meta

        is_deleted = self.is_deleted

        last_op_id: Union[None, Unset, str]
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
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        content_text = d.pop("contentText", UNSET)

        content_meta = d.pop("contentMeta", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_last_op_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_op_id = _parse_last_op_id(d.pop("lastOpId", UNSET))


        post_document_blocks_body = cls(
            document_id=document_id,
            position=position,
            block_type=block_type,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            content_text=content_text,
            content_meta=content_meta,
            is_deleted=is_deleted,
            last_op_id=last_op_id,
        )

        return post_document_blocks_body

