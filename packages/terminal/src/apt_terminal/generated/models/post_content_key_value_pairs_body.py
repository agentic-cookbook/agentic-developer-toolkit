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
  from ..models.post_content_key_value_pairs_body_value_type_1 import PostContentKeyValuePairsBodyValueType1





T = TypeVar("T", bound="PostContentKeyValuePairsBody")



@_attrs_define
class PostContentKeyValuePairsBody:
    """ 
        Attributes:
            key (str):
            value (Union['PostContentKeyValuePairsBodyValueType1', None, bool, float, list[Any], str]):
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    key: str
    value: Union['PostContentKeyValuePairsBodyValueType1', None, bool, float, list[Any], str]
    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_key_value_pairs_body_value_type_1 import PostContentKeyValuePairsBodyValueType1
        key = self.key

        value: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.value, PostContentKeyValuePairsBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "value": value,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_content_key_value_pairs_body_value_type_1 import PostContentKeyValuePairsBodyValueType1
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> Union['PostContentKeyValuePairsBodyValueType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PostContentKeyValuePairsBodyValueType1.from_dict(data)



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
            return cast(Union['PostContentKeyValuePairsBodyValueType1', None, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value"))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_content_key_value_pairs_body = cls(
            key=key,
            value=value,
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
        )

        return post_content_key_value_pairs_body

