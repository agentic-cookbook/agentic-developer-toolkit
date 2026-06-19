from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityUserBadgesIdResponse200")



@_attrs_define
class GetCommunityUserBadgesIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (str):
            ecosystem_id (str):
            badge_type (str):
            awarded_at (str):
     """

    id: str
    user_id: str
    ecosystem_id: str
    badge_type: str
    awarded_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        badge_type = self.badge_type

        awarded_at = self.awarded_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "badgeType": badge_type,
            "awardedAt": awarded_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        badge_type = d.pop("badgeType")

        awarded_at = d.pop("awardedAt")

        get_community_user_badges_id_response_200 = cls(
            id=id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            badge_type=badge_type,
            awarded_at=awarded_at,
        )

        return get_community_user_badges_id_response_200

