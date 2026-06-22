from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutTeamTeamsIdResponse200")



@_attrs_define
class PutTeamTeamsIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_kind (str):
            owner_id (str):
            slug (str):
            name (str):
            description (str):
            created_by (Union[None, str]):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
     """

    id: str
    owner_kind: str
    owner_id: str
    slug: str
    name: str
    description: str
    created_by: Union[None, str]
    created_at: str
    updated_at: str
    is_deleted: bool





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_kind = self.owner_kind

        owner_id = self.owner_id

        slug = self.slug

        name = self.name

        description = self.description

        created_by: Union[None, str]
        created_by = self.created_by

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerKind": owner_kind,
            "ownerId": owner_id,
            "slug": slug,
            "name": name,
            "description": description,
            "createdBy": created_by,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_kind = d.pop("ownerKind")

        owner_id = d.pop("ownerId")

        slug = d.pop("slug")

        name = d.pop("name")

        description = d.pop("description")

        def _parse_created_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        created_by = _parse_created_by(d.pop("createdBy"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        put_team_teams_id_response_200 = cls(
            id=id,
            owner_kind=owner_kind,
            owner_id=owner_id,
            slug=slug,
            name=name,
            description=description,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
        )

        return put_team_teams_id_response_200

