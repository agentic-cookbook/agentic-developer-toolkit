from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetChatChatRichContentIdResponse200")



@_attrs_define
class GetChatChatRichContentIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            message_id (str):
            display_order (int):
            kind (str):
            payload (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    message_id: str
    display_order: int
    kind: str
    payload: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        message_id = self.message_id

        display_order = self.display_order

        kind = self.kind

        payload = self.payload

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "messageId": message_id,
            "displayOrder": display_order,
            "kind": kind,
            "payload": payload,
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

        display_order = d.pop("displayOrder")

        kind = d.pop("kind")

        payload = d.pop("payload")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_chat_chat_rich_content_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            message_id=message_id,
            display_order=display_order,
            kind=kind,
            payload=payload,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_chat_chat_rich_content_id_response_200

