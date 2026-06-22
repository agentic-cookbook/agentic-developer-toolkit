from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.put_system_server_bag_key_response_200_value_type_1 import PutSystemServerBagKeyResponse200ValueType1





T = TypeVar("T", bound="PutSystemServerBagKeyResponse200")



@_attrs_define
class PutSystemServerBagKeyResponse200:
    """ 
        Attributes:
            key (str):
            value (Union['PutSystemServerBagKeyResponse200ValueType1', None, bool, float, list[Any], str]):
            description (str):
            created_at (str):
            updated_at (str):
     """

    key: str
    value: Union['PutSystemServerBagKeyResponse200ValueType1', None, bool, float, list[Any], str]
    description: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_system_server_bag_key_response_200_value_type_1 import PutSystemServerBagKeyResponse200ValueType1
        key = self.key

        value: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.value, PutSystemServerBagKeyResponse200ValueType1):
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
        from ..models.put_system_server_bag_key_response_200_value_type_1 import PutSystemServerBagKeyResponse200ValueType1
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> Union['PutSystemServerBagKeyResponse200ValueType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PutSystemServerBagKeyResponse200ValueType1.from_dict(data)



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
            return cast(Union['PutSystemServerBagKeyResponse200ValueType1', None, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value"))


        description = d.pop("description")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_system_server_bag_key_response_200 = cls(
            key=key,
            value=value,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_system_server_bag_key_response_200

