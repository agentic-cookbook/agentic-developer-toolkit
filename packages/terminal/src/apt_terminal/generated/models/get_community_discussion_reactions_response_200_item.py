from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityDiscussionReactionsResponse200Item")



@_attrs_define
class GetCommunityDiscussionReactionsResponse200Item:
    """ 
        Attributes:
            id (str):
            target_type (str):
            target_id (str):
            user_id (str):
            ecosystem_id (str):
            emoji (str):
            created_at (str):
     """

    id: str
    target_type: str
    target_id: str
    user_id: str
    ecosystem_id: str
    emoji: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        target_type = self.target_type

        target_id = self.target_id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        emoji = self.emoji

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "targetType": target_type,
            "targetId": target_id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "emoji": emoji,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        target_type = d.pop("targetType")

        target_id = d.pop("targetId")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        emoji = d.pop("emoji")

        created_at = d.pop("createdAt")

        get_community_discussion_reactions_response_200_item = cls(
            id=id,
            target_type=target_type,
            target_id=target_id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            emoji=emoji,
            created_at=created_at,
        )

        return get_community_discussion_reactions_response_200_item

