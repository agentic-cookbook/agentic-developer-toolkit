from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityUserBadgesIdBody")



@_attrs_define
class PutCommunityUserBadgesIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            badge_type (Union[Unset, str]):
            awarded_at (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    badge_type: Union[Unset, str] = UNSET
    awarded_at: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        badge_type = self.badge_type

        awarded_at = self.awarded_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if badge_type is not UNSET:
            field_dict["badgeType"] = badge_type
        if awarded_at is not UNSET:
            field_dict["awardedAt"] = awarded_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        badge_type = d.pop("badgeType", UNSET)

        awarded_at = d.pop("awardedAt", UNSET)

        put_community_user_badges_id_body = cls(
            ecosystem_id=ecosystem_id,
            badge_type=badge_type,
            awarded_at=awarded_at,
        )

        return put_community_user_badges_id_body

