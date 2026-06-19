from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostCommunityDiscussionRepliesBody")



@_attrs_define
class PostCommunityDiscussionRepliesBody:
    """ 
        Attributes:
            thread_id (str):
            author_id (str):
            body (str):
            ecosystem_id (str | Unset):
            parent_reply_id (None | str | Unset):
            is_deleted (bool | Unset):
     """

    thread_id: str
    author_id: str
    body: str
    ecosystem_id: str | Unset = UNSET
    parent_reply_id: None | str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        author_id = self.author_id

        body = self.body

        ecosystem_id = self.ecosystem_id

        parent_reply_id: None | str | Unset
        if isinstance(self.parent_reply_id, Unset):
            parent_reply_id = UNSET
        else:
            parent_reply_id = self.parent_reply_id

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "threadId": thread_id,
            "authorId": author_id,
            "body": body,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if parent_reply_id is not UNSET:
            field_dict["parentReplyId"] = parent_reply_id
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("threadId")

        author_id = d.pop("authorId")

        body = d.pop("body")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_parent_reply_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_reply_id = _parse_parent_reply_id(d.pop("parentReplyId", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        post_community_discussion_replies_body = cls(
            thread_id=thread_id,
            author_id=author_id,
            body=body,
            ecosystem_id=ecosystem_id,
            parent_reply_id=parent_reply_id,
            is_deleted=is_deleted,
        )

        return post_community_discussion_replies_body

