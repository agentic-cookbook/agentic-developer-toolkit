from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostCommunityDiscussionCategoriesBody")



@_attrs_define
class PostCommunityDiscussionCategoriesBody:
    """ 
        Attributes:
            name (str):
            slug (str):
            ecosystem_id (Union[Unset, str]):
            description (Union[Unset, str]):
            display_order (Union[Unset, int]):
            color (Union[Unset, str]):
            is_public (Union[Unset, bool]):
            is_archived (Union[Unset, bool]):
     """

    name: str
    slug: str
    ecosystem_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_archived: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        ecosystem_id = self.ecosystem_id

        description = self.description

        display_order = self.display_order

        color = self.color

        is_public = self.is_public

        is_archived = self.is_archived


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "slug": slug,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if description is not UNSET:
            field_dict["description"] = description
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if color is not UNSET:
            field_dict["color"] = color
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        description = d.pop("description", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        color = d.pop("color", UNSET)

        is_public = d.pop("isPublic", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        post_community_discussion_categories_body = cls(
            name=name,
            slug=slug,
            ecosystem_id=ecosystem_id,
            description=description,
            display_order=display_order,
            color=color,
            is_public=is_public,
            is_archived=is_archived,
        )

        return post_community_discussion_categories_body

