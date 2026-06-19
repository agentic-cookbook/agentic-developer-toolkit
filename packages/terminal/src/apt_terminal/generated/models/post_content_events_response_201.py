from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.post_content_events_response_201_payload_type_1 import PostContentEventsResponse201PayloadType1





T = TypeVar("T", bound="PostContentEventsResponse201")



@_attrs_define
class PostContentEventsResponse201:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (None | str):
            type_ (str):
            payload (bool | float | list[Any] | None | PostContentEventsResponse201PayloadType1 | str):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: None | str
    type_: str
    payload: bool | float | list[Any] | None | PostContentEventsResponse201PayloadType1 | str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_events_response_201_payload_type_1 import PostContentEventsResponse201PayloadType1
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        type_ = self.type_

        payload: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.payload, PostContentEventsResponse201PayloadType1):
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
        from ..models.post_content_events_response_201_payload_type_1 import PostContentEventsResponse201PayloadType1
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

        def _parse_payload(data: object) -> bool | float | list[Any] | None | PostContentEventsResponse201PayloadType1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PostContentEventsResponse201PayloadType1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostContentEventsResponse201PayloadType1 | str, data)

        payload = _parse_payload(d.pop("payload"))


        created_at = d.pop("createdAt")

        post_content_events_response_201 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            type_=type_,
            payload=payload,
            created_at=created_at,
        )

        return post_content_events_response_201

