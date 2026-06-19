from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostCommunityDiscussionPollsBody")



@_attrs_define
class PostCommunityDiscussionPollsBody:
    """ 
        Attributes:
            thread_id (str):
            question (str):
            ecosystem_id (str | Unset):
            allow_multiple (bool | Unset):
            expires_at (None | str | Unset):
     """

    thread_id: str
    question: str
    ecosystem_id: str | Unset = UNSET
    allow_multiple: bool | Unset = UNSET
    expires_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        question = self.question

        ecosystem_id = self.ecosystem_id

        allow_multiple = self.allow_multiple

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "threadId": thread_id,
            "question": question,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = d.pop("threadId")

        question = d.pop("question")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        allow_multiple = d.pop("allowMultiple", UNSET)

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        post_community_discussion_polls_body = cls(
            thread_id=thread_id,
            question=question,
            ecosystem_id=ecosystem_id,
            allow_multiple=allow_multiple,
            expires_at=expires_at,
        )

        return post_community_discussion_polls_body

