from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostTeamTeamsBody")



@_attrs_define
class PostTeamTeamsBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            owner_kind (Union[Unset, str]):
            owner_id (Union[Unset, str]):
            description (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    slug: str
    name: str
    owner_kind: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





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

