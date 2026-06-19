from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutCommunityDiscussionNotificationsIdBody")



@_attrs_define
class PutCommunityDiscussionNotificationsIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            type_ (str | Unset):
            thread_id (str | Unset):
            reply_id (None | str | Unset):
            actor_id (str | Unset):
            is_read (bool | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    reply_id: None | str | Unset = UNSET
    actor_id: str | Unset = UNSET
    is_read: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        type_ = self.type_

        thread_id = self.thread_id

        reply_id: None | str | Unset
        if isinstance(self.reply_id, Unset):
            reply_id = UNSET
        else:
            reply_id = self.reply_id

        actor_id = self.actor_id

        is_read = self.is_read


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if reply_id is not UNSET:
            field_dict["replyId"] = reply_id
        if actor_id is not UNSET:
            field_dict["actorId"] = actor_id
        if is_read is not UNSET:
            field_dict["isRead"] = is_read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        type_ = d.pop("type", UNSET)

        thread_id = d.pop("threadId", UNSET)

        def _parse_reply_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_id = _parse_reply_id(d.pop("replyId", UNSET))


        actor_id = d.pop("actorId", UNSET)

        is_read = d.pop("isRead", UNSET)

        put_community_discussion_notifications_id_body = cls(
            ecosystem_id=ecosystem_id,
            type_=type_,
            thread_id=thread_id,
            reply_id=reply_id,
            actor_id=actor_id,
            is_read=is_read,
        )

        return put_community_discussion_notifications_id_body

