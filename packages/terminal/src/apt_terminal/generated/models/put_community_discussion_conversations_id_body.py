from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutCommunityDiscussionConversationsIdBody")



@_attrs_define
class PutCommunityDiscussionConversationsIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            participant_1_id (str | Unset):
            participant_2_id (str | Unset):
            last_message_at (str | Unset):
            participant_1_archived_at (None | str | Unset):
            participant_2_archived_at (None | str | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    participant_1_id: str | Unset = UNSET
    participant_2_id: str | Unset = UNSET
    last_message_at: str | Unset = UNSET
    participant_1_archived_at: None | str | Unset = UNSET
    participant_2_archived_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        participant_1_id = self.participant_1_id

        participant_2_id = self.participant_2_id

        last_message_at = self.last_message_at

        participant_1_archived_at: None | str | Unset
        if isinstance(self.participant_1_archived_at, Unset):
            participant_1_archived_at = UNSET
        else:
            participant_1_archived_at = self.participant_1_archived_at

        participant_2_archived_at: None | str | Unset
        if isinstance(self.participant_2_archived_at, Unset):
            participant_2_archived_at = UNSET
        else:
            participant_2_archived_at = self.participant_2_archived_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if participant_1_id is not UNSET:
            field_dict["participant1Id"] = participant_1_id
        if participant_2_id is not UNSET:
            field_dict["participant2Id"] = participant_2_id
        if last_message_at is not UNSET:
            field_dict["lastMessageAt"] = last_message_at
        if participant_1_archived_at is not UNSET:
            field_dict["participant1ArchivedAt"] = participant_1_archived_at
        if participant_2_archived_at is not UNSET:
            field_dict["participant2ArchivedAt"] = participant_2_archived_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        participant_1_id = d.pop("participant1Id", UNSET)

        participant_2_id = d.pop("participant2Id", UNSET)

        last_message_at = d.pop("lastMessageAt", UNSET)

        def _parse_participant_1_archived_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_1_archived_at = _parse_participant_1_archived_at(d.pop("participant1ArchivedAt", UNSET))


        def _parse_participant_2_archived_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_2_archived_at = _parse_participant_2_archived_at(d.pop("participant2ArchivedAt", UNSET))


        put_community_discussion_conversations_id_body = cls(
            ecosystem_id=ecosystem_id,
            participant_1_id=participant_1_id,
            participant_2_id=participant_2_id,
            last_message_at=last_message_at,
            participant_1_archived_at=participant_1_archived_at,
            participant_2_archived_at=participant_2_archived_at,
        )

        return put_community_discussion_conversations_id_body

