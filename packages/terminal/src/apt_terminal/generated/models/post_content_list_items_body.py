from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_content_list_items_body_value_type_1 import PostContentListItemsBodyValueType1





T = TypeVar("T", bound="PostContentListItemsBody")



@_attrs_define
class PostContentListItemsBody:
    """ 
        Attributes:
            list_id (str):
            position (int):
            value (bool | float | list[Any] | None | PostContentListItemsBodyValueType1 | str):
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
     """

    list_id: str
    position: int
    value: bool | float | list[Any] | None | PostContentListItemsBodyValueType1 | str
    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_list_items_body_value_type_1 import PostContentListItemsBodyValueType1
        list_id = self.list_id

        position = self.position

        value: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.value, PostContentListItemsBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "listId": list_id,
            "position": position,
            "value": value,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_content_list_items_body_value_type_1 import PostContentListItemsBodyValueType1
        d = dict(src_dict)
        list_id = d.pop("listId")

        position = d.pop("position")

        def _parse_value(data: object) -> bool | float | list[Any] | None | PostContentListItemsBodyValueType1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PostContentListItemsBodyValueType1.from_dict(data)



                return value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(list[Any], data)

                return value_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | list[Any] | None | PostContentListItemsBodyValueType1 | str, data)

        value = _parse_value(d.pop("value"))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_content_list_items_body = cls(
            list_id=list_id,
            position=position,
            value=value,
            owner_id=owner_id,
            deleted_at=deleted_at,
        )

        return post_content_list_items_body

