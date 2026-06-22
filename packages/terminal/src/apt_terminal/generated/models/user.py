from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ 
        Attributes:
            id (str):
            email (str):
            name (str):
            avatar_url (str):
            slug (Union[None, str]):
            capabilities (list[str]):
     """

    id: str
    email: str
    name: str
    avatar_url: str
    slug: Union[None, str]
    capabilities: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        avatar_url = self.avatar_url

        slug: Union[None, str]
        slug = self.slug

        capabilities = self.capabilities




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "email": email,
            "name": name,
            "avatarUrl": avatar_url,
            "slug": slug,
            "capabilities": capabilities,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        avatar_url = d.pop("avatarUrl")

        def _parse_slug(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        slug = _parse_slug(d.pop("slug"))


        capabilities = cast(list[str], d.pop("capabilities"))


        user = cls(
            id=id,
            email=email,
            name=name,
            avatar_url=avatar_url,
            slug=slug,
            capabilities=capabilities,
        )


        user.additional_properties = d
        return user

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
