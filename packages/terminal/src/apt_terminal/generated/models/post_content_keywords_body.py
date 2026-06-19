from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostContentKeywordsBody")



@_attrs_define
class PostContentKeywordsBody:
    """ 
        Attributes:
            label (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            color (str | Unset):
            description (str | Unset):
     """

    label: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    color: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        label = self.label

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        color = self.color

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "label": label,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        post_content_keywords_body = cls(
            label=label,
            deleted_at=deleted_at,
            owner_id=owner_id,
            color=color,
            description=description,
        )

        return post_content_keywords_body

