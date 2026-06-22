from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutDocumentOperationsIdBody")



@_attrs_define
class PutDocumentOperationsIdBody:
    """ 
        Attributes:
            document_id (Union[Unset, str]):
            block_id (Union[None, Unset, str]):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            client_id (Union[Unset, str]):
            client_seq (Union[Unset, int]):
            op_type (Union[Unset, str]):
            op_payload (Union[Unset, str]):
            undo_group_id (Union[None, Unset, str]):
            inverse_of_op_id (Union[None, Unset, str]):
     """

    document_id: Union[Unset, str] = UNSET
    block_id: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_seq: Union[Unset, int] = UNSET
    op_type: Union[Unset, str] = UNSET
    op_payload: Union[Unset, str] = UNSET
    undo_group_id: Union[None, Unset, str] = UNSET
    inverse_of_op_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        block_id: Union[None, Unset, str]
        if isinstance(self.block_id, Unset):
            block_id = UNSET
        else:
            block_id = self.block_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        client_id = self.client_id

        client_seq = self.client_seq

        op_type = self.op_type

        op_payload = self.op_payload

        undo_group_id: Union[None, Unset, str]
        if isinstance(self.undo_group_id, Unset):
            undo_group_id = UNSET
        else:
            undo_group_id = self.undo_group_id

        inverse_of_op_id: Union[None, Unset, str]
        if isinstance(self.inverse_of_op_id, Unset):
            inverse_of_op_id = UNSET
        else:
            inverse_of_op_id = self.inverse_of_op_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if block_id is not UNSET:
            field_dict["blockId"] = block_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_seq is not UNSET:
            field_dict["clientSeq"] = client_seq
        if op_type is not UNSET:
            field_dict["opType"] = op_type
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
        document_id = d.pop("documentId", UNSET)

        def _parse_block_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        block_id = _parse_block_id(d.pop("blockId", UNSET))


        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_seq = d.pop("clientSeq", UNSET)

        op_type = d.pop("opType", UNSET)

        op_payload = d.pop("opPayload", UNSET)

        def _parse_undo_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        undo_group_id = _parse_undo_group_id(d.pop("undoGroupId", UNSET))


        def _parse_inverse_of_op_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inverse_of_op_id = _parse_inverse_of_op_id(d.pop("inverseOfOpId", UNSET))


        put_document_operations_id_body = cls(
            document_id=document_id,
            block_id=block_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            client_id=client_id,
            client_seq=client_seq,
            op_type=op_type,
            op_payload=op_payload,
            undo_group_id=undo_group_id,
            inverse_of_op_id=inverse_of_op_id,
        )

        return put_document_operations_id_body

