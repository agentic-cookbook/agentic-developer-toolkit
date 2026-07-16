from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetContentListsIdResponse200")



@_attrs_define
class GetContentListsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            name (str):
            description (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    customer_id: str
    deleted_at: Union[None, str]
    name: str
    description: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        name = self.name

        description: Union[None, str]
        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "name": name,
            "description": description,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_content_lists_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_content_lists_id_response_200

