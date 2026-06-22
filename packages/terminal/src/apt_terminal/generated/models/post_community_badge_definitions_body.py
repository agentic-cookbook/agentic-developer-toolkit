from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostCommunityBadgeDefinitionsBody")



@_attrs_define
class PostCommunityBadgeDefinitionsBody:
    """ 
        Attributes:
            name (str):
            description (str):
            icon (str):
            criteria_type (str):
            criteria_threshold (int):
            point_value (Union[Unset, int]):
     """

    name: str
    description: str
    icon: str
    criteria_type: str
    criteria_threshold: int
    point_value: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        icon = self.icon

        criteria_type = self.criteria_type

        criteria_threshold = self.criteria_threshold

        point_value = self.point_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "description": description,
            "icon": icon,
            "criteriaType": criteria_type,
            "criteriaThreshold": criteria_threshold,
        })
        if point_value is not UNSET:
            field_dict["pointValue"] = point_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        icon = d.pop("icon")

        criteria_type = d.pop("criteriaType")

        criteria_threshold = d.pop("criteriaThreshold")

        point_value = d.pop("pointValue", UNSET)

        post_community_badge_definitions_body = cls(
            name=name,
            description=description,
            icon=icon,
            criteria_type=criteria_type,
            criteria_threshold=criteria_threshold,
            point_value=point_value,
        )

        return post_community_badge_definitions_body

