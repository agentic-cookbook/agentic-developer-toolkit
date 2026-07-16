from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PatchProjectProjectsIdBody")



@_attrs_define
class PatchProjectProjectsIdBody:
    """ 
        Attributes:
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            status (Union[Unset, str]):
            color (Union[Unset, str]):
            archived_at (Union[None, Unset, str]): an ISO timestamp archives; null un-archives
     """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    archived_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        status = self.status

        color = self.color

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = self.archived_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if color is not UNSET:
            field_dict["color"] = color
        if archived_at is not UNSET:
            field_dict["archivedAt"] = archived_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        color = d.pop("color", UNSET)

        def _parse_archived_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archived_at = _parse_archived_at(d.pop("archivedAt", UNSET))


        patch_project_projects_id_body = cls(
            name=name,
            description=description,
            status=status,
            color=color,
            archived_at=archived_at,
        )


        patch_project_projects_id_body.additional_properties = d
        return patch_project_projects_id_body

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
