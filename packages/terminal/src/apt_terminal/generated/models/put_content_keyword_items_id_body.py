from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutContentKeywordItemsIdBody")



@_attrs_define
class PutContentKeywordItemsIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            keyword_id (str | Unset):
            target_kind (str | Unset):
            target_id (str | Unset):
            sort_order (int | Unset):
     """

    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    keyword_id: str | Unset = UNSET
    target_kind: str | Unset = UNSET
    target_id: str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        keyword_id = self.keyword_id

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
        if keyword_id is not UNSET:
            field_dict["keywordId"] = keyword_id
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

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        keyword_id = d.pop("keywordId", UNSET)

        target_kind = d.pop("targetKind", UNSET)

        target_id = d.pop("targetId", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        put_content_keyword_items_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            keyword_id=keyword_id,
            target_kind=target_kind,
            target_id=target_id,
            sort_order=sort_order,
        )

        return put_content_keyword_items_id_body

