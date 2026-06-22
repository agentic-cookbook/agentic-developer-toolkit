from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutChatChatParticipantsIdBody")



@_attrs_define
class PutChatChatParticipantsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            chat_id (Union[Unset, str]):
            participant_id (Union[Unset, str]):
            type_ (Union[Unset, str]):
            role (Union[Unset, str]):
            state (Union[Unset, str]):
            joined_at (Union[Unset, str]):
            state_changed_at (Union[Unset, str]):
            contact_id (Union[None, Unset, str]):
            last_read_message_id (Union[None, Unset, str]):
     """

    owner_id: Union[Unset, str] = UNSET
    chat_id: Union[Unset, str] = UNSET
    participant_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    joined_at: Union[Unset, str] = UNSET
    state_changed_at: Union[Unset, str] = UNSET
    contact_id: Union[None, Unset, str] = UNSET
    last_read_message_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        chat_id = self.chat_id

        participant_id = self.participant_id

        type_ = self.type_

        role = self.role

        state = self.state

        joined_at = self.joined_at

        state_changed_at = self.state_changed_at

        contact_id: Union[None, Unset, str]
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        last_read_message_id: Union[None, Unset, str]
        if isinstance(self.last_read_message_id, Unset):
            last_read_message_id = UNSET
        else:
            last_read_message_id = self.last_read_message_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if participant_id is not UNSET:
            field_dict["participantId"] = participant_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state
        if joined_at is not UNSET:
            field_dict["joinedAt"] = joined_at
        if state_changed_at is not UNSET:
            field_dict["stateChangedAt"] = state_changed_at
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if last_read_message_id is not UNSET:
            field_dict["lastReadMessageId"] = last_read_message_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        chat_id = d.pop("chatId", UNSET)

        participant_id = d.pop("participantId", UNSET)

        type_ = d.pop("type", UNSET)

        role = d.pop("role", UNSET)

        state = d.pop("state", UNSET)

        joined_at = d.pop("joinedAt", UNSET)

        state_changed_at = d.pop("stateChangedAt", UNSET)

        def _parse_contact_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contact_id = _parse_contact_id(d.pop("contactId", UNSET))


        def _parse_last_read_message_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_read_message_id = _parse_last_read_message_id(d.pop("lastReadMessageId", UNSET))


        put_chat_chat_participants_id_body = cls(
            owner_id=owner_id,
            chat_id=chat_id,
            participant_id=participant_id,
            type_=type_,
            role=role,
            state=state,
            joined_at=joined_at,
            state_changed_at=state_changed_at,
            contact_id=contact_id,
            last_read_message_id=last_read_message_id,
        )

        return put_chat_chat_participants_id_body

