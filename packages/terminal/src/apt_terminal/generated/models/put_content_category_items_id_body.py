from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentCategoryItemsIdBody")



@_attrs_define
class PutContentCategoryItemsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            category_id (Union[Unset, str]):
            target_kind (Union[Unset, str]):
            target_id (Union[Unset, str]):
            sort_order (Union[Unset, int]):
     """

    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    target_kind: Union[Unset, str] = UNSET
    target_id: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        category_id = self.category_id

        target_kind = self.target_kind

        target_id = self.target_id

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if target_kind is not UNSET:
            field_dict["targetKind"] = target_kind
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        category_id = d.pop("categoryId", UNSET)

        target_kind = d.pop("targetKind", UNSET)

        target_id = d.pop("targetId", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        put_content_category_items_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            category_id=category_id,
            target_kind=target_kind,
            target_id=target_id,
            sort_order=sort_order,
        )

        return put_content_category_items_id_body

