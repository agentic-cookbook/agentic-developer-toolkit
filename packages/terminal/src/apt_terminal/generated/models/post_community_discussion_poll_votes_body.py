from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionPollVotesBody")



@_attrs_define
class PostCommunityDiscussionPollVotesBody:
    """ 
        Attributes:
            option_id (str):
            ecosystem_id (str | Unset):
     """

    option_id: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        option_id = self.option_id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "optionId": option_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        option_id = d.pop("optionId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_poll_votes_body = cls(
            option_id=option_id,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_poll_votes_body

