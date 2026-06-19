from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetContentQueuesResponse200Item")



@_attrs_define
class GetContentQueuesResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            name (str):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    name: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        name = self.name

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "name": name,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        name = d.pop("name")

        created_at = d.pop("createdAt")

        get_content_queues_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            name=name,
            created_at=created_at,
        )

        return get_content_queues_response_200_item

