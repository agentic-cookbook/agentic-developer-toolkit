from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.public_persona_summary import PublicPersonaSummary





T = TypeVar("T", bound="PublicUserProfile")



@_attrs_define
class PublicUserProfile:
    """ 
        Attributes:
            slug (str):
            display_name (Union[None, str]):
            avatar_url (Union[None, str]):
            created_at (str):
            personas (list['PublicPersonaSummary']):
     """

    slug: str
    display_name: Union[None, str]
    avatar_url: Union[None, str]
    created_at: str
    personas: list['PublicPersonaSummary']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_persona_summary import PublicPersonaSummary
        slug = self.slug

        display_name: Union[None, str]
        display_name = self.display_name

        avatar_url: Union[None, str]
        avatar_url = self.avatar_url

        created_at = self.created_at

        personas = []
        for personas_item_data in self.personas:
            personas_item = personas_item_data.to_dict()
            personas.append(personas_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slug": slug,
            "displayName": display_name,
            "avatarUrl": avatar_url,
            "createdAt": created_at,
            "personas": personas,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_persona_summary import PublicPersonaSummary
        d = dict(src_dict)
        slug = d.pop("slug")

        def _parse_display_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        display_name = _parse_display_name(d.pop("displayName"))


        def _parse_avatar_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        avatar_url = _parse_avatar_url(d.pop("avatarUrl"))


        created_at = d.pop("createdAt")

        personas = []
        _personas = d.pop("personas")
        for personas_item_data in (_personas):
            personas_item = PublicPersonaSummary.from_dict(personas_item_data)



            personas.append(personas_item)


        public_user_profile = cls(
            slug=slug,
            display_name=display_name,
            avatar_url=avatar_url,
            created_at=created_at,
            personas=personas,
        )


        public_user_profile.additional_properties = d
        return public_user_profile

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
