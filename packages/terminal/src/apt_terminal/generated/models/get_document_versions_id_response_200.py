from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetDocumentVersionsIdResponse200")



@_attrs_define
class GetDocumentVersionsIdResponse200:
    """ 
        Attributes:
            id (str):
            document_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            name (str):
            description (str):
            pinned_op_id (str):
            pinned_sync_version (int):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            sync_version (int):
     """

    id: str
    document_id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    name: str
    description: str
    pinned_op_id: str
    pinned_sync_version: int
    created_at: str
    updated_at: str
    is_deleted: bool
    sync_version: int





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        name = self.name

        description = self.description

        pinned_op_id = self.pinned_op_id

        pinned_sync_version = self.pinned_sync_version

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted

        sync_version = self.sync_version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "documentId": document_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "name": name,
            "description": description,
            "pinnedOpId": pinned_op_id,
            "pinnedSyncVersion": pinned_sync_version,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
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

        name = d.pop("name")

        description = d.pop("description")

        pinned_op_id = d.pop("pinnedOpId")

        pinned_sync_version = d.pop("pinnedSyncVersion")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        get_document_versions_id_response_200 = cls(
            id=id,
            document_id=document_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            name=name,
            description=description,
            pinned_op_id=pinned_op_id,
            pinned_sync_version=pinned_sync_version,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            sync_version=sync_version,
        )

        return get_document_versions_id_response_200

