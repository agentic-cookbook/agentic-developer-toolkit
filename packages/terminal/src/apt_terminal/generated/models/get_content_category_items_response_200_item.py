from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetContentCategoryItemsResponse200Item")



@_attrs_define
class GetContentCategoryItemsResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            category_id (str):
            target_kind (str):
            target_id (str):
            sort_order (int):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: Union[None, str]
    category_id: str
    target_kind: str
    target_id: str
    sort_order: int
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        category_id = self.category_id

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
            "categoryId": category_id,
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

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        category_id = d.pop("categoryId")

        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        sort_order = d.pop("sortOrder")

        created_at = d.pop("createdAt")

        get_content_category_items_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            category_id=category_id,
            target_kind=target_kind,
            target_id=target_id,
            sort_order=sort_order,
            created_at=created_at,
        )

        return get_content_category_items_response_200_item

