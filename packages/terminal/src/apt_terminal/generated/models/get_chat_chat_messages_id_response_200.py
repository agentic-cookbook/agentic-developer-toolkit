from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetChatChatMessagesIdResponse200")



@_attrs_define
class GetChatChatMessagesIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            chat_id (str):
            sender_participant_id (Union[None, str]):
            client_message_id (Union[None, str]):
            seq (int):
            role (str):
            body (Union[None, str]):
            tool_calls (Union[None, str]):
            tool_call_id (Union[None, str]):
            tool_name (Union[None, str]):
            reply_to_message_id (Union[None, str]):
            state (str):
            date_sent (str):
            date_delivered (Union[None, str]):
            deleted_at (Union[None, str]):
            edited_at (Union[None, str]):
     """

    id: str
    owner_id: str
    chat_id: str
    sender_participant_id: Union[None, str]
    client_message_id: Union[None, str]
    seq: int
    role: str
    body: Union[None, str]
    tool_calls: Union[None, str]
    tool_call_id: Union[None, str]
    tool_name: Union[None, str]
    reply_to_message_id: Union[None, str]
    state: str
    date_sent: str
    date_delivered: Union[None, str]
    deleted_at: Union[None, str]
    edited_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        chat_id = self.chat_id

        sender_participant_id: Union[None, str]
        sender_participant_id = self.sender_participant_id

        client_message_id: Union[None, str]
        client_message_id = self.client_message_id

        seq = self.seq

        role = self.role

        body: Union[None, str]
        body = self.body

        tool_calls: Union[None, str]
        tool_calls = self.tool_calls

        tool_call_id: Union[None, str]
        tool_call_id = self.tool_call_id

        tool_name: Union[None, str]
        tool_name = self.tool_name

        reply_to_message_id: Union[None, str]
        reply_to_message_id = self.reply_to_message_id

        state = self.state

        date_sent = self.date_sent

        date_delivered: Union[None, str]
        date_delivered = self.date_delivered

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        edited_at: Union[None, str]
        edited_at = self.edited_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "chatId": chat_id,
            "senderParticipantId": sender_participant_id,
            "clientMessageId": client_message_id,
            "seq": seq,
            "role": role,
            "body": body,
            "toolCalls": tool_calls,
            "toolCallId": tool_call_id,
            "toolName": tool_name,
            "replyToMessageId": reply_to_message_id,
            "state": state,
            "dateSent": date_sent,
            "dateDelivered": date_delivered,
            "deletedAt": deleted_at,
            "editedAt": edited_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        chat_id = d.pop("chatId")

        def _parse_sender_participant_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sender_participant_id = _parse_sender_participant_id(d.pop("senderParticipantId"))


        def _parse_client_message_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        client_message_id = _parse_client_message_id(d.pop("clientMessageId"))


        seq = d.pop("seq")

        role = d.pop("role")

        def _parse_body(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        body = _parse_body(d.pop("body"))


        def _parse_tool_calls(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tool_calls = _parse_tool_calls(d.pop("toolCalls"))


        def _parse_tool_call_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tool_call_id = _parse_tool_call_id(d.pop("toolCallId"))


        def _parse_tool_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tool_name = _parse_tool_name(d.pop("toolName"))


        def _parse_reply_to_message_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        reply_to_message_id = _parse_reply_to_message_id(d.pop("replyToMessageId"))


        state = d.pop("state")

        date_sent = d.pop("dateSent")

        def _parse_date_delivered(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        date_delivered = _parse_date_delivered(d.pop("dateDelivered"))


        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        def _parse_edited_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        edited_at = _parse_edited_at(d.pop("editedAt"))


        get_chat_chat_messages_id_response_200 = cls(
            id=id,
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

        return get_chat_chat_messages_id_response_200

