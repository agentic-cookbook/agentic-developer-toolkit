from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutCommunityDiscussionMessagesIdResponse200")



@_attrs_define
class PutCommunityDiscussionMessagesIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            conversation_id (None | str):
            sender_id (str):
            recipient_id (str):
            body (str):
            is_read (bool):
            created_at (str):
     """

    id: str
    ecosystem_id: str
    conversation_id: None | str
    sender_id: str
    recipient_id: str
    body: str
    is_read: bool
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        conversation_id: None | str
        conversation_id = self.conversation_id

        sender_id = self.sender_id

        recipient_id = self.recipient_id

        body = self.body

        is_read = self.is_read

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "conversationId": conversation_id,
            "senderId": sender_id,
            "recipientId": recipient_id,
            "body": body,
            "isRead": is_read,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        def _parse_conversation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId"))


        sender_id = d.pop("senderId")

        recipient_id = d.pop("recipientId")

        body = d.pop("body")

        is_read = d.pop("isRead")

        created_at = d.pop("createdAt")

        put_community_discussion_messages_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            conversation_id=conversation_id,
            sender_id=sender_id,
            recipient_id=recipient_id,
            body=body,
            is_read=is_read,
            created_at=created_at,
        )

        return put_community_discussion_messages_id_response_200

