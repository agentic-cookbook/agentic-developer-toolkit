from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDiscussionTopicsBody")



@_attrs_define
class PostDiscussionTopicsBody:
    """ 
        Attributes:
            title (str):
            last_activity_at (str):
            owner_id (Union[Unset, str]):
            category_id (Union[None, Unset, str]):
            is_pinned (Union[Unset, bool]):
            is_locked (Union[Unset, bool]):
            is_deleted (Union[Unset, bool]):
            reply_count (Union[Unset, int]):
            answered_post_id (Union[None, Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    title: str
    last_activity_at: str
    owner_id: Union[Unset, str] = UNSET
    category_id: Union[None, Unset, str] = UNSET
    is_pinned: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    reply_count: Union[Unset, int] = UNSET
    answered_post_id: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        last_activity_at = self.last_activity_at

        owner_id = self.owner_id

        category_id: Union[None, Unset, str]
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        is_deleted = self.is_deleted

        reply_count = self.reply_count

        answered_post_id: Union[None, Unset, str]
        if isinstance(self.answered_post_id, Unset):
            answered_post_id = UNSET
        else:
            answered_post_id = self.answered_post_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "title": title,
            "lastActivityAt": last_activity_at,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if answered_post_id is not UNSET:
            field_dict["answeredPostId"] = answered_post_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        last_activity_at = d.pop("lastActivityAt")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_category_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        is_pinned = d.pop("isPinned", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        reply_count = d.pop("replyCount", UNSET)

        def _parse_answered_post_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answered_post_id = _parse_answered_post_id(d.pop("answeredPostId", UNSET))


        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_discussion_topics_body = cls(
            title=title,
            last_activity_at=last_activity_at,
            owner_id=owner_id,
            category_id=category_id,
            is_pinned=is_pinned,
            is_locked=is_locked,
            is_deleted=is_deleted,
            reply_count=reply_count,
            answered_post_id=answered_post_id,
            deleted_at=deleted_at,
        )

        return post_discussion_topics_body

