from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityDiscussionTagsIdResponse200")



@_attrs_define
class GetCommunityDiscussionTagsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            name (str):
            slug (str):
            color (str):
            created_at (str):
     """

    id: str
    ecosystem_id: str
    name: str
    slug: str
    color: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        name = self.name

        slug = self.slug

        color = self.color

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "name": name,
            "slug": slug,
            "color": color,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        name = d.pop("name")

        slug = d.pop("slug")

        color = d.pop("color")

        created_at = d.pop("createdAt")

        get_community_discussion_tags_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            name=name,
            slug=slug,
            color=color,
            created_at=created_at,
        )

        return get_community_discussion_tags_id_response_200

