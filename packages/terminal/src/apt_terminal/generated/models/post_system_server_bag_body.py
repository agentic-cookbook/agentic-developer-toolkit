from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_system_server_bag_body_value_type_1 import PostSystemServerBagBodyValueType1





T = TypeVar("T", bound="PostSystemServerBagBody")



@_attrs_define
class PostSystemServerBagBody:
    """ 
        Attributes:
            key (str):
            value (bool | float | list[Any] | None | PostSystemServerBagBodyValueType1 | str):
            description (str | Unset):
     """

    key: str
    value: bool | float | list[Any] | None | PostSystemServerBagBodyValueType1 | str
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_system_server_bag_body_value_type_1 import PostSystemServerBagBodyValueType1
        key = self.key

        value: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.value, PostSystemServerBagBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "value": value,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_system_server_bag_body_value_type_1 import PostSystemServerBagBodyValueType1
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> bool | float | list[Any] | None | PostSystemServerBagBodyValueType1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PostSystemServerBagBodyValueType1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostSystemServerBagBodyValueType1 | str, data)

        value = _parse_value(d.pop("value"))


        description = d.pop("description", UNSET)

        post_system_server_bag_body = cls(
            key=key,
            value=value,
            description=description,
        )

        return post_system_server_bag_body

