from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_system_server_bag_key_body_value_type_1 import PutSystemServerBagKeyBodyValueType1





T = TypeVar("T", bound="PutSystemServerBagKeyBody")



@_attrs_define
class PutSystemServerBagKeyBody:
    """ 
        Attributes:
            key (str | Unset):
            value (bool | float | list[Any] | None | PutSystemServerBagKeyBodyValueType1 | str | Unset):
            description (str | Unset):
     """

    key: str | Unset = UNSET
    value: bool | float | list[Any] | None | PutSystemServerBagKeyBodyValueType1 | str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_system_server_bag_key_body_value_type_1 import PutSystemServerBagKeyBodyValueType1
        key = self.key

        value: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PutSystemServerBagKeyBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_system_server_bag_key_body_value_type_1 import PutSystemServerBagKeyBodyValueType1
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        def _parse_value(data: object) -> bool | float | list[Any] | None | PutSystemServerBagKeyBodyValueType1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PutSystemServerBagKeyBodyValueType1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PutSystemServerBagKeyBodyValueType1 | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        description = d.pop("description", UNSET)

        put_system_server_bag_key_body = cls(
            key=key,
            value=value,
            description=description,
        )

        return put_system_server_bag_key_body

