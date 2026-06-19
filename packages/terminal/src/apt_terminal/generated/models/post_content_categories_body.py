from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostContentCategoriesBody")



@_attrs_define
class PostContentCategoriesBody:
    """ 
        Attributes:
            name (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            description (str | Unset):
            color (str | Unset):
            icon (str | Unset):
            parent_id (None | str | Unset):
            sort_order (int | Unset):
     """

    name: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    description: str | Unset = UNSET
    color: str | Unset = UNSET
    icon: str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    sort_order: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        description = self.description

        color = self.color

        icon = self.icon

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        post_content_categories_body = cls(
            name=name,
            deleted_at=deleted_at,
            owner_id=owner_id,
            description=description,
            color=color,
            icon=icon,
            parent_id=parent_id,
            sort_order=sort_order,
        )

        return post_content_categories_body

