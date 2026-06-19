from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CommunityLeaderboardEntry")



@_attrs_define
class CommunityLeaderboardEntry:
    """ 
        Attributes:
            user_id (str):
            name (None | str): customer.customers.display_name
            avatar_url (str):
            total_points (int): SUM(amount) over the selected period
            level (str): Level name computed from totalPoints
     """

    user_id: str
    name: None | str
    avatar_url: str
    total_points: int
    level: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        name: None | str
        name = self.name

        avatar_url = self.avatar_url

        total_points = self.total_points

        level = self.level


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "userId": user_id,
            "name": name,
            "avatarUrl": avatar_url,
            "totalPoints": total_points,
            "level": level,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        avatar_url = d.pop("avatarUrl")

        total_points = d.pop("totalPoints")

        level = d.pop("level")

        community_leaderboard_entry = cls(
            user_id=user_id,
            name=name,
            avatar_url=avatar_url,
            total_points=total_points,
            level=level,
        )


        community_leaderboard_entry.additional_properties = d
        return community_leaderboard_entry

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
