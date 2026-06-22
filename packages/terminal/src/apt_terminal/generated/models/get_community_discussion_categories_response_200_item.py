from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityDiscussionCategoriesResponse200Item")



@_attrs_define
class GetCommunityDiscussionCategoriesResponse200Item:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            name (str):
            slug (str):
            description (str):
            display_order (int):
            color (str):
            is_public (bool):
            is_archived (bool):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    name: str
    slug: str
    description: str
    display_order: int
    color: str
    is_public: bool
    is_archived: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        name = self.name

        slug = self.slug

        description = self.description

        display_order = self.display_order

        color = self.color

        is_public = self.is_public

        is_archived = self.is_archived

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "name": name,
            "slug": slug,
            "description": description,
            "displayOrder": display_order,
            "color": color,
            "isPublic": is_public,
            "isArchived": is_archived,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        name = d.pop("name")

        slug = d.pop("slug")

        description = d.pop("description")

        display_order = d.pop("displayOrder")

        color = d.pop("color")

        is_public = d.pop("isPublic")

        is_archived = d.pop("isArchived")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_community_discussion_categories_response_200_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            name=name,
            slug=slug,
            description=description,
            display_order=display_order,
            color=color,
            is_public=is_public,
            is_archived=is_archived,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_community_discussion_categories_response_200_item

