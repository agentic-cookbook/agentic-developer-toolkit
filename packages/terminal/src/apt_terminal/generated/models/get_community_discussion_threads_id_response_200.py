from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetCommunityDiscussionThreadsIdResponse200")



@_attrs_define
class GetCommunityDiscussionThreadsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            category_id (str):
            author_id (str):
            title (str):
            body (str):
            is_pinned (bool):
            is_locked (bool):
            is_deleted (bool):
            reply_count (int):
            answered_reply_id (None | str):
            last_activity_at (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    category_id: str
    author_id: str
    title: str
    body: str
    is_pinned: bool
    is_locked: bool
    is_deleted: bool
    reply_count: int
    answered_reply_id: None | str
    last_activity_at: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        category_id = self.category_id

        author_id = self.author_id

        title = self.title

        body = self.body

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        is_deleted = self.is_deleted

        reply_count = self.reply_count

        answered_reply_id: None | str
        answered_reply_id = self.answered_reply_id

        last_activity_at = self.last_activity_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "categoryId": category_id,
            "authorId": author_id,
            "title": title,
            "body": body,
            "isPinned": is_pinned,
            "isLocked": is_locked,
            "isDeleted": is_deleted,
            "replyCount": reply_count,
            "answeredReplyId": answered_reply_id,
            "lastActivityAt": last_activity_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        category_id = d.pop("categoryId")

        author_id = d.pop("authorId")

        title = d.pop("title")

        body = d.pop("body")

        is_pinned = d.pop("isPinned")

        is_locked = d.pop("isLocked")

        is_deleted = d.pop("isDeleted")

        reply_count = d.pop("replyCount")

        def _parse_answered_reply_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        answered_reply_id = _parse_answered_reply_id(d.pop("answeredReplyId"))


        last_activity_at = d.pop("lastActivityAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_community_discussion_threads_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            category_id=category_id,
            author_id=author_id,
            title=title,
            body=body,
            is_pinned=is_pinned,
            is_locked=is_locked,
            is_deleted=is_deleted,
            reply_count=reply_count,
            answered_reply_id=answered_reply_id,
            last_activity_at=last_activity_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_community_discussion_threads_id_response_200

