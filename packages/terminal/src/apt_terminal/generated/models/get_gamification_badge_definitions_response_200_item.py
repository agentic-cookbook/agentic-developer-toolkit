from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetGamificationBadgeDefinitionsResponse200Item")



@_attrs_define
class GetGamificationBadgeDefinitionsResponse200Item:
    """ 
        Attributes:
            id (str):
            name (str):
            description (str):
            icon (str):
            criteria_type (str):
            criteria_threshold (int):
            point_value (int):
            subject_type (Union[None, str]):
     """

    id: str
    name: str
    description: str
    icon: str
    criteria_type: str
    criteria_threshold: int
    point_value: int
    subject_type: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        icon = self.icon

        criteria_type = self.criteria_type

        criteria_threshold = self.criteria_threshold

        point_value = self.point_value

        subject_type: Union[None, str]
        subject_type = self.subject_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "description": description,
            "icon": icon,
            "criteriaType": criteria_type,
            "criteriaThreshold": criteria_threshold,
            "pointValue": point_value,
            "subjectType": subject_type,
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

        def _parse_subject_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_type = _parse_subject_type(d.pop("subjectType"))


        get_gamification_badge_definitions_response_200_item = cls(
            id=id,
            name=name,
            description=description,
            icon=icon,
            criteria_type=criteria_type,
            criteria_threshold=criteria_threshold,
            point_value=point_value,
            subject_type=subject_type,
        )

        return get_gamification_badge_definitions_response_200_item

