from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostChatChatRichContentBody")



@_attrs_define
class PostChatChatRichContentBody:
    """ 
        Attributes:
            message_id (str):
            kind (str):
            owner_id (Union[Unset, str]):
            display_order (Union[Unset, int]):
            payload (Union[Unset, str]):
     """

    message_id: str
    kind: str
    owner_id: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    payload: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        kind = self.kind

        owner_id = self.owner_id

        display_order = self.display_order

        payload = self.payload


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageId": message_id,
            "kind": kind,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        kind = d.pop("kind")

        owner_id = d.pop("ownerId", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        payload = d.pop("payload", UNSET)

        post_chat_chat_rich_content_body = cls(
            message_id=message_id,
            kind=kind,
            owner_id=owner_id,
            display_order=display_order,
            payload=payload,
        )

        return post_chat_chat_rich_content_body

