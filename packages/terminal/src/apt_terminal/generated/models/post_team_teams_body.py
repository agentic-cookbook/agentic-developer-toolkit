from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostTeamTeamsBody")



@_attrs_define
class PostTeamTeamsBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            owner_kind (str | Unset):
            owner_id (str | Unset):
            description (str | Unset):
            is_deleted (bool | Unset):
     """

    slug: str
    name: str
    owner_kind: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    description: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        owner_kind = self.owner_kind

        owner_id = self.owner_id

        description = self.description

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "name": name,
        })
        if owner_kind is not UNSET:
            field_dict["ownerKind"] = owner_kind
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        owner_kind = d.pop("ownerKind", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        description = d.pop("description", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        post_team_teams_body = cls(
            slug=slug,
            name=name,
            owner_kind=owner_kind,
            owner_id=owner_id,
            description=description,
            is_deleted=is_deleted,
        )

        return post_team_teams_body

