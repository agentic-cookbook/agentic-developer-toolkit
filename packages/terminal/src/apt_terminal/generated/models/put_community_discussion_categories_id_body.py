from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionCategoriesIdBody")



@_attrs_define
class PutCommunityDiscussionCategoriesIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            name (Union[Unset, str]):
            slug (Union[Unset, str]):
            description (Union[Unset, str]):
            display_order (Union[Unset, int]):
            color (Union[Unset, str]):
            is_public (Union[Unset, bool]):
            is_archived (Union[Unset, bool]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    color: Union[Unset, str] = UNSET
    is_public: Union[Unset, bool] = UNSET
    is_archived: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        name = self.name

        slug = self.slug

        description = self.description

        display_order = self.display_order

        color = self.color

        is_public = self.is_public

        is_archived = self.is_archived


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
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
        ecosystem_id = d.pop("ecosystemId", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        color = d.pop("color", UNSET)

        is_public = d.pop("isPublic", UNSET)

        is_archived = d.pop("isArchived", UNSET)

        put_community_discussion_categories_id_body = cls(
            ecosystem_id=ecosystem_id,
            name=name,
            slug=slug,
            description=description,
            display_order=display_order,
            color=color,
            is_public=is_public,
            is_archived=is_archived,
        )

        return put_community_discussion_categories_id_body

