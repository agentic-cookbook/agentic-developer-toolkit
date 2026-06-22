from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutSystemFeatureFlagsIdBody")



@_attrs_define
class PutSystemFeatureFlagsIdBody:
    """ 
        Attributes:
            key (Union[Unset, str]):
            description (Union[Unset, str]):
            enabled (Union[Unset, bool]):
     """

    key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        description = self.description

        enabled = self.enabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        put_system_feature_flags_id_body = cls(
            key=key,
            description=description,
            enabled=enabled,
        )

        return put_system_feature_flags_id_body

