from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostContentCategoryItemsBody")



@_attrs_define
class PostContentCategoryItemsBody:
    """ 
        Attributes:
            category_id (str):
            target_kind (str):
            target_id (str):
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            sort_order (int | Unset):
     """

    category_id: str
    target_kind: str
    target_id: str
    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        target_kind = self.target_kind

        target_id = self.target_id

        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "categoryId": category_id,
            "targetKind": target_kind,
            "targetId": target_id,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId")

        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        post_content_category_items_body = cls(
            category_id=category_id,
            target_kind=target_kind,
            target_id=target_id,
            owner_id=owner_id,
            deleted_at=deleted_at,
            sort_order=sort_order,
        )

        return post_content_category_items_body

