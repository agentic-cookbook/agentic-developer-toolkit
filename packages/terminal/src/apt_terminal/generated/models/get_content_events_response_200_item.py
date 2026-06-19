from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_content_events_response_200_item_payload_type_1 import GetContentEventsResponse200ItemPayloadType1





T = TypeVar("T", bound="GetContentEventsResponse200Item")



@_attrs_define
class GetContentEventsResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            type_ (str):
            payload (bool | float | GetContentEventsResponse200ItemPayloadType1 | list[Any] | None | str):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    type_: str
    payload: bool | float | GetContentEventsResponse200ItemPayloadType1 | list[Any] | None | str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_content_events_response_200_item_payload_type_1 import GetContentEventsResponse200ItemPayloadType1
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        type_ = self.type_

        payload: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.payload, GetContentEventsResponse200ItemPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "type": type_,
            "payload": payload,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_content_events_response_200_item_payload_type_1 import GetContentEventsResponse200ItemPayloadType1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        type_ = d.pop("type")

        def _parse_payload(data: object) -> bool | float | GetContentEventsResponse200ItemPayloadType1 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = GetContentEventsResponse200ItemPayloadType1.from_dict(data)



                return payload_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payload_type_2 = cast(list[Any], data)

                return payload_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetContentEventsResponse200ItemPayloadType1 | list[Any] | None | str, data)

        payload = _parse_payload(d.pop("payload"))


        created_at = d.pop("createdAt")

        get_content_events_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            type_=type_,
            payload=payload,
            created_at=created_at,
        )

        return get_content_events_response_200_item

