from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.put_content_queue_items_id_response_200_payload_type_1 import PutContentQueueItemsIdResponse200PayloadType1





T = TypeVar("T", bound="PutContentQueueItemsIdResponse200")



@_attrs_define
class PutContentQueueItemsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            queue_id (str):
            payload (Union['PutContentQueueItemsIdResponse200PayloadType1', None, bool, float, list[Any], str]):
            status (str):
            enqueued_at (str):
            dequeued_at (Union[None, str]):
            acked_at (Union[None, str]):
            nacked_at (Union[None, str]):
     """

    id: str
    ecosystem_id: str
    customer_id: str
    deleted_at: Union[None, str]
    queue_id: str
    payload: Union['PutContentQueueItemsIdResponse200PayloadType1', None, bool, float, list[Any], str]
    status: str
    enqueued_at: str
    dequeued_at: Union[None, str]
    acked_at: Union[None, str]
    nacked_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_queue_items_id_response_200_payload_type_1 import PutContentQueueItemsIdResponse200PayloadType1
        id = self.id

        ecosystem_id = self.ecosystem_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        queue_id = self.queue_id

        payload: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.payload, PutContentQueueItemsIdResponse200PayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        status = self.status

        enqueued_at = self.enqueued_at

        dequeued_at: Union[None, str]
        dequeued_at = self.dequeued_at

        acked_at: Union[None, str]
        acked_at = self.acked_at

        nacked_at: Union[None, str]
        nacked_at = self.nacked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
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
        from ..models.put_content_queue_items_id_response_200_payload_type_1 import PutContentQueueItemsIdResponse200PayloadType1
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        queue_id = d.pop("queueId")

        def _parse_payload(data: object) -> Union['PutContentQueueItemsIdResponse200PayloadType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PutContentQueueItemsIdResponse200PayloadType1.from_dict(data)



                return payload_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payload_type_2 = cast(list[Any], data)

                return payload_type_2
            except: # noqa: E722
                pass
            return cast(Union['PutContentQueueItemsIdResponse200PayloadType1', None, bool, float, list[Any], str], data)

        payload = _parse_payload(d.pop("payload"))


        status = d.pop("status")

        enqueued_at = d.pop("enqueuedAt")

        def _parse_dequeued_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        dequeued_at = _parse_dequeued_at(d.pop("dequeuedAt"))


        def _parse_acked_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        acked_at = _parse_acked_at(d.pop("ackedAt"))


        def _parse_nacked_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        nacked_at = _parse_nacked_at(d.pop("nackedAt"))


        put_content_queue_items_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
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

        return put_content_queue_items_id_response_200

