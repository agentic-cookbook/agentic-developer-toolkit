from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetContentReactionsIdResponse200")



@_attrs_define
class GetContentReactionsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            target_kind (str):
            target_id (str):
            emoji (str):
            created_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    target_kind: str
    target_id: str
    emoji: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        target_kind = self.target_kind

        target_id = self.target_id

        emoji = self.emoji

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "targetKind": target_kind,
            "targetId": target_id,
            "emoji": emoji,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        emoji = d.pop("emoji")

        created_at = d.pop("createdAt")

        get_content_reactions_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            target_kind=target_kind,
            target_id=target_id,
            emoji=emoji,
            created_at=created_at,
        )

        return get_content_reactions_id_response_200

