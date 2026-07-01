from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TeamMember")



@_attrs_define
class TeamMember:
    """ 
        Attributes:
            id (str):
            team_id (str):
            user_id (str): the member customer id
            role (str):
            added_at (str):
            email (Union[None, Unset, str]): the member's email (resolved)
            display_name (Union[None, Unset, str]):
     """

    id: str
    team_id: str
    user_id: str
    role: str
    added_at: str
    email: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        user_id = self.user_id

        role = self.role

        added_at = self.added_at

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "teamId": team_id,
            "userId": user_id,
            "role": role,
            "addedAt": added_at,
        })
        if email is not UNSET:
            field_dict["email"] = email
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        team_id = d.pop("teamId")

        user_id = d.pop("userId")

        role = d.pop("role")

        added_at = d.pop("addedAt")

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))


        team_member = cls(
            id=id,
            team_id=team_id,
            user_id=user_id,
            role=role,
            added_at=added_at,
            email=email,
            display_name=display_name,
        )


        team_member.additional_properties = d
        return team_member

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
