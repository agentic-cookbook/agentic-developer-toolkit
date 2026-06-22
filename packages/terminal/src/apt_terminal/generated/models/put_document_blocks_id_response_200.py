from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutDocumentBlocksIdResponse200")



@_attrs_define
class PutDocumentBlocksIdResponse200:
    """ 
        Attributes:
            id (str):
            document_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            position (str):
            block_type (str):
            content_text (str):
            content_meta (str):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            sync_version (int):
            last_op_id (Union[None, str]):
     """

    id: str
    document_id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    position: str
    block_type: str
    content_text: str
    content_meta: str
    created_at: str
    updated_at: str
    is_deleted: bool
    sync_version: int
    last_op_id: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        position = self.position

        block_type = self.block_type

        content_text = self.content_text

        content_meta = self.content_meta

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted

        sync_version = self.sync_version

        last_op_id: Union[None, str]
        last_op_id = self.last_op_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "documentId": document_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "position": position,
            "blockType": block_type,
            "contentText": content_text,
            "contentMeta": content_meta,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
            "lastOpId": last_op_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        document_id = d.pop("documentId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        position = d.pop("position")

        block_type = d.pop("blockType")

        content_text = d.pop("contentText")

        content_meta = d.pop("contentMeta")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        def _parse_last_op_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_op_id = _parse_last_op_id(d.pop("lastOpId"))


        put_document_blocks_id_response_200 = cls(
            id=id,
            document_id=document_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            position=position,
            block_type=block_type,
            content_text=content_text,
            content_meta=content_meta,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            sync_version=sync_version,
            last_op_id=last_op_id,
        )

        return put_document_blocks_id_response_200

