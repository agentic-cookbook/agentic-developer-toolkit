from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutChatChatMentionsIdBody")



@_attrs_define
class PutChatChatMentionsIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            message_id (str | Unset):
            mentioned_participant_id (str | Unset):
     """

    owner_id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    mentioned_participant_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        message_id = self.message_id

        mentioned_participant_id = self.mentioned_participant_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if mentioned_participant_id is not UNSET:
            field_dict["mentionedParticipantId"] = mentioned_participant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        message_id = d.pop("messageId", UNSET)

        mentioned_participant_id = d.pop("mentionedParticipantId", UNSET)

        put_chat_chat_mentions_id_body = cls(
            owner_id=owner_id,
            message_id=message_id,
            mentioned_participant_id=mentioned_participant_id,
        )

        return put_chat_chat_mentions_id_body

