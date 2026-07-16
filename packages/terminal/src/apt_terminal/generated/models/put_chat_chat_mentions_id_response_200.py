from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutChatChatMentionsIdResponse200")



@_attrs_define
class PutChatChatMentionsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            message_id (str):
            mentioned_participant_id (str):
            created_at (str):
     """

    id: str
    ecosystem_id: str
    message_id: str
    mentioned_participant_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        message_id = self.message_id

        mentioned_participant_id = self.mentioned_participant_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "messageId": message_id,
            "mentionedParticipantId": mentioned_participant_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        message_id = d.pop("messageId")

        mentioned_participant_id = d.pop("mentionedParticipantId")

        created_at = d.pop("createdAt")

        put_chat_chat_mentions_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            message_id=message_id,
            mentioned_participant_id=mentioned_participant_id,
            created_at=created_at,
        )

        return put_chat_chat_mentions_id_response_200

