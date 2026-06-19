from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutChatChatMessagesIdBody")



@_attrs_define
class PutChatChatMessagesIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            chat_id (str | Unset):
            sender_participant_id (None | str | Unset):
            client_message_id (None | str | Unset):
            seq (int | Unset):
            role (str | Unset):
            body (None | str | Unset):
            tool_calls (None | str | Unset):
            tool_call_id (None | str | Unset):
            tool_name (None | str | Unset):
            reply_to_message_id (None | str | Unset):
            state (str | Unset):
            date_sent (str | Unset):
            date_delivered (None | str | Unset):
            deleted_at (None | str | Unset):
            edited_at (None | str | Unset):
     """

    owner_id: str | Unset = UNSET
    chat_id: str | Unset = UNSET
    sender_participant_id: None | str | Unset = UNSET
    client_message_id: None | str | Unset = UNSET
    seq: int | Unset = UNSET
    role: str | Unset = UNSET
    body: None | str | Unset = UNSET
    tool_calls: None | str | Unset = UNSET
    tool_call_id: None | str | Unset = UNSET
    tool_name: None | str | Unset = UNSET
    reply_to_message_id: None | str | Unset = UNSET
    state: str | Unset = UNSET
    date_sent: str | Unset = UNSET
    date_delivered: None | str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    edited_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        chat_id = self.chat_id

        sender_participant_id: None | str | Unset
        if isinstance(self.sender_participant_id, Unset):
            sender_participant_id = UNSET
        else:
            sender_participant_id = self.sender_participant_id

        client_message_id: None | str | Unset
        if isinstance(self.client_message_id, Unset):
            client_message_id = UNSET
        else:
            client_message_id = self.client_message_id

        seq = self.seq

        role = self.role

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        tool_calls: None | str | Unset
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        else:
            tool_calls = self.tool_calls

        tool_call_id: None | str | Unset
        if isinstance(self.tool_call_id, Unset):
            tool_call_id = UNSET
        else:
            tool_call_id = self.tool_call_id

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        reply_to_message_id: None | str | Unset
        if isinstance(self.reply_to_message_id, Unset):
            reply_to_message_id = UNSET
        else:
            reply_to_message_id = self.reply_to_message_id

        state = self.state

        date_sent = self.date_sent

        date_delivered: None | str | Unset
        if isinstance(self.date_delivered, Unset):
            date_delivered = UNSET
        else:
            date_delivered = self.date_delivered

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        edited_at: None | str | Unset
        if isinstance(self.edited_at, Unset):
            edited_at = UNSET
        else:
            edited_at = self.edited_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if sender_participant_id is not UNSET:
            field_dict["senderParticipantId"] = sender_participant_id
        if client_message_id is not UNSET:
            field_dict["clientMessageId"] = client_message_id
        if seq is not UNSET:
            field_dict["seq"] = seq
        if role is not UNSET:
            field_dict["role"] = role
        if body is not UNSET:
            field_dict["body"] = body
        if tool_calls is not UNSET:
            field_dict["toolCalls"] = tool_calls
        if tool_call_id is not UNSET:
            field_dict["toolCallId"] = tool_call_id
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name
        if reply_to_message_id is not UNSET:
            field_dict["replyToMessageId"] = reply_to_message_id
        if state is not UNSET:
            field_dict["state"] = state
        if date_sent is not UNSET:
            field_dict["dateSent"] = date_sent
        if date_delivered is not UNSET:
            field_dict["dateDelivered"] = date_delivered
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if edited_at is not UNSET:
            field_dict["editedAt"] = edited_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        chat_id = d.pop("chatId", UNSET)

        def _parse_sender_participant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_participant_id = _parse_sender_participant_id(d.pop("senderParticipantId", UNSET))


        def _parse_client_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_message_id = _parse_client_message_id(d.pop("clientMessageId", UNSET))


        seq = d.pop("seq", UNSET)

        role = d.pop("role", UNSET)

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_tool_calls(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_calls = _parse_tool_calls(d.pop("toolCalls", UNSET))


        def _parse_tool_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_call_id = _parse_tool_call_id(d.pop("toolCallId", UNSET))


        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("toolName", UNSET))


        def _parse_reply_to_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to_message_id = _parse_reply_to_message_id(d.pop("replyToMessageId", UNSET))


        state = d.pop("state", UNSET)

        date_sent = d.pop("dateSent", UNSET)

        def _parse_date_delivered(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_delivered = _parse_date_delivered(d.pop("dateDelivered", UNSET))


        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_edited_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edited_at = _parse_edited_at(d.pop("editedAt", UNSET))


        put_chat_chat_messages_id_body = cls(
            owner_id=owner_id,
            chat_id=chat_id,
            sender_participant_id=sender_participant_id,
            client_message_id=client_message_id,
            seq=seq,
            role=role,
            body=body,
            tool_calls=tool_calls,
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            reply_to_message_id=reply_to_message_id,
            state=state,
            date_sent=date_sent,
            date_delivered=date_delivered,
            deleted_at=deleted_at,
            edited_at=edited_at,
        )

        return put_chat_chat_messages_id_body

