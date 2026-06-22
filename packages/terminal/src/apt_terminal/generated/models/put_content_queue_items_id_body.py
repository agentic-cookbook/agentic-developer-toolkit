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
  from ..models.put_content_queue_items_id_body_payload_type_1 import PutContentQueueItemsIdBodyPayloadType1





T = TypeVar("T", bound="PutContentQueueItemsIdBody")



@_attrs_define
class PutContentQueueItemsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            queue_id (Union[Unset, str]):
            payload (Union['PutContentQueueItemsIdBodyPayloadType1', None, Unset, bool, float, list[Any], str]):
            status (Union[Unset, str]):
            enqueued_at (Union[Unset, str]):
            dequeued_at (Union[None, Unset, str]):
            acked_at (Union[None, Unset, str]):
            nacked_at (Union[None, Unset, str]):
     """

    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    queue_id: Union[Unset, str] = UNSET
    payload: Union['PutContentQueueItemsIdBodyPayloadType1', None, Unset, bool, float, list[Any], str] = UNSET
    status: Union[Unset, str] = UNSET
    enqueued_at: Union[Unset, str] = UNSET
    dequeued_at: Union[None, Unset, str] = UNSET
    acked_at: Union[None, Unset, str] = UNSET
    nacked_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_queue_items_id_body_payload_type_1 import PutContentQueueItemsIdBodyPayloadType1
        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        queue_id = self.queue_id

        payload: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, PutContentQueueItemsIdBodyPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        status = self.status

        enqueued_at = self.enqueued_at

        dequeued_at: Union[None, Unset, str]
        if isinstance(self.dequeued_at, Unset):
            dequeued_at = UNSET
        else:
            dequeued_at = self.dequeued_at

        acked_at: Union[None, Unset, str]
        if isinstance(self.acked_at, Unset):
            acked_at = UNSET
        else:
            acked_at = self.acked_at

        nacked_at: Union[None, Unset, str]
        if isinstance(self.nacked_at, Unset):
            nacked_at = UNSET
        else:
            nacked_at = self.nacked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if queue_id is not UNSET:
            field_dict["queueId"] = queue_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if status is not UNSET:
            field_dict["status"] = status
        if enqueued_at is not UNSET:
            field_dict["enqueuedAt"] = enqueued_at
        if dequeued_at is not UNSET:
            field_dict["dequeuedAt"] = dequeued_at
        if acked_at is not UNSET:
            field_dict["ackedAt"] = acked_at
        if nacked_at is not UNSET:
            field_dict["nackedAt"] = nacked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_content_queue_items_id_body_payload_type_1 import PutContentQueueItemsIdBodyPayloadType1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        queue_id = d.pop("queueId", UNSET)

        def _parse_payload(data: object) -> Union['PutContentQueueItemsIdBodyPayloadType1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PutContentQueueItemsIdBodyPayloadType1.from_dict(data)



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
            return cast(Union['PutContentQueueItemsIdBodyPayloadType1', None, Unset, bool, float, list[Any], str], data)

        payload = _parse_payload(d.pop("payload", UNSET))


        status = d.pop("status", UNSET)

        enqueued_at = d.pop("enqueuedAt", UNSET)

        def _parse_dequeued_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dequeued_at = _parse_dequeued_at(d.pop("dequeuedAt", UNSET))


        def _parse_acked_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acked_at = _parse_acked_at(d.pop("ackedAt", UNSET))


        def _parse_nacked_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nacked_at = _parse_nacked_at(d.pop("nackedAt", UNSET))


        put_content_queue_items_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            queue_id=queue_id,
            payload=payload,
            status=status,
            enqueued_at=enqueued_at,
            dequeued_at=dequeued_at,
            acked_at=acked_at,
            nacked_at=nacked_at,
        )

        return put_content_queue_items_id_body

