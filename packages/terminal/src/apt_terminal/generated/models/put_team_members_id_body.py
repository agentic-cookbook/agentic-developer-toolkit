from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutTeamMembersIdBody")



@_attrs_define
class PutTeamMembersIdBody:
    """ 
        Attributes:
            team_id (str | Unset):
            role (str | Unset):
            added_at (str | Unset):
     """

    team_id: str | Unset = UNSET
    role: str | Unset = UNSET
    added_at: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        role = self.role

        added_at = self.added_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if role is not UNSET:
            field_dict["role"] = role
        if added_at is not UNSET:
            field_dict["addedAt"] = added_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("teamId", UNSET)

        role = d.pop("role", UNSET)

        added_at = d.pop("addedAt", UNSET)

        put_team_members_id_body = cls(
            team_id=team_id,
            role=role,
            added_at=added_at,
        )

        return put_team_members_id_body

