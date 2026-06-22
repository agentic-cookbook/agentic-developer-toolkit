from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutTeamPermissionsIdBody")



@_attrs_define
class PutTeamPermissionsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            team_id (Union[Unset, str]):
            permission (Union[Unset, str]):
            granted_at (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    permission: Union[Unset, str] = UNSET
    granted_at: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        team_id = self.team_id

        permission = self.permission

        granted_at = self.granted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if permission is not UNSET:
            field_dict["permission"] = permission
        if granted_at is not UNSET:
            field_dict["grantedAt"] = granted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        team_id = d.pop("teamId", UNSET)

        permission = d.pop("permission", UNSET)

        granted_at = d.pop("grantedAt", UNSET)

        put_team_permissions_id_body = cls(
            ecosystem_id=ecosystem_id,
            team_id=team_id,
            permission=permission,
            granted_at=granted_at,
        )

        return put_team_permissions_id_body

