from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostChatChatMentionsBody")



@_attrs_define
class PostChatChatMentionsBody:
    """ 
        Attributes:
            message_id (str):
            mentioned_participant_id (str):
            ecosystem_id (Union[Unset, str]):
     """

    message_id: str
    mentioned_participant_id: str
    ecosystem_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        mentioned_participant_id = self.mentioned_participant_id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageId": message_id,
            "mentionedParticipantId": mentioned_participant_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        mentioned_participant_id = d.pop("mentionedParticipantId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_chat_chat_mentions_body = cls(
            message_id=message_id,
            mentioned_participant_id=mentioned_participant_id,
            ecosystem_id=ecosystem_id,
        )

        return post_chat_chat_mentions_body

