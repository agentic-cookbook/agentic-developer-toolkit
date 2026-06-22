from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostProjectProjectsBody")



@_attrs_define
class PostProjectProjectsBody:
    """ 
        Attributes:
            name (str):
            description (Union[Unset, str]):
            status (Union[Unset, str]):
            color (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
     """

    name: str
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        status = self.status

        color = self.color

        is_deleted = self.is_deleted

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if color is not UNSET:
            field_dict["color"] = color
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        color = d.pop("color", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        post_project_projects_body = cls(
            name=name,
            description=description,
            status=status,
            color=color,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
            owner_id=owner_id,
        )

        return post_project_projects_body

