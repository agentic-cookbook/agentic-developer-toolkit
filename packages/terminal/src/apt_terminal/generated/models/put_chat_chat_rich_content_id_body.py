from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutChatChatRichContentIdBody")



@_attrs_define
class PutChatChatRichContentIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            message_id (Union[Unset, str]):
            display_order (Union[Unset, int]):
            kind (Union[Unset, str]):
            payload (Union[Unset, str]):
     """

    owner_id: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    kind: Union[Unset, str] = UNSET
    payload: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        message_id = self.message_id

        display_order = self.display_order

        kind = self.kind

        payload = self.payload


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if kind is not UNSET:
            field_dict["kind"] = kind
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        message_id = d.pop("messageId", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        kind = d.pop("kind", UNSET)

        payload = d.pop("payload", UNSET)

        put_chat_chat_rich_content_id_body = cls(
            owner_id=owner_id,
            message_id=message_id,
            display_order=display_order,
            kind=kind,
            payload=payload,
        )

        return put_chat_chat_rich_content_id_body

