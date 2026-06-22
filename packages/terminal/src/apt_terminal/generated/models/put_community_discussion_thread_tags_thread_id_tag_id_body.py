from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionThreadTagsThreadIdTagIdBody")



@_attrs_define
class PutCommunityDiscussionThreadTagsThreadIdTagIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            thread_id (Union[Unset, str]):
            tag_id (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    tag_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        tag_id = self.tag_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if tag_id is not UNSET:
            field_dict["tagId"] = tag_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        thread_id = d.pop("threadId", UNSET)

        tag_id = d.pop("tagId", UNSET)

        put_community_discussion_thread_tags_thread_id_tag_id_body = cls(
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            tag_id=tag_id,
        )

        return put_community_discussion_thread_tags_thread_id_tag_id_body

