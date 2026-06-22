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
  from ..models.post_content_events_body_payload_type_1 import PostContentEventsBodyPayloadType1





T = TypeVar("T", bound="PostContentEventsBody")



@_attrs_define
class PostContentEventsBody:
    """ 
        Attributes:
            type_ (str):
            payload (Union['PostContentEventsBodyPayloadType1', None, bool, float, list[Any], str]):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    type_: str
    payload: Union['PostContentEventsBodyPayloadType1', None, bool, float, list[Any], str]
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_events_body_payload_type_1 import PostContentEventsBodyPayloadType1
        type_ = self.type_

        payload: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.payload, PostContentEventsBodyPayloadType1):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, list):
            payload = self.payload


        else:
            payload = self.payload

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "payload": payload,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_content_events_body_payload_type_1 import PostContentEventsBodyPayloadType1
        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_payload(data: object) -> Union['PostContentEventsBodyPayloadType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_1 = PostContentEventsBodyPayloadType1.from_dict(data)



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
            return cast(Union['PostContentEventsBodyPayloadType1', None, bool, float, list[Any], str], data)

        payload = _parse_payload(d.pop("payload"))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_content_events_body = cls(
            type_=type_,
            payload=payload,
            owner_id=owner_id,
            deleted_at=deleted_at,
        )

        return post_content_events_body

