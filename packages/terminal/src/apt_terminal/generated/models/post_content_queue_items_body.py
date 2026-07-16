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
  from ..models.post_content_queue_items_body_payload_type_1 import PostContentQueueItemsBodyPayloadType1





T = TypeVar("T", bound="PostContentQueueItemsBody")



@_attrs_define
class PostContentQueueItemsBody:
    """ 
        Attributes:
            queue_id (str):
            payload (Union['PostContentQueueItemsBodyPayloadType1', None, bool, float, list[Any], str]):
            status (str):
            enqueued_at (str):
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            dequeued_at (Union[None, Unset, str]):
            acked_at (Union[None, Unset, str]):
            nacked_at (Union[None, Unset, str]):
     """

    queue_id: str
    payload: Union['PostContentQueueItemsBodyPayloadType1', None, bool, float, list[Any], str]
    status: str
    enqueued_at: str
    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    dequeued_at: Union[None, Unset, str] = UNSET
    acked_at: Union[None, Unset, str] = UNSET
    nacked_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_queue_items_body_payload_type_1 import PostContentQueueItemsBodyPayloadType1
        queue_id = self.queue_id

        payload: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.payload, PostContentQueueItemsBodyPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        status = self.status

        enqueued_at = self.enqueued_at

        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

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
            "queueId": queue_id,
            "payload": payload,
            "status": status,
            "enqueuedAt": enqueued_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if dequeued_at is not UNSET:
            field_dict["dequeuedAt"] = dequeued_at
        if acked_at is not UNSET:
            field_dict["ackedAt"] = acked_at
        if nacked_at is not UNSET:
            field_dict["nackedAt"] = nacked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_content_queue_items_body_payload_type_1 import PostContentQueueItemsBodyPayloadType1
        d = dict(src_dict)
        queue_id = d.pop("queueId")

        def _parse_payload(data: object) -> Union['PostContentQueueItemsBodyPayloadType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PostContentQueueItemsBodyPayloadType1.from_dict(data)



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
            return cast(Union['PostContentQueueItemsBodyPayloadType1', None, bool, float, list[Any], str], data)

        payload = _parse_payload(d.pop("payload"))


        status = d.pop("status")

        enqueued_at = d.pop("enqueuedAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


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


        post_content_queue_items_body = cls(
            queue_id=queue_id,
            payload=payload,
            status=status,
            enqueued_at=enqueued_at,
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
            dequeued_at=dequeued_at,
            acked_at=acked_at,
            nacked_at=nacked_at,
        )

        return post_content_queue_items_body

