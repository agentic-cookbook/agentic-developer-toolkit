from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_content_queue_items_response_200_item_payload_type_1 import GetContentQueueItemsResponse200ItemPayloadType1





T = TypeVar("T", bound="GetContentQueueItemsResponse200Item")



@_attrs_define
class GetContentQueueItemsResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            queue_id (str):
            payload (bool | float | GetContentQueueItemsResponse200ItemPayloadType1 | list[Any] | None | str):
            status (str):
            enqueued_at (str):
            dequeued_at (None | str):
            acked_at (None | str):
            nacked_at (None | str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    queue_id: str
    payload: bool | float | GetContentQueueItemsResponse200ItemPayloadType1 | list[Any] | None | str
    status: str
    enqueued_at: str
    dequeued_at: None | str
    acked_at: None | str
    nacked_at: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_content_queue_items_response_200_item_payload_type_1 import GetContentQueueItemsResponse200ItemPayloadType1
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        queue_id = self.queue_id

        payload: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.payload, GetContentQueueItemsResponse200ItemPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        status = self.status

        enqueued_at = self.enqueued_at

        dequeued_at: None | str
        dequeued_at = self.dequeued_at

        acked_at: None | str
        acked_at = self.acked_at

        nacked_at: None | str
        nacked_at = self.nacked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "queueId": queue_id,
            "payload": payload,
            "status": status,
            "enqueuedAt": enqueued_at,
            "dequeuedAt": dequeued_at,
            "ackedAt": acked_at,
            "nackedAt": nacked_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_content_queue_items_response_200_item_payload_type_1 import GetContentQueueItemsResponse200ItemPayloadType1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        queue_id = d.pop("queueId")

        def _parse_payload(data: object) -> bool | float | GetContentQueueItemsResponse200ItemPayloadType1 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = GetContentQueueItemsResponse200ItemPayloadType1.from_dict(data)



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
            return cast(bool | float | GetContentQueueItemsResponse200ItemPayloadType1 | list[Any] | None | str, data)

        payload = _parse_payload(d.pop("payload"))


        status = d.pop("status")

        enqueued_at = d.pop("enqueuedAt")

        def _parse_dequeued_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dequeued_at = _parse_dequeued_at(d.pop("dequeuedAt"))


        def _parse_acked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acked_at = _parse_acked_at(d.pop("ackedAt"))


        def _parse_nacked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        nacked_at = _parse_nacked_at(d.pop("nackedAt"))


        get_content_queue_items_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            queue_id=queue_id,
            payload=payload,
            status=status,
            enqueued_at=enqueued_at,
            dequeued_at=dequeued_at,
            acked_at=acked_at,
            nacked_at=nacked_at,
        )

        return get_content_queue_items_response_200_item

