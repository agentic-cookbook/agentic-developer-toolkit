from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostCommunityDiscussionBookmarksBody")



@_attrs_define
class PostCommunityDiscussionBookmarksBody:
    """ 
        Attributes:
            thread_id (str):
            ecosystem_id (Union[Unset, str]):
     """

    thread_id: str
    ecosystem_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "threadId": thread_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("threadId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_bookmarks_body = cls(
            thread_id=thread_id,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_bookmarks_body

