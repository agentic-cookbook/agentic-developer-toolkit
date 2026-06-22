from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentKeywordItemsBody")



@_attrs_define
class PostContentKeywordItemsBody:
    """ 
        Attributes:
            keyword_id (str):
            target_kind (str):
            target_id (str):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            sort_order (Union[Unset, int]):
     """

    keyword_id: str
    target_kind: str
    target_id: str
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        keyword_id = self.keyword_id

        target_kind = self.target_kind

        target_id = self.target_id

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "keywordId": keyword_id,
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
        keyword_id = d.pop("keywordId")

        target_kind = d.pop("targetKind")

        target_id = d.pop("targetId")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        post_content_keyword_items_body = cls(
            keyword_id=keyword_id,
            target_kind=target_kind,
            target_id=target_id,
            owner_id=owner_id,
            deleted_at=deleted_at,
            sort_order=sort_order,
        )

        return post_content_keyword_items_body

