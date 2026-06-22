from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutCommunityDiscussionPollOptionsIdResponse200")



@_attrs_define
class PutCommunityDiscussionPollOptionsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            poll_id (str):
            text (str):
            display_order (int):
     """

    id: str
    ecosystem_id: str
    poll_id: str
    text: str
    display_order: int





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        poll_id = self.poll_id

        text = self.text

        display_order = self.display_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "pollId": poll_id,
            "text": text,
            "displayOrder": display_order,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        poll_id = d.pop("pollId")

        text = d.pop("text")

        display_order = d.pop("displayOrder")

        put_community_discussion_poll_options_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            poll_id=poll_id,
            text=text,
            display_order=display_order,
        )

        return put_community_discussion_poll_options_id_response_200

