from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostCommunityDiscussionMessagesBody")



@_attrs_define
class PostCommunityDiscussionMessagesBody:
    """ 
        Attributes:
            sender_id (str):
            recipient_id (str):
            body (str):
            ecosystem_id (str | Unset):
            conversation_id (None | str | Unset):
            is_read (bool | Unset):
     """

    sender_id: str
    recipient_id: str
    body: str
    ecosystem_id: str | Unset = UNSET
    conversation_id: None | str | Unset = UNSET
    is_read: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        sender_id = self.sender_id

        recipient_id = self.recipient_id

        body = self.body

        ecosystem_id = self.ecosystem_id

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        is_read = self.is_read


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "senderId": sender_id,
            "recipientId": recipient_id,
            "body": body,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if is_read is not UNSET:
            field_dict["isRead"] = is_read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_id = d.pop("senderId")

        recipient_id = d.pop("recipientId")

        body = d.pop("body")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId", UNSET))


        is_read = d.pop("isRead", UNSET)

        post_community_discussion_messages_body = cls(
            sender_id=sender_id,
            recipient_id=recipient_id,
            body=body,
            ecosystem_id=ecosystem_id,
            conversation_id=conversation_id,
            is_read=is_read,
        )

        return post_community_discussion_messages_body

