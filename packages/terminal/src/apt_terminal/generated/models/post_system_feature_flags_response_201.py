from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostSystemFeatureFlagsResponse201")



@_attrs_define
class PostSystemFeatureFlagsResponse201:
    """ 
        Attributes:
            id (int):
            key (str):
            description (str):
            enabled (bool):
            created_at (str):
            updated_at (str):
     """

    id: int
    key: str
    description: str
    enabled: bool
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        description = self.description

        enabled = self.enabled

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "key": key,
            "description": description,
            "enabled": enabled,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        description = d.pop("description")

        enabled = d.pop("enabled")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_system_feature_flags_response_201 = cls(
            id=id,
            key=key,
            description=description,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_system_feature_flags_response_201

