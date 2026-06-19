from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionTagsBody")



@_attrs_define
class PostCommunityDiscussionTagsBody:
    """ 
        Attributes:
            name (str):
            slug (str):
            ecosystem_id (str | Unset):
            color (str | Unset):
     """

    name: str
    slug: str
    ecosystem_id: str | Unset = UNSET
    color: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        ecosystem_id = self.ecosystem_id

        color = self.color


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "slug": slug,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        color = d.pop("color", UNSET)

        post_community_discussion_tags_body = cls(
            name=name,
            slug=slug,
            ecosystem_id=ecosystem_id,
            color=color,
        )

        return post_community_discussion_tags_body

