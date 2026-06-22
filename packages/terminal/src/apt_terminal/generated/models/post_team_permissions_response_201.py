from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostTeamPermissionsResponse201")



@_attrs_define
class PostTeamPermissionsResponse201:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            team_id (str):
            permission (str):
            granted_by (Union[None, str]):
            granted_at (str):
     """

    id: str
    ecosystem_id: str
    team_id: str
    permission: str
    granted_by: Union[None, str]
    granted_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        team_id = self.team_id

        permission = self.permission

        granted_by: Union[None, str]
        granted_by = self.granted_by

        granted_at = self.granted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "teamId": team_id,
            "permission": permission,
            "grantedBy": granted_by,
            "grantedAt": granted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        team_id = d.pop("teamId")

        permission = d.pop("permission")

        def _parse_granted_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        granted_by = _parse_granted_by(d.pop("grantedBy"))


        granted_at = d.pop("grantedAt")

        post_team_permissions_response_201 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            team_id=team_id,
            permission=permission,
            granted_by=granted_by,
            granted_at=granted_at,
        )

        return post_team_permissions_response_201

