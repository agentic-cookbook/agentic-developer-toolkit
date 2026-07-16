from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetChatChatParticipantsResponse200Item")



@_attrs_define
class GetChatChatParticipantsResponse200Item:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            chat_id (str):
            participant_id (str):
            type_ (str):
            role (str):
            state (str):
            joined_at (str):
            state_changed_at (str):
            contact_id (Union[None, str]):
            last_read_message_id (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    chat_id: str
    participant_id: str
    type_: str
    role: str
    state: str
    joined_at: str
    state_changed_at: str
    contact_id: Union[None, str]
    last_read_message_id: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        chat_id = self.chat_id

        participant_id = self.participant_id

        type_ = self.type_

        role = self.role

        state = self.state

        joined_at = self.joined_at

        state_changed_at = self.state_changed_at

        contact_id: Union[None, str]
        contact_id = self.contact_id

        last_read_message_id: Union[None, str]
        last_read_message_id = self.last_read_message_id

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "chatId": chat_id,
            "participantId": participant_id,
            "type": type_,
            "role": role,
            "state": state,
            "joinedAt": joined_at,
            "stateChangedAt": state_changed_at,
            "contactId": contact_id,
            "lastReadMessageId": last_read_message_id,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        chat_id = d.pop("chatId")

        participant_id = d.pop("participantId")

        type_ = d.pop("type")

        role = d.pop("role")

        state = d.pop("state")

        joined_at = d.pop("joinedAt")

        state_changed_at = d.pop("stateChangedAt")

        def _parse_contact_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        contact_id = _parse_contact_id(d.pop("contactId"))


        def _parse_last_read_message_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_read_message_id = _parse_last_read_message_id(d.pop("lastReadMessageId"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_chat_chat_participants_response_200_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            chat_id=chat_id,
            participant_id=participant_id,
            type_=type_,
            role=role,
            state=state,
            joined_at=joined_at,
            state_changed_at=state_changed_at,
            contact_id=contact_id,
            last_read_message_id=last_read_message_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_chat_chat_participants_response_200_item

