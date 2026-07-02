from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="DiscussionTopic")



@_attrs_define
class DiscussionTopic:
    """ 
        Attributes:
            id (str):
            title (str):
            is_pinned (bool):
            is_locked (bool):
            is_public (bool):
            reply_count (int):
            last_activity_at (str):
            created_at (str):
            updated_at (str):
            customer_id (Union[Unset, str]): Author (server-stamped principal). Omitted on the public surface.
            category_id (Union[None, Unset, str]):
            answered_post_id (Union[None, Unset, str]):
     """

    id: str
    title: str
    is_pinned: bool
    is_locked: bool
    is_public: bool
    reply_count: int
    last_activity_at: str
    created_at: str
    updated_at: str
    customer_id: Union[Unset, str] = UNSET
    category_id: Union[None, Unset, str] = UNSET
    answered_post_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        is_pinned = self.is_pinned

        is_locked = self.is_locked

        is_public = self.is_public

        reply_count = self.reply_count

        last_activity_at = self.last_activity_at

        created_at = self.created_at

        updated_at = self.updated_at

        customer_id = self.customer_id

        category_id: Union[None, Unset, str]
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        answered_post_id: Union[None, Unset, str]
        if isinstance(self.answered_post_id, Unset):
            answered_post_id = UNSET
        else:
            answered_post_id = self.answered_post_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "isPinned": is_pinned,
            "isLocked": is_locked,
            "isPublic": is_public,
            "replyCount": reply_count,
            "lastActivityAt": last_activity_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if answered_post_id is not UNSET:
            field_dict["answeredPostId"] = answered_post_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        is_pinned = d.pop("isPinned")

        is_locked = d.pop("isLocked")

        is_public = d.pop("isPublic")

        reply_count = d.pop("replyCount")

        last_activity_at = d.pop("lastActivityAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        customer_id = d.pop("customerId", UNSET)

        def _parse_category_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_id = _parse_category_id(d.pop("categoryId", UNSET))


        def _parse_answered_post_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answered_post_id = _parse_answered_post_id(d.pop("answeredPostId", UNSET))


        discussion_topic = cls(
            id=id,
            title=title,
            is_pinned=is_pinned,
            is_locked=is_locked,
            is_public=is_public,
            reply_count=reply_count,
            last_activity_at=last_activity_at,
            created_at=created_at,
            updated_at=updated_at,
            customer_id=customer_id,
            category_id=category_id,
            answered_post_id=answered_post_id,
        )


        discussion_topic.additional_properties = d
        return discussion_topic

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
