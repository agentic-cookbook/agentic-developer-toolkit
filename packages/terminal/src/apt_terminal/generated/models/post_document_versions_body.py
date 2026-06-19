from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostDocumentVersionsBody")



@_attrs_define
class PostDocumentVersionsBody:
    """ 
        Attributes:
            document_id (str):
            name (str):
            pinned_op_id (str):
            pinned_sync_version (int):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            description (str | Unset):
            is_deleted (bool | Unset):
     """

    document_id: str
    name: str
    pinned_op_id: str
    pinned_sync_version: int
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    description: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        name = self.name

        pinned_op_id = self.pinned_op_id

        pinned_sync_version = self.pinned_sync_version

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        description = self.description

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "documentId": document_id,
            "name": name,
            "pinnedOpId": pinned_op_id,
            "pinnedSyncVersion": pinned_sync_version,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId")

        name = d.pop("name")

        pinned_op_id = d.pop("pinnedOpId")

        pinned_sync_version = d.pop("pinnedSyncVersion")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        description = d.pop("description", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        post_document_versions_body = cls(
            document_id=document_id,
            name=name,
            pinned_op_id=pinned_op_id,
            pinned_sync_version=pinned_sync_version,
            deleted_at=deleted_at,
            owner_id=owner_id,
            description=description,
            is_deleted=is_deleted,
        )

        return post_document_versions_body

