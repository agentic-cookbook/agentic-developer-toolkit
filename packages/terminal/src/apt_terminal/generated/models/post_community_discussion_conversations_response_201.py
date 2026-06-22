from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostCommunityDiscussionConversationsResponse201")



@_attrs_define
class PostCommunityDiscussionConversationsResponse201:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            participant_1_id (str):
            participant_2_id (str):
            last_message_at (str):
            created_at (str):
            participant_1_archived_at (Union[None, str]):
            participant_2_archived_at (Union[None, str]):
     """

    id: str
    ecosystem_id: str
    participant_1_id: str
    participant_2_id: str
    last_message_at: str
    created_at: str
    participant_1_archived_at: Union[None, str]
    participant_2_archived_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        participant_1_id = self.participant_1_id

        participant_2_id = self.participant_2_id

        last_message_at = self.last_message_at

        created_at = self.created_at

        participant_1_archived_at: Union[None, str]
        participant_1_archived_at = self.participant_1_archived_at

        participant_2_archived_at: Union[None, str]
        participant_2_archived_at = self.participant_2_archived_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "participant1Id": participant_1_id,
            "participant2Id": participant_2_id,
            "lastMessageAt": last_message_at,
            "createdAt": created_at,
            "participant1ArchivedAt": participant_1_archived_at,
            "participant2ArchivedAt": participant_2_archived_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        participant_1_id = d.pop("participant1Id")

        participant_2_id = d.pop("participant2Id")

        last_message_at = d.pop("lastMessageAt")

        created_at = d.pop("createdAt")

        def _parse_participant_1_archived_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        participant_1_archived_at = _parse_participant_1_archived_at(d.pop("participant1ArchivedAt"))


        def _parse_participant_2_archived_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        participant_2_archived_at = _parse_participant_2_archived_at(d.pop("participant2ArchivedAt"))


        post_community_discussion_conversations_response_201 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            participant_1_id=participant_1_id,
            participant_2_id=participant_2_id,
            last_message_at=last_message_at,
            created_at=created_at,
            participant_1_archived_at=participant_1_archived_at,
            participant_2_archived_at=participant_2_archived_at,
        )

        return post_community_discussion_conversations_response_201

