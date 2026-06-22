from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetCommunityDiscussionPollsResponse200Item")



@_attrs_define
class GetCommunityDiscussionPollsResponse200Item:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            thread_id (str):
            question (str):
            allow_multiple (bool):
            expires_at (Union[None, str]):
            created_at (str):
     """

    id: str
    ecosystem_id: str
    thread_id: str
    question: str
    allow_multiple: bool
    expires_at: Union[None, str]
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        question = self.question

        allow_multiple = self.allow_multiple

        expires_at: Union[None, str]
        expires_at = self.expires_at

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "threadId": thread_id,
            "question": question,
            "allowMultiple": allow_multiple,
            "expiresAt": expires_at,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        thread_id = d.pop("threadId")

        question = d.pop("question")

        allow_multiple = d.pop("allowMultiple")

        def _parse_expires_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        created_at = d.pop("createdAt")

        get_community_discussion_polls_response_200_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            question=question,
            allow_multiple=allow_multiple,
            expires_at=expires_at,
            created_at=created_at,
        )

        return get_community_discussion_polls_response_200_item

