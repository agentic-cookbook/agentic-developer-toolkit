from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.post_system_server_bag_response_201_value_type_1 import PostSystemServerBagResponse201ValueType1





T = TypeVar("T", bound="PostSystemServerBagResponse201")



@_attrs_define
class PostSystemServerBagResponse201:
    """ 
        Attributes:
            key (str):
            value (Union['PostSystemServerBagResponse201ValueType1', None, bool, float, list[Any], str]):
            description (str):
            created_at (str):
            updated_at (str):
     """

    key: str
    value: Union['PostSystemServerBagResponse201ValueType1', None, bool, float, list[Any], str]
    description: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_system_server_bag_response_201_value_type_1 import PostSystemServerBagResponse201ValueType1
        key = self.key

        value: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.value, PostSystemServerBagResponse201ValueType1):
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
        from ..models.post_system_server_bag_response_201_value_type_1 import PostSystemServerBagResponse201ValueType1
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> Union['PostSystemServerBagResponse201ValueType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PostSystemServerBagResponse201ValueType1.from_dict(data)



                return value_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(list[Any], data)

                return value_type_2
            except: # noqa: E722
                pass
            return cast(Union['PostSystemServerBagResponse201ValueType1', None, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value"))


        description = d.pop("description")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_system_server_bag_response_201 = cls(
            key=key,
            value=value,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_system_server_bag_response_201

