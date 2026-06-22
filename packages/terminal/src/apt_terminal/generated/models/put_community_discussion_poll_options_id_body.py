from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionPollOptionsIdBody")



@_attrs_define
class PutCommunityDiscussionPollOptionsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            poll_id (Union[Unset, str]):
            text (Union[Unset, str]):
            display_order (Union[Unset, int]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    poll_id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        poll_id = self.poll_id

        text = self.text

        display_order = self.display_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if poll_id is not UNSET:
            field_dict["pollId"] = poll_id
        if text is not UNSET:
            field_dict["text"] = text
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        poll_id = d.pop("pollId", UNSET)

        text = d.pop("text", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        put_community_discussion_poll_options_id_body = cls(
            ecosystem_id=ecosystem_id,
            poll_id=poll_id,
            text=text,
            display_order=display_order,
        )

        return put_community_discussion_poll_options_id_body

