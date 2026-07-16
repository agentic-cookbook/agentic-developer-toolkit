from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_project_projects_id_artifacts_body_direction import PostProjectProjectsIdArtifactsBodyDirection






T = TypeVar("T", bound="PostProjectProjectsIdArtifactsBody")



@_attrs_define
class PostProjectProjectsIdArtifactsBody:
    """ 
        Attributes:
            direction (PostProjectProjectsIdArtifactsBodyDirection):
            target_kind (str): the target's registry, e.g. 'content.markdown'
            target_id (str):
     """

    direction: PostProjectProjectsIdArtifactsBodyDirection
    target_kind: str
    target_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        target_kind = self.target_kind

        target_id = self.target_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "direction": direction,
            "targetKind": target_kind,
            "targetId": target_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direction = PostProjectProjectsIdArtifactsBodyDirection(d.pop("direction"))




        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        post_project_projects_id_artifacts_body = cls(
            direction=direction,
            target_kind=target_kind,
            target_id=target_id,
        )


        post_project_projects_id_artifacts_body.additional_properties = d
        return post_project_projects_id_artifacts_body

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
