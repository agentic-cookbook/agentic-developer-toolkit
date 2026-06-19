from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PostContentCountersResponse201")



@_attrs_define
class PostContentCountersResponse201:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            name (str):
            value (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    name: str
    value: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        name = self.name

        value = self.value

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "name": name,
            "value": value,
            "createdAt": created_at,
            "updatedAt": updated_at,
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

        value = d.pop("value")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_content_counters_response_201 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            name=name,
            value=value,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_content_counters_response_201

