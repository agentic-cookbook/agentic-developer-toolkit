from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_system_server_bag_key_response_200_value_type_1 import GetSystemServerBagKeyResponse200ValueType1





T = TypeVar("T", bound="GetSystemServerBagKeyResponse200")



@_attrs_define
class GetSystemServerBagKeyResponse200:
    """ 
        Attributes:
            key (str):
            value (bool | float | GetSystemServerBagKeyResponse200ValueType1 | list[Any] | None | str):
            description (str):
            created_at (str):
            updated_at (str):
     """

    key: str
    value: bool | float | GetSystemServerBagKeyResponse200ValueType1 | list[Any] | None | str
    description: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_system_server_bag_key_response_200_value_type_1 import GetSystemServerBagKeyResponse200ValueType1
        key = self.key

        value: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.value, GetSystemServerBagKeyResponse200ValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "value": value,
            "description": description,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_system_server_bag_key_response_200_value_type_1 import GetSystemServerBagKeyResponse200ValueType1
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> bool | float | GetSystemServerBagKeyResponse200ValueType1 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = GetSystemServerBagKeyResponse200ValueType1.from_dict(data)



                return value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(list[Any], data)

                return value_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetSystemServerBagKeyResponse200ValueType1 | list[Any] | None | str, data)

        value = _parse_value(d.pop("value"))


        description = d.pop("description")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_system_server_bag_key_response_200 = cls(
            key=key,
            value=value,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_system_server_bag_key_response_200

