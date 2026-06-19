from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionThreadTagsBody")



@_attrs_define
class PostCommunityDiscussionThreadTagsBody:
    """ 
        Attributes:
            thread_id (str):
            tag_id (str):
            ecosystem_id (str | Unset):
     """

    thread_id: str
    tag_id: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        tag_id = self.tag_id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "threadId": thread_id,
            "tagId": tag_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("threadId")

        tag_id = d.pop("tagId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_thread_tags_body = cls(
            thread_id=thread_id,
            tag_id=tag_id,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_thread_tags_body

