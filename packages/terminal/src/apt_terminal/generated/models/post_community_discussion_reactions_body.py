from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionReactionsBody")



@_attrs_define
class PostCommunityDiscussionReactionsBody:
    """ 
        Attributes:
            target_type (str):
            target_id (str):
            emoji (str):
            ecosystem_id (str | Unset):
     """

    target_type: str
    target_id: str
    emoji: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type

        target_id = self.target_id

        emoji = self.emoji

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "targetType": target_type,
            "targetId": target_id,
            "emoji": emoji,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = d.pop("targetType")

        target_id = d.pop("targetId")

        emoji = d.pop("emoji")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_reactions_body = cls(
            target_type=target_type,
            target_id=target_id,
            emoji=emoji,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_reactions_body

