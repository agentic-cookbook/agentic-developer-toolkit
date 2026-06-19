from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_content_events_id_body_payload_type_1 import PutContentEventsIdBodyPayloadType1





T = TypeVar("T", bound="PutContentEventsIdBody")



@_attrs_define
class PutContentEventsIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            type_ (str | Unset):
            payload (bool | float | list[Any] | None | PutContentEventsIdBodyPayloadType1 | str | Unset):
     """

    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    type_: str | Unset = UNSET
    payload: bool | float | list[Any] | None | PutContentEventsIdBodyPayloadType1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_events_id_body_payload_type_1 import PutContentEventsIdBodyPayloadType1
        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        type_ = self.type_

        payload: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, PutContentEventsIdBodyPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_content_events_id_body_payload_type_1 import PutContentEventsIdBodyPayloadType1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        type_ = d.pop("type", UNSET)

        def _parse_payload(data: object) -> bool | float | list[Any] | None | PutContentEventsIdBodyPayloadType1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PutContentEventsIdBodyPayloadType1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PutContentEventsIdBodyPayloadType1 | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))


        put_content_events_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            type_=type_,
            payload=payload,
        )

        return put_content_events_id_body

