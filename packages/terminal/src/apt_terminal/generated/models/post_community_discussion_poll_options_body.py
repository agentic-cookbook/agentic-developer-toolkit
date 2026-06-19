from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionPollOptionsBody")



@_attrs_define
class PostCommunityDiscussionPollOptionsBody:
    """ 
        Attributes:
            poll_id (str):
            text (str):
            display_order (int):
            ecosystem_id (str | Unset):
     """

    poll_id: str
    text: str
    display_order: int
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        poll_id = self.poll_id

        text = self.text

        display_order = self.display_order

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "pollId": poll_id,
            "text": text,
            "displayOrder": display_order,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        poll_id = d.pop("pollId")

        text = d.pop("text")

        display_order = d.pop("displayOrder")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_poll_options_body = cls(
            poll_id=poll_id,
            text=text,
            display_order=display_order,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_poll_options_body

