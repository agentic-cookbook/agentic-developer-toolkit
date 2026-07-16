from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutChatChatMentionsIdBody")



@_attrs_define
class PutChatChatMentionsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            message_id (Union[Unset, str]):
            mentioned_participant_id (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    mentioned_participant_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        message_id = self.message_id

        mentioned_participant_id = self.mentioned_participant_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if mentioned_participant_id is not UNSET:
            field_dict["mentionedParticipantId"] = mentioned_participant_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        message_id = d.pop("messageId", UNSET)

        mentioned_participant_id = d.pop("mentionedParticipantId", UNSET)

        put_chat_chat_mentions_id_body = cls(
            ecosystem_id=ecosystem_id,
            message_id=message_id,
            mentioned_participant_id=mentioned_participant_id,
        )

        return put_chat_chat_mentions_id_body

