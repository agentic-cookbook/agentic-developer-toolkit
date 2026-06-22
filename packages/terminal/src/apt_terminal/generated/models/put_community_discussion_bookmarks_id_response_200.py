from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutCommunityDiscussionBookmarksIdResponse200")



@_attrs_define
class PutCommunityDiscussionBookmarksIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (str):
            ecosystem_id (str):
            thread_id (str):
            created_at (str):
     """

    id: str
    user_id: str
    ecosystem_id: str
    thread_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "threadId": thread_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        thread_id = d.pop("threadId")

        created_at = d.pop("createdAt")

        put_community_discussion_bookmarks_id_response_200 = cls(
            id=id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            created_at=created_at,
        )

        return put_community_discussion_bookmarks_id_response_200

