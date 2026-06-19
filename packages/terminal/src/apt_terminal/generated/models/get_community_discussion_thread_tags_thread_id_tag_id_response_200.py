from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200")



@_attrs_define
class GetCommunityDiscussionThreadTagsThreadIdTagIdResponse200:
    """ 
        Attributes:
            ecosystem_id (str):
            thread_id (str):
            tag_id (str):
     """

    ecosystem_id: str
    thread_id: str
    tag_id: str





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        tag_id = self.tag_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ecosystemId": ecosystem_id,
            "threadId": thread_id,
            "tagId": tag_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId")

        thread_id = d.pop("threadId")

        tag_id = d.pop("tagId")

        get_community_discussion_thread_tags_thread_id_tag_id_response_200 = cls(
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            tag_id=tag_id,
        )

        return get_community_discussion_thread_tags_thread_id_tag_id_response_200

