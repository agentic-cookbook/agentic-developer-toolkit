from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetDiscussionTopicsIdResponse200")



@_attrs_define
class GetDiscussionTopicsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            owner_id (str):
            title (str):
            category_id (Union[None, str]):
            is_pinned (bool):
            is_locked (bool):
            is_deleted (bool):
            reply_count (int):
            answered_post_id (Union[None, str]):
            last_activity_at (str):
            created_at (str):
            updated_at (str):
            deleted_at (Union[None, str]):
     """

    id: str
    customer_id: str
    owner_id: str
    title: str
    category_id: Union[None, str]
    is_pinned: bool
    is_locked: bool
    is_deleted: bool
    reply_count: int
    answered_post_id: Union[None, str]
    last_activity_at: str
    created_at: str
    updated_at: str
    deleted_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        owner_id = self.owner_id

        title = self.title

        category_id: Union[None, str]
        category_id = self.category_id

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        is_deleted = self.is_deleted

        reply_count = self.reply_count

        answered_post_id: Union[None, str]
        answered_post_id = self.answered_post_id

        last_activity_at = self.last_activity_at

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "ownerId": owner_id,
            "title": title,
            "categoryId": category_id,
            "isPinned": is_pinned,
            "isLocked": is_locked,
            "isDeleted": is_deleted,
            "replyCount": reply_count,
            "answeredPostId": answered_post_id,
            "lastActivityAt": last_activity_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "deletedAt": deleted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        owner_id = d.pop("ownerId")

        title = d.pop("title")

        def _parse_category_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        category_id = _parse_category_id(d.pop("categoryId"))


        is_pinned = d.pop("isPinned")

        is_locked = d.pop("isLocked")

        is_deleted = d.pop("isDeleted")

        reply_count = d.pop("replyCount")

        def _parse_answered_post_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        answered_post_id = _parse_answered_post_id(d.pop("answeredPostId"))


        last_activity_at = d.pop("lastActivityAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        get_discussion_topics_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            owner_id=owner_id,
            title=title,
            category_id=category_id,
            is_pinned=is_pinned,
            is_locked=is_locked,
            is_deleted=is_deleted,
            reply_count=reply_count,
            answered_post_id=answered_post_id,
            last_activity_at=last_activity_at,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        return get_discussion_topics_id_response_200

