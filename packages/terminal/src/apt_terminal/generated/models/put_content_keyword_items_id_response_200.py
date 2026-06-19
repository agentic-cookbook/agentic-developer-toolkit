from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PutContentKeywordItemsIdResponse200")



@_attrs_define
class PutContentKeywordItemsIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            keyword_id (str):
            target_kind (str):
            target_id (str):
            sort_order (int):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    keyword_id: str
    target_kind: str
    target_id: str
    sort_order: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        keyword_id = self.keyword_id

        target_kind = self.target_kind

        target_id = self.target_id

        sort_order = self.sort_order

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "keywordId": keyword_id,
            "targetKind": target_kind,
            "targetId": target_id,
            "sortOrder": sort_order,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        keyword_id = d.pop("keywordId")

        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        sort_order = d.pop("sortOrder")

        created_at = d.pop("createdAt")

        put_content_keyword_items_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            keyword_id=keyword_id,
            target_kind=target_kind,
            target_id=target_id,
            sort_order=sort_order,
            created_at=created_at,
        )

        return put_content_keyword_items_id_response_200

