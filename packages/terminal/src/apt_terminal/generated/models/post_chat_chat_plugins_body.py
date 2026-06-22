from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostChatChatPluginsBody")



@_attrs_define
class PostChatChatPluginsBody:
    """ 
        Attributes:
            message_id (str):
            kind (str):
            owner_id (Union[Unset, str]):
            state (Union[Unset, str]):
            config (Union[Unset, str]):
            state_data (Union[Unset, str]):
            expires_at (Union[None, Unset, str]):
     """

    message_id: str
    kind: str
    owner_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    config: Union[Unset, str] = UNSET
    state_data: Union[Unset, str] = UNSET
    expires_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        kind = self.kind

        owner_id = self.owner_id

        state = self.state

        config = self.config

        state_data = self.state_data

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageId": message_id,
            "kind": kind,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if state is not UNSET:
            field_dict["state"] = state
        if config is not UNSET:
            field_dict["config"] = config
        if state_data is not UNSET:
            field_dict["stateData"] = state_data
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        kind = d.pop("kind")

        owner_id = d.pop("ownerId", UNSET)

        state = d.pop("state", UNSET)

        config = d.pop("config", UNSET)

        state_data = d.pop("stateData", UNSET)

        def _parse_expires_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        post_chat_chat_plugins_body = cls(
            message_id=message_id,
            kind=kind,
            owner_id=owner_id,
            state=state,
            config=config,
            state_data=state_data,
            expires_at=expires_at,
        )

        return post_chat_chat_plugins_body

