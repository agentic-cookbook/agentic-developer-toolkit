from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutCommunityDiscussionPollsIdBody")



@_attrs_define
class PutCommunityDiscussionPollsIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            thread_id (str | Unset):
            question (str | Unset):
            allow_multiple (bool | Unset):
            expires_at (None | str | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    thread_id: str | Unset = UNSET
    question: str | Unset = UNSET
    allow_multiple: bool | Unset = UNSET
    expires_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        thread_id = self.thread_id

        question = self.question

        allow_multiple = self.allow_multiple

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if question is not UNSET:
            field_dict["question"] = question
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        thread_id = d.pop("threadId", UNSET)

        question = d.pop("question", UNSET)

        allow_multiple = d.pop("allowMultiple", UNSET)

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        put_community_discussion_polls_id_body = cls(
            ecosystem_id=ecosystem_id,
            thread_id=thread_id,
            question=question,
            allow_multiple=allow_multiple,
            expires_at=expires_at,
        )

        return put_community_discussion_polls_id_body

