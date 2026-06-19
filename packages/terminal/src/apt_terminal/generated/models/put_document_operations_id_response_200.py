from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutDocumentOperationsIdResponse200")



@_attrs_define
class PutDocumentOperationsIdResponse200:
    """ 
        Attributes:
            id (str):
            document_id (str):
            block_id (None | str):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
            client_id (str):
            client_seq (int):
            op_type (str):
            op_payload (str):
            created_at (str):
            sync_version (int):
            undo_group_id (None | str):
            inverse_of_op_id (None | str):
     """

    id: str
    document_id: str
    block_id: None | str
    customer_id: str
    deleted_at: None | str
    owner_id: str
    client_id: str
    client_seq: int
    op_type: str
    op_payload: str
    created_at: str
    sync_version: int
    undo_group_id: None | str
    inverse_of_op_id: None | str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        block_id: None | str
        block_id = self.block_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        client_id = self.client_id

        client_seq = self.client_seq

        op_type = self.op_type

        op_payload = self.op_payload

        created_at = self.created_at

        sync_version = self.sync_version

        undo_group_id: None | str
        undo_group_id = self.undo_group_id

        inverse_of_op_id: None | str
        inverse_of_op_id = self.inverse_of_op_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "documentId": document_id,
            "blockId": block_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "clientId": client_id,
            "clientSeq": client_seq,
            "opType": op_type,
            "opPayload": op_payload,
            "createdAt": created_at,
            "syncVersion": sync_version,
            "undoGroupId": undo_group_id,
            "inverseOfOpId": inverse_of_op_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        document_id = d.pop("documentId")

        def _parse_block_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        block_id = _parse_block_id(d.pop("blockId"))


        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        client_id = d.pop("clientId")

        client_seq = d.pop("clientSeq")

        op_type = d.pop("opType")

        op_payload = d.pop("opPayload")

        created_at = d.pop("createdAt")

        sync_version = d.pop("syncVersion")

        def _parse_undo_group_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        undo_group_id = _parse_undo_group_id(d.pop("undoGroupId"))


        def _parse_inverse_of_op_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        inverse_of_op_id = _parse_inverse_of_op_id(d.pop("inverseOfOpId"))


        put_document_operations_id_response_200 = cls(
            id=id,
            document_id=document_id,
            block_id=block_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            client_id=client_id,
            client_seq=client_seq,
            op_type=op_type,
            op_payload=op_payload,
            created_at=created_at,
            sync_version=sync_version,
            undo_group_id=undo_group_id,
            inverse_of_op_id=inverse_of_op_id,
        )

        return put_document_operations_id_response_200

