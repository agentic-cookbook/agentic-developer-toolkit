from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutCommunityDiscussionBookmarksIdBody")



@_attrs_define
class PutCommunityDiscussionBookmarksIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            thread_id (str | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    thread_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        thread_id = d.pop("threadId", UNSET)

        put_community_discussion_bookmarks_id_body = cls(
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
        )

        return put_community_discussion_bookmarks_id_body

