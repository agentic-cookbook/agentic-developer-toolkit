from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutChatChatRichContentIdBody")



@_attrs_define
class PutChatChatRichContentIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            message_id (str | Unset):
            display_order (int | Unset):
            kind (str | Unset):
            payload (str | Unset):
     """

    owner_id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    display_order: int | Unset = UNSET
    kind: str | Unset = UNSET
    payload: str | Unset = UNSET





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

