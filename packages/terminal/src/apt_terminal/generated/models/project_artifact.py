from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_artifact_direction import ProjectArtifactDirection
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="ProjectArtifact")



@_attrs_define
class ProjectArtifact:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            project_id (str):
            direction (ProjectArtifactDirection): whether the project INGESTED or PRODUCED this target
            target_kind (str): the target's registry, e.g. 'content.markdown'
            target_id (str): the opaque target id
            created_at (str):
            updated_at (str):
            deleted_at (Union[None, Unset, str]): set when un-linked (soft delete); null for a live link
     """

    id: str
    ecosystem_id: str
    project_id: str
    direction: ProjectArtifactDirection
    target_kind: str
    target_id: str
    created_at: str
    updated_at: str
    deleted_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        project_id = self.project_id

        direction = self.direction.value

        target_kind = self.target_kind

        target_id = self.target_id

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "projectId": project_id,
            "direction": direction,
            "targetKind": target_kind,
            "targetId": target_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        project_id = d.pop("projectId")

        direction = ProjectArtifactDirection(d.pop("direction"))




        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        project_artifact = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            project_id=project_id,
            direction=direction,
            target_kind=target_kind,
            target_id=target_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )


        project_artifact.additional_properties = d
        return project_artifact

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
