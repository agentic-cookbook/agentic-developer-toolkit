from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetChatChatPluginsIdResponse200")



@_attrs_define
class GetChatChatPluginsIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            message_id (str):
            kind (str):
            state (str):
            config (str):
            state_data (str):
            expires_at (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    message_id: str
    kind: str
    state: str
    config: str
    state_data: str
    expires_at: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        message_id = self.message_id

        kind = self.kind

        state = self.state

        config = self.config

        state_data = self.state_data

        expires_at: Union[None, str]
        expires_at = self.expires_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "messageId": message_id,
            "kind": kind,
            "state": state,
            "config": config,
            "stateData": state_data,
            "expiresAt": expires_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        message_id = d.pop("messageId")

        kind = d.pop("kind")

        state = d.pop("state")

        config = d.pop("config")

        state_data = d.pop("stateData")

        def _parse_expires_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_chat_chat_plugins_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            message_id=message_id,
            kind=kind,
            state=state,
            config=config,
            state_data=state_data,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_chat_chat_plugins_id_response_200

