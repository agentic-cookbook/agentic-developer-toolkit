from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostCommunityDiscussionPollVotesResponse201")



@_attrs_define
class PostCommunityDiscussionPollVotesResponse201:
    """ 
        Attributes:
            id (str):
            option_id (str):
            user_id (str):
            ecosystem_id (str):
            created_at (str):
     """

    id: str
    option_id: str
    user_id: str
    ecosystem_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        option_id = self.option_id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "optionId": option_id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        option_id = d.pop("optionId")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        created_at = d.pop("createdAt")

        post_community_discussion_poll_votes_response_201 = cls(
            id=id,
            option_id=option_id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            created_at=created_at,
        )

        return post_community_discussion_poll_votes_response_201

