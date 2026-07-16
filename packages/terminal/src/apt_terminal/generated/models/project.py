from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_owner_kind import ProjectOwnerKind
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="Project")



@_attrs_define
class Project:
    """ 
        Attributes:
            id (str):
            name (str):
            description (str):
            status (str): lifecycle status (DB default 'active')
            color (str): hex board accent (DB default #007AFF)
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            sync_version (int):
            customer_id (str): the customer (user) who created the project
            ecosystem_id (str): the owning ecosystem (tenant scope)
            owner_kind (ProjectOwnerKind): the kind of principal that OWNS the project
            owner_id (str): the owning principal (customer or organization id); server-stamped from the verified ?workspace=
                scope, else the creator
            deleted_at (Union[None, Unset, str]):
            archived_at (Union[None, Unset, str]): ISO timestamp when archived; null = not archived
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
    ecosystem_id: str
    owner_kind: ProjectOwnerKind
    owner_id: str
    deleted_at: Union[None, Unset, str] = UNSET
    archived_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





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

        ecosystem_id = self.ecosystem_id

        owner_kind = self.owner_kind.value

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = self.archived_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
            "ecosystemId": ecosystem_id,
            "ownerKind": owner_kind,
            "ownerId": owner_id,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if archived_at is not UNSET:
            field_dict["archivedAt"] = archived_at

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

        ecosystem_id = d.pop("ecosystemId")

        owner_kind = ProjectOwnerKind(d.pop("ownerKind"))




        owner_id = d.pop("ownerId")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_archived_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archived_at = _parse_archived_at(d.pop("archivedAt", UNSET))


        project = cls(
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
            ecosystem_id=ecosystem_id,
            owner_kind=owner_kind,
            owner_id=owner_id,
            deleted_at=deleted_at,
            archived_at=archived_at,
        )


        project.additional_properties = d
        return project

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
