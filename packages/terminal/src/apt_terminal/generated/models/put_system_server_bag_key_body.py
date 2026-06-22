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
  from ..models.put_system_server_bag_key_body_value_type_1 import PutSystemServerBagKeyBodyValueType1





T = TypeVar("T", bound="PutSystemServerBagKeyBody")



@_attrs_define
class PutSystemServerBagKeyBody:
    """ 
        Attributes:
            key (Union[Unset, str]):
            value (Union['PutSystemServerBagKeyBodyValueType1', None, Unset, bool, float, list[Any], str]):
            description (Union[Unset, str]):
     """

    key: Union[Unset, str] = UNSET
    value: Union['PutSystemServerBagKeyBodyValueType1', None, Unset, bool, float, list[Any], str] = UNSET
    description: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_system_server_bag_key_body_value_type_1 import PutSystemServerBagKeyBodyValueType1
        key = self.key

        value: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
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

        def _parse_value(data: object) -> Union['PutSystemServerBagKeyBodyValueType1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PutSystemServerBagKeyBodyValueType1.from_dict(data)



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
            return cast(Union['PutSystemServerBagKeyBodyValueType1', None, Unset, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value", UNSET))


        description = d.pop("description", UNSET)

        put_system_server_bag_key_body = cls(
            key=key,
            value=value,
            description=description,
        )

        return put_system_server_bag_key_body

