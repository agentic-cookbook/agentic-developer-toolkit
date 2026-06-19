from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostCommunityDiscussionNotificationsBody")



@_attrs_define
class PostCommunityDiscussionNotificationsBody:
    """ 
        Attributes:
            type_ (str):
            thread_id (str):
            actor_id (str):
            ecosystem_id (str | Unset):
            reply_id (None | str | Unset):
            is_read (bool | Unset):
     """

    type_: str
    thread_id: str
    actor_id: str
    ecosystem_id: str | Unset = UNSET
    reply_id: None | str | Unset = UNSET
    is_read: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        thread_id = self.thread_id

        actor_id = self.actor_id

        ecosystem_id = self.ecosystem_id

        reply_id: None | str | Unset
        if isinstance(self.reply_id, Unset):
            reply_id = UNSET
        else:
            reply_id = self.reply_id

        is_read = self.is_read


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "threadId": thread_id,
            "actorId": actor_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if reply_id is not UNSET:
            field_dict["replyId"] = reply_id
        if is_read is not UNSET:
            field_dict["isRead"] = is_read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        thread_id = d.pop("threadId")

        actor_id = d.pop("actorId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_reply_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_id = _parse_reply_id(d.pop("replyId", UNSET))


        is_read = d.pop("isRead", UNSET)

        post_community_discussion_notifications_body = cls(
            type_=type_,
            thread_id=thread_id,
            actor_id=actor_id,
            ecosystem_id=ecosystem_id,
            reply_id=reply_id,
            is_read=is_read,
        )

        return post_community_discussion_notifications_body

