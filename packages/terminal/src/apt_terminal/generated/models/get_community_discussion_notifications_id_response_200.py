from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetCommunityDiscussionNotificationsIdResponse200")



@_attrs_define
class GetCommunityDiscussionNotificationsIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (str):
            ecosystem_id (str):
            type_ (str):
            thread_id (str):
            reply_id (Union[None, str]):
            actor_id (str):
            is_read (bool):
            created_at (str):
     """

    id: str
    user_id: str
    ecosystem_id: str
    type_: str
    thread_id: str
    reply_id: Union[None, str]
    actor_id: str
    is_read: bool
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        type_ = self.type_

        thread_id = self.thread_id

        reply_id: Union[None, str]
        reply_id = self.reply_id

        actor_id = self.actor_id

        is_read = self.is_read

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "type": type_,
            "threadId": thread_id,
            "replyId": reply_id,
            "actorId": actor_id,
            "isRead": is_read,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        type_ = d.pop("type")

        thread_id = d.pop("threadId")

        def _parse_reply_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reply_id = _parse_reply_id(d.pop("replyId"))


        actor_id = d.pop("actorId")

        is_read = d.pop("isRead")

        created_at = d.pop("createdAt")

        get_community_discussion_notifications_id_response_200 = cls(
            id=id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            type_=type_,
            thread_id=thread_id,
            reply_id=reply_id,
            actor_id=actor_id,
            is_read=is_read,
            created_at=created_at,
        )

        return get_community_discussion_notifications_id_response_200

