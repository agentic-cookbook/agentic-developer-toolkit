from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutProjectProjectsIdResponse200")



@_attrs_define
class PutProjectProjectsIdResponse200:
    """ 
        Attributes:
            id (str):
            name (str):
            description (str):
            status (str):
            color (str):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            sync_version (int):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
     """

    id: str
    name: str
    description: str
    status: str
    color: str
    created_at: str
    updated_at: str
    is_deleted: bool
    sync_version: int
    customer_id: str
    deleted_at: None | str
    owner_id: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        status = self.status

        color = self.color

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted

        sync_version = self.sync_version

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "description": description,
            "status": status,
            "color": color,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        status = d.pop("status")

        color = d.pop("color")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        put_project_projects_id_response_200 = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            color=color,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            sync_version=sync_version,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
        )

        return put_project_projects_id_response_200

