from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityUserBadgesBody")



@_attrs_define
class PostCommunityUserBadgesBody:
    """ 
        Attributes:
            badge_type (str):
            awarded_at (str):
            ecosystem_id (str | Unset):
     """

    badge_type: str
    awarded_at: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        badge_type = self.badge_type

        awarded_at = self.awarded_at

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "badgeType": badge_type,
            "awardedAt": awarded_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_type = d.pop("badgeType")

        awarded_at = d.pop("awardedAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_user_badges_body = cls(
            badge_type=badge_type,
            awarded_at=awarded_at,
            ecosystem_id=ecosystem_id,
        )

        return post_community_user_badges_body

