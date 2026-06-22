from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetTeamMembersIdResponse200")



@_attrs_define
class GetTeamMembersIdResponse200:
    """ 
        Attributes:
            id (str):
            team_id (str):
            user_id (str):
            role (str):
            added_by (Union[None, str]):
            added_at (str):
     """

    id: str
    team_id: str
    user_id: str
    role: str
    added_by: Union[None, str]
    added_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        user_id = self.user_id

        role = self.role

        added_by: Union[None, str]
        added_by = self.added_by

        added_at = self.added_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "teamId": team_id,
            "userId": user_id,
            "role": role,
            "addedBy": added_by,
            "addedAt": added_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("teamId")

        user_id = d.pop("userId")

        role = d.pop("role")

        def _parse_added_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        added_by = _parse_added_by(d.pop("addedBy"))


        added_at = d.pop("addedAt")

        get_team_members_id_response_200 = cls(
            id=id,
            team_id=team_id,
            user_id=user_id,
            role=role,
            added_by=added_by,
            added_at=added_at,
        )

        return get_team_members_id_response_200

