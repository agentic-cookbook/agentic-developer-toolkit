from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostDocumentOperationsBody")



@_attrs_define
class PostDocumentOperationsBody:
    """ 
        Attributes:
            document_id (str):
            client_id (str):
            client_seq (int):
            op_type (str):
            block_id (None | str | Unset):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            op_payload (str | Unset):
            undo_group_id (None | str | Unset):
            inverse_of_op_id (None | str | Unset):
     """

    document_id: str
    client_id: str
    client_seq: int
    op_type: str
    block_id: None | str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    op_payload: str | Unset = UNSET
    undo_group_id: None | str | Unset = UNSET
    inverse_of_op_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        client_id = self.client_id

        client_seq = self.client_seq

        op_type = self.op_type

        block_id: None | str | Unset
        if isinstance(self.block_id, Unset):
            block_id = UNSET
        else:
            block_id = self.block_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        op_payload = self.op_payload

        undo_group_id: None | str | Unset
        if isinstance(self.undo_group_id, Unset):
            undo_group_id = UNSET
        else:
            undo_group_id = self.undo_group_id

        inverse_of_op_id: None | str | Unset
        if isinstance(self.inverse_of_op_id, Unset):
            inverse_of_op_id = UNSET
        else:
            inverse_of_op_id = self.inverse_of_op_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "documentId": document_id,
            "clientId": client_id,
            "clientSeq": client_seq,
            "opType": op_type,
        })
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if op_payload is not UNSET:
            field_dict["opPayload"] = op_payload
        if undo_group_id is not UNSET:
            field_dict["undoGroupId"] = undo_group_id
        if inverse_of_op_id is not UNSET:
            field_dict["inverseOfOpId"] = inverse_of_op_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId")

        client_id = d.pop("clientId")

        client_seq = d.pop("clientSeq")

        op_type = d.pop("opType")

        def _parse_block_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_id = _parse_block_id(d.pop("blockId", UNSET))


        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        op_payload = d.pop("opPayload", UNSET)

        def _parse_undo_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        undo_group_id = _parse_undo_group_id(d.pop("undoGroupId", UNSET))


        def _parse_inverse_of_op_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inverse_of_op_id = _parse_inverse_of_op_id(d.pop("inverseOfOpId", UNSET))


        post_document_operations_body = cls(
            document_id=document_id,
            client_id=client_id,
            client_seq=client_seq,
            op_type=op_type,
            block_id=block_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            op_payload=op_payload,
            undo_group_id=undo_group_id,
            inverse_of_op_id=inverse_of_op_id,
        )

        return post_document_operations_body

