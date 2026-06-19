from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutCommunityDiscussionMessagesIdBody")



@_attrs_define
class PutCommunityDiscussionMessagesIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            conversation_id (None | str | Unset):
            sender_id (str | Unset):
            recipient_id (str | Unset):
            body (str | Unset):
            is_read (bool | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    conversation_id: None | str | Unset = UNSET
    sender_id: str | Unset = UNSET
    recipient_id: str | Unset = UNSET
    body: str | Unset = UNSET
    is_read: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        sender_id = self.sender_id

        recipient_id = self.recipient_id

        body = self.body

        is_read = self.is_read


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if body is not UNSET:
            field_dict["body"] = body
        if is_read is not UNSET:
            field_dict["isRead"] = is_read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversationId", UNSET))


        sender_id = d.pop("senderId", UNSET)

        recipient_id = d.pop("recipientId", UNSET)

        body = d.pop("body", UNSET)

        is_read = d.pop("isRead", UNSET)

        put_community_discussion_messages_id_body = cls(
            ecosystem_id=ecosystem_id,
            conversation_id=conversation_id,
            sender_id=sender_id,
            recipient_id=recipient_id,
            body=body,
            is_read=is_read,
        )

        return put_community_discussion_messages_id_body

