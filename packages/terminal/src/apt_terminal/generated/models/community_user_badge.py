from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CommunityUserBadge")



@_attrs_define
class CommunityUserBadge:
    """ 
        Attributes:
            id (str):
            badge_type (str): badge_definitions.id this award maps to
            name (str):
            description (str):
            icon (str):
            awarded_at (str):
     """

    id: str
    badge_type: str
    name: str
    description: str
    icon: str
    awarded_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        badge_type = self.badge_type

        name = self.name

        description = self.description

        icon = self.icon

        awarded_at = self.awarded_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "badgeType": badge_type,
            "name": name,
            "description": description,
            "icon": icon,
            "awardedAt": awarded_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        badge_type = d.pop("badgeType")

        name = d.pop("name")

        description = d.pop("description")

        icon = d.pop("icon")

        awarded_at = d.pop("awardedAt")

        community_user_badge = cls(
            id=id,
            badge_type=badge_type,
            name=name,
            description=description,
            icon=icon,
            awarded_at=awarded_at,
        )


        community_user_badge.additional_properties = d
        return community_user_badge

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
