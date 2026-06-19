from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutDocumentDocumentsIdBody")



@_attrs_define
class PutDocumentDocumentsIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            title (str | Unset):
            doc_type (str | Unset):
            is_deleted (bool | Unset):
            last_op_id (None | str | Unset):
            last_snapshot_id (None | str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    title: str | Unset = UNSET
    doc_type: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    last_op_id: None | str | Unset = UNSET
    last_snapshot_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        title = self.title

        doc_type = self.doc_type

        is_deleted = self.is_deleted

        last_op_id: None | str | Unset
        if isinstance(self.last_op_id, Unset):
            last_op_id = UNSET
        else:
            last_op_id = self.last_op_id

        last_snapshot_id: None | str | Unset
        if isinstance(self.last_snapshot_id, Unset):
            last_snapshot_id = UNSET
        else:
            last_snapshot_id = self.last_snapshot_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if title is not UNSET:
            field_dict["title"] = title
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if last_op_id is not UNSET:
            field_dict["lastOpId"] = last_op_id
        if last_snapshot_id is not UNSET:
            field_dict["lastSnapshotId"] = last_snapshot_id

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

        title = d.pop("title", UNSET)

        doc_type = d.pop("docType", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_last_op_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_op_id = _parse_last_op_id(d.pop("lastOpId", UNSET))


        def _parse_last_snapshot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_snapshot_id = _parse_last_snapshot_id(d.pop("lastSnapshotId", UNSET))


        put_document_documents_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            title=title,
            doc_type=doc_type,
            is_deleted=is_deleted,
            last_op_id=last_op_id,
            last_snapshot_id=last_snapshot_id,
        )

        return put_document_documents_id_body

