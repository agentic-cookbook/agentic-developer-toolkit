from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutGamificationBadgeDefinitionsIdBody")



@_attrs_define
class PutGamificationBadgeDefinitionsIdBody:
    """ 
        Attributes:
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            icon (Union[Unset, str]):
            criteria_type (Union[Unset, str]):
            criteria_threshold (Union[Unset, int]):
            point_value (Union[Unset, int]):
            subject_type (Union[None, Unset, str]):
     """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    criteria_type: Union[Unset, str] = UNSET
    criteria_threshold: Union[Unset, int] = UNSET
    point_value: Union[Unset, int] = UNSET
    subject_type: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        icon = self.icon

        criteria_type = self.criteria_type

        criteria_threshold = self.criteria_threshold

        point_value = self.point_value

        subject_type: Union[None, Unset, str]
        if isinstance(self.subject_type, Unset):
            subject_type = UNSET
        else:
            subject_type = self.subject_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if criteria_type is not UNSET:
            field_dict["criteriaType"] = criteria_type
        if criteria_threshold is not UNSET:
            field_dict["criteriaThreshold"] = criteria_threshold
        if point_value is not UNSET:
            field_dict["pointValue"] = point_value
        if subject_type is not UNSET:
            field_dict["subjectType"] = subject_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        criteria_type = d.pop("criteriaType", UNSET)

        criteria_threshold = d.pop("criteriaThreshold", UNSET)

        point_value = d.pop("pointValue", UNSET)

        def _parse_subject_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_type = _parse_subject_type(d.pop("subjectType", UNSET))


        put_gamification_badge_definitions_id_body = cls(
            name=name,
            description=description,
            icon=icon,
            criteria_type=criteria_type,
            criteria_threshold=criteria_threshold,
            point_value=point_value,
            subject_type=subject_type,
        )

        return put_gamification_badge_definitions_id_body

