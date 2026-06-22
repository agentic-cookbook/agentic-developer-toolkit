from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostChatChatMentionsResponse201")



@_attrs_define
class PostChatChatMentionsResponse201:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            message_id (str):
            mentioned_participant_id (str):
            created_at (str):
     """

    id: str
    owner_id: str
    message_id: str
    mentioned_participant_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        message_id = self.message_id

        mentioned_participant_id = self.mentioned_participant_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "messageId": message_id,
            "mentionedParticipantId": mentioned_participant_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        message_id = d.pop("messageId")

        mentioned_participant_id = d.pop("mentionedParticipantId")

        created_at = d.pop("createdAt")

        post_chat_chat_mentions_response_201 = cls(
            id=id,
            owner_id=owner_id,
            message_id=message_id,
            mentioned_participant_id=mentioned_participant_id,
            created_at=created_at,
        )

        return post_chat_chat_mentions_response_201

