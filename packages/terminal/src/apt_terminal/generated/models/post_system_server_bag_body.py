from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.post_system_server_bag_body_value_type_1 import PostSystemServerBagBodyValueType1





T = TypeVar("T", bound="PostSystemServerBagBody")



@_attrs_define
class PostSystemServerBagBody:
    """ 
        Attributes:
            key (str):
            value (Union['PostSystemServerBagBodyValueType1', None, bool, float, list[Any], str]):
            description (Union[Unset, str]):
     """

    key: str
    value: Union['PostSystemServerBagBodyValueType1', None, bool, float, list[Any], str]
    description: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_system_server_bag_body_value_type_1 import PostSystemServerBagBodyValueType1
        key = self.key

        value: Union[None, bool, dict[str, Any], float, list[Any], str]
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

        def _parse_value(data: object) -> Union['PostSystemServerBagBodyValueType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PostSystemServerBagBodyValueType1.from_dict(data)



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
            return cast(Union['PostSystemServerBagBodyValueType1', None, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value"))


        description = d.pop("description", UNSET)

        post_system_server_bag_body = cls(
            key=key,
            value=value,
            description=description,
        )

        return post_system_server_bag_body

