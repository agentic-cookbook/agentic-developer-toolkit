from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.get_content_list_items_response_200_item_value_type_1 import GetContentListItemsResponse200ItemValueType1





T = TypeVar("T", bound="GetContentListItemsResponse200Item")



@_attrs_define
class GetContentListItemsResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            list_id (str):
            position (int):
            value (Union['GetContentListItemsResponse200ItemValueType1', None, bool, float, list[Any], str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: Union[None, str]
    list_id: str
    position: int
    value: Union['GetContentListItemsResponse200ItemValueType1', None, bool, float, list[Any], str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_content_list_items_response_200_item_value_type_1 import GetContentListItemsResponse200ItemValueType1
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        list_id = self.list_id

        position = self.position

        value: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.value, GetContentListItemsResponse200ItemValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "listId": list_id,
            "position": position,
            "value": value,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_content_list_items_response_200_item_value_type_1 import GetContentListItemsResponse200ItemValueType1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        list_id = d.pop("listId")

        position = d.pop("position")

        def _parse_value(data: object) -> Union['GetContentListItemsResponse200ItemValueType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = GetContentListItemsResponse200ItemValueType1.from_dict(data)



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
            return cast(Union['GetContentListItemsResponse200ItemValueType1', None, bool, float, list[Any], str], data)

        value = _parse_value(d.pop("value"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_content_list_items_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            list_id=list_id,
            position=position,
            value=value,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_content_list_items_response_200_item

