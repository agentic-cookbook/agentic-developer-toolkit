from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostCommunityBadgeDefinitionsResponse201")



@_attrs_define
class PostCommunityBadgeDefinitionsResponse201:
    """ 
        Attributes:
            id (str):
            name (str):
            description (str):
            icon (str):
            criteria_type (str):
            criteria_threshold (int):
            point_value (int):
     """

    id: str
    name: str
    description: str
    icon: str
    criteria_type: str
    criteria_threshold: int
    point_value: int





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        icon = self.icon

        criteria_type = self.criteria_type

        criteria_threshold = self.criteria_threshold

        point_value = self.point_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "description": description,
            "icon": icon,
            "criteriaType": criteria_type,
            "criteriaThreshold": criteria_threshold,
            "pointValue": point_value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        icon = d.pop("icon")

        criteria_type = d.pop("criteriaType")

        criteria_threshold = d.pop("criteriaThreshold")

        point_value = d.pop("pointValue")

        post_community_badge_definitions_response_201 = cls(
            id=id,
            name=name,
            description=description,
            icon=icon,
            criteria_type=criteria_type,
            criteria_threshold=criteria_threshold,
            point_value=point_value,
        )

        return post_community_badge_definitions_response_201

