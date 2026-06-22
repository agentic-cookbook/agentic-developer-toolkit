from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostCommunityDiscussionThreadsBody")



@_attrs_define
class PostCommunityDiscussionThreadsBody:
    """ 
        Attributes:
            category_id (str):
            author_id (str):
            title (str):
            body (str):
            last_activity_at (str):
            ecosystem_id (Union[Unset, str]):
            is_pinned (Union[Unset, bool]):
            is_locked (Union[Unset, bool]):
            is_deleted (Union[Unset, bool]):
            reply_count (Union[Unset, int]):
            answered_reply_id (Union[None, Unset, str]):
     """

    category_id: str
    author_id: str
    title: str
    body: str
    last_activity_at: str
    ecosystem_id: Union[Unset, str] = UNSET
    is_pinned: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    reply_count: Union[Unset, int] = UNSET
    answered_reply_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        author_id = self.author_id

        title = self.title

        body = self.body

        last_activity_at = self.last_activity_at

        ecosystem_id = self.ecosystem_id

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        is_deleted = self.is_deleted

        reply_count = self.reply_count

        answered_reply_id: Union[None, Unset, str]
        if isinstance(self.answered_reply_id, Unset):
            answered_reply_id = UNSET
        else:
            answered_reply_id = self.answered_reply_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "categoryId": category_id,
            "authorId": author_id,
            "title": title,
            "body": body,
            "lastActivityAt": last_activity_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if answered_reply_id is not UNSET:
            field_dict["answeredReplyId"] = answered_reply_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId")

        author_id = d.pop("authorId")

        title = d.pop("title")

        body = d.pop("body")

        last_activity_at = d.pop("lastActivityAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        is_pinned = d.pop("isPinned", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        reply_count = d.pop("replyCount", UNSET)

        def _parse_answered_reply_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answered_reply_id = _parse_answered_reply_id(d.pop("answeredReplyId", UNSET))


        post_community_discussion_threads_body = cls(
            category_id=category_id,
            author_id=author_id,
            title=title,
            body=body,
            last_activity_at=last_activity_at,
            ecosystem_id=ecosystem_id,
            is_pinned=is_pinned,
            is_locked=is_locked,
            is_deleted=is_deleted,
            reply_count=reply_count,
            answered_reply_id=answered_reply_id,
        )

        return post_community_discussion_threads_body

