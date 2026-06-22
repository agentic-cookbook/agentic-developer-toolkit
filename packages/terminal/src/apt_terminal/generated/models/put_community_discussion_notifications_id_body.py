from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionNotificationsIdBody")



@_attrs_define
class PutCommunityDiscussionNotificationsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            type_ (Union[Unset, str]):
            thread_id (Union[Unset, str]):
            reply_id (Union[None, Unset, str]):
            actor_id (Union[Unset, str]):
            is_read (Union[Unset, bool]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    reply_id: Union[None, Unset, str] = UNSET
    actor_id: Union[Unset, str] = UNSET
    is_read: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        type_ = self.type_

        thread_id = self.thread_id

        reply_id: Union[None, Unset, str]
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

        def _parse_reply_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

