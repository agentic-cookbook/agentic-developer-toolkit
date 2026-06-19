from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetCommunityDiscussionRepliesResponse200Item")



@_attrs_define
class GetCommunityDiscussionRepliesResponse200Item:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            thread_id (str):
            parent_reply_id (None | str):
            author_id (str):
            body (str):
            is_deleted (bool):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    thread_id: str
    parent_reply_id: None | str
    author_id: str
    body: str
    is_deleted: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        parent_reply_id: None | str
        parent_reply_id = self.parent_reply_id

        author_id = self.author_id

        body = self.body

        is_deleted = self.is_deleted

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "threadId": thread_id,
            "parentReplyId": parent_reply_id,
            "authorId": author_id,
            "body": body,
            "isDeleted": is_deleted,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        thread_id = d.pop("threadId")

        def _parse_parent_reply_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_reply_id = _parse_parent_reply_id(d.pop("parentReplyId"))


        author_id = d.pop("authorId")

        body = d.pop("body")

        is_deleted = d.pop("isDeleted")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_community_discussion_replies_response_200_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            parent_reply_id=parent_reply_id,
            author_id=author_id,
            body=body,
            is_deleted=is_deleted,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_community_discussion_replies_response_200_item

