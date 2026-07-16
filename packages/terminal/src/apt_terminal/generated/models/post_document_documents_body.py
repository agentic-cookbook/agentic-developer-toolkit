from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDocumentDocumentsBody")



@_attrs_define
class PostDocumentDocumentsBody:
    """ 
        Attributes:
            title (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            doc_type (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
            last_op_id (Union[None, Unset, str]):
            last_snapshot_id (Union[None, Unset, str]):
     """

    title: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    doc_type: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    last_op_id: Union[None, Unset, str] = UNSET
    last_snapshot_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        doc_type = self.doc_type

        is_deleted = self.is_deleted

        last_op_id: Union[None, Unset, str]
        if isinstance(self.last_op_id, Unset):
            last_op_id = UNSET
        else:
            last_op_id = self.last_op_id

        last_snapshot_id: Union[None, Unset, str]
        if isinstance(self.last_snapshot_id, Unset):
            last_snapshot_id = UNSET
        else:
            last_snapshot_id = self.last_snapshot_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "title": title,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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
        title = d.pop("title")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        doc_type = d.pop("docType", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_last_op_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_op_id = _parse_last_op_id(d.pop("lastOpId", UNSET))


        def _parse_last_snapshot_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_snapshot_id = _parse_last_snapshot_id(d.pop("lastSnapshotId", UNSET))


        post_document_documents_body = cls(
            title=title,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            doc_type=doc_type,
            is_deleted=is_deleted,
            last_op_id=last_op_id,
            last_snapshot_id=last_snapshot_id,
        )

        return post_document_documents_body

