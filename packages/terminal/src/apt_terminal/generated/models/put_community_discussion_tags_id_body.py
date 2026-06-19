from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutCommunityDiscussionTagsIdBody")



@_attrs_define
class PutCommunityDiscussionTagsIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            name (str | Unset):
            slug (str | Unset):
            color (str | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    color: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        name = self.name

        slug = self.slug

        color = self.color


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        color = d.pop("color", UNSET)

        put_community_discussion_tags_id_body = cls(
            ecosystem_id=ecosystem_id,
            name=name,
            slug=slug,
            color=color,
        )

        return put_community_discussion_tags_id_body

