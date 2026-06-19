from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SystemService")



@_attrs_define
class SystemService:
    """ 
        Attributes:
            slug (str):
            kind (str):
            enabled (bool):
            config_keys (list[str]): Names of configured keys; secret values are redacted.
            updated_at (str):
     """

    slug: str
    kind: str
    enabled: bool
    config_keys: list[str]
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        kind = self.kind

        enabled = self.enabled

        config_keys = self.config_keys



        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slug": slug,
            "kind": kind,
            "enabled": enabled,
            "configKeys": config_keys,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        kind = d.pop("kind")

        enabled = d.pop("enabled")

        config_keys = cast(list[str], d.pop("configKeys"))


        updated_at = d.pop("updatedAt")

        system_service = cls(
            slug=slug,
            kind=kind,
            enabled=enabled,
            config_keys=config_keys,
            updated_at=updated_at,
        )


        system_service.additional_properties = d
        return system_service

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
