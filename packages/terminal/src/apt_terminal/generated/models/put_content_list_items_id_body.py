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
  from ..models.put_content_list_items_id_body_value_type_1 import PutContentListItemsIdBodyValueType1





T = TypeVar("T", bound="PutContentListItemsIdBody")



@_attrs_define
class PutContentListItemsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            list_id (Union[Unset, str]):
            position (Union[Unset, int]):
            value (Union['PutContentListItemsIdBodyValueType1', None, Unset, bool, float, list[Any], str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    list_id: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    value: Union['PutContentListItemsIdBodyValueType1', None, Unset, bool, float, list[Any], str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_list_items_id_body_value_type_1 import PutContentListItemsIdBodyValueType1
        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        list_id = self.list_id

        position = self.position

        value: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PutContentListItemsIdBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if list_id is not UNSET:
            field_dict["listId"] = list_id
        if position is not UNSET:
            field_dict["position"] = position
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_content_list_items_id_body_value_type_1 import PutContentListItemsIdBodyValueType1
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        list_id = d.pop("listId", UNSET)

        position = d.pop("position", UNSET)

        def _parse_value(data: object) -> Union['PutContentListItemsIdBodyValueType1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PutContentListItemsIdBodyValueType1.from_dict(data)



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
            return cast(Union['PutContentListItemsIdBodyValueType1', None, Unset, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value", UNSET))


        put_content_list_items_id_body = cls(
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
            list_id=list_id,
            position=position,
            value=value,
        )

        return put_content_list_items_id_body

