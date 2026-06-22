from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostCommunityDiscussionConversationsBody")



@_attrs_define
class PostCommunityDiscussionConversationsBody:
    """ 
        Attributes:
            participant_1_id (str):
            participant_2_id (str):
            last_message_at (str):
            ecosystem_id (Union[Unset, str]):
            participant_1_archived_at (Union[None, Unset, str]):
            participant_2_archived_at (Union[None, Unset, str]):
     """

    participant_1_id: str
    participant_2_id: str
    last_message_at: str
    ecosystem_id: Union[Unset, str] = UNSET
    participant_1_archived_at: Union[None, Unset, str] = UNSET
    participant_2_archived_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        participant_1_id = self.participant_1_id

        participant_2_id = self.participant_2_id

        last_message_at = self.last_message_at

        ecosystem_id = self.ecosystem_id

        participant_1_archived_at: Union[None, Unset, str]
        if isinstance(self.participant_1_archived_at, Unset):
            participant_1_archived_at = UNSET
        else:
            participant_1_archived_at = self.participant_1_archived_at

        participant_2_archived_at: Union[None, Unset, str]
        if isinstance(self.participant_2_archived_at, Unset):
            participant_2_archived_at = UNSET
        else:
            participant_2_archived_at = self.participant_2_archived_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "participant1Id": participant_1_id,
            "participant2Id": participant_2_id,
            "lastMessageAt": last_message_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if participant_1_archived_at is not UNSET:
            field_dict["participant1ArchivedAt"] = participant_1_archived_at
        if participant_2_archived_at is not UNSET:
            field_dict["participant2ArchivedAt"] = participant_2_archived_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        participant_1_id = d.pop("participant1Id")

        participant_2_id = d.pop("participant2Id")

        last_message_at = d.pop("lastMessageAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_participant_1_archived_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        participant_1_archived_at = _parse_participant_1_archived_at(d.pop("participant1ArchivedAt", UNSET))


        def _parse_participant_2_archived_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        participant_2_archived_at = _parse_participant_2_archived_at(d.pop("participant2ArchivedAt", UNSET))


        post_community_discussion_conversations_body = cls(
            participant_1_id=participant_1_id,
            participant_2_id=participant_2_id,
            last_message_at=last_message_at,
            ecosystem_id=ecosystem_id,
            participant_1_archived_at=participant_1_archived_at,
            participant_2_archived_at=participant_2_archived_at,
        )

        return post_community_discussion_conversations_body

