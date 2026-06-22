from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionRepliesIdBody")



@_attrs_define
class PutCommunityDiscussionRepliesIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            thread_id (Union[Unset, str]):
            parent_reply_id (Union[None, Unset, str]):
            author_id (Union[Unset, str]):
            body (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    parent_reply_id: Union[None, Unset, str] = UNSET
    author_id: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        parent_reply_id: Union[None, Unset, str]
        if isinstance(self.parent_reply_id, Unset):
            parent_reply_id = UNSET
        else:
            parent_reply_id = self.parent_reply_id

        author_id = self.author_id

        body = self.body

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if parent_reply_id is not UNSET:
            field_dict["parentReplyId"] = parent_reply_id
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if body is not UNSET:
            field_dict["body"] = body
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        thread_id = d.pop("threadId", UNSET)

        def _parse_parent_reply_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_reply_id = _parse_parent_reply_id(d.pop("parentReplyId", UNSET))


        author_id = d.pop("authorId", UNSET)

        body = d.pop("body", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        put_community_discussion_replies_id_body = cls(
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            parent_reply_id=parent_reply_id,
            author_id=author_id,
            body=body,
            is_deleted=is_deleted,
        )

        return put_community_discussion_replies_id_body

