from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostTeamPermissionsBody")



@_attrs_define
class PostTeamPermissionsBody:
    """ 
        Attributes:
            team_id (str):
            permission (str):
            granted_at (str):
            ecosystem_id (str | Unset):
     """

    team_id: str
    permission: str
    granted_at: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        permission = self.permission

        granted_at = self.granted_at

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "teamId": team_id,
            "permission": permission,
            "grantedAt": granted_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("teamId")

        permission = d.pop("permission")

        granted_at = d.pop("grantedAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_team_permissions_body = cls(
            team_id=team_id,
            permission=permission,
            granted_at=granted_at,
            ecosystem_id=ecosystem_id,
        )

        return post_team_permissions_body

