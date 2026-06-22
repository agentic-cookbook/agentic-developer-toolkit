from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostTeamMembersBody")



@_attrs_define
class PostTeamMembersBody:
    """ 
        Attributes:
            team_id (str):
            added_at (str):
            role (Union[Unset, str]):
     """

    team_id: str
    added_at: str
    role: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        added_at = self.added_at

        role = self.role


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "teamId": team_id,
            "addedAt": added_at,
        })
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("teamId")

        added_at = d.pop("addedAt")

        role = d.pop("role", UNSET)

        post_team_members_body = cls(
            team_id=team_id,
            added_at=added_at,
            role=role,
        )

        return post_team_members_body

