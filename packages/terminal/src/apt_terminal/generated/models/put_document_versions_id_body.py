from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutDocumentVersionsIdBody")



@_attrs_define
class PutDocumentVersionsIdBody:
    """ 
        Attributes:
            document_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            pinned_op_id (Union[Unset, str]):
            pinned_sync_version (Union[Unset, int]):
            is_deleted (Union[Unset, bool]):
     """

    document_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    pinned_op_id: Union[Unset, str] = UNSET
    pinned_sync_version: Union[Unset, int] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        name = self.name

        description = self.description

        pinned_op_id = self.pinned_op_id

        pinned_sync_version = self.pinned_sync_version

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if pinned_op_id is not UNSET:
            field_dict["pinnedOpId"] = pinned_op_id
        if pinned_sync_version is not UNSET:
            field_dict["pinnedSyncVersion"] = pinned_sync_version
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        pinned_op_id = d.pop("pinnedOpId", UNSET)

        pinned_sync_version = d.pop("pinnedSyncVersion", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        put_document_versions_id_body = cls(
            document_id=document_id,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            name=name,
            description=description,
            pinned_op_id=pinned_op_id,
            pinned_sync_version=pinned_sync_version,
            is_deleted=is_deleted,
        )

        return put_document_versions_id_body

