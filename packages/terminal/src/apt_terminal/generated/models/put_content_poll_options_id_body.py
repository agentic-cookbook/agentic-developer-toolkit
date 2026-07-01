from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentPollOptionsIdBody")



@_attrs_define
class PutContentPollOptionsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            poll_id (Union[Unset, str]):
            text (Union[Unset, str]):
            sort_order (Union[Unset, int]):
     """

    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    poll_id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        poll_id = self.poll_id

        text = self.text

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if poll_id is not UNSET:
            field_dict["pollId"] = poll_id
        if text is not UNSET:
            field_dict["text"] = text
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        poll_id = d.pop("pollId", UNSET)

        text = d.pop("text", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        put_content_poll_options_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            poll_id=poll_id,
            text=text,
            sort_order=sort_order,
        )

        return put_content_poll_options_id_body

