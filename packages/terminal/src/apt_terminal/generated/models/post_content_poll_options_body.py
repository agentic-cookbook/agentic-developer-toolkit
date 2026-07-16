from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentPollOptionsBody")



@_attrs_define
class PostContentPollOptionsBody:
    """ 
        Attributes:
            poll_id (str):
            text (str):
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            sort_order (Union[Unset, int]):
     """

    poll_id: str
    text: str
    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        poll_id = self.poll_id

        text = self.text

        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "pollId": poll_id,
            "text": text,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        poll_id = d.pop("pollId")

        text = d.pop("text")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        sort_order = d.pop("sortOrder", UNSET)

        post_content_poll_options_body = cls(
            poll_id=poll_id,
            text=text,
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
            sort_order=sort_order,
        )

        return post_content_poll_options_body

