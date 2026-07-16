from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentPollsBody")



@_attrs_define
class PostContentPollsBody:
    """ 
        Attributes:
            question (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            host_kind (Union[None, Unset, str]):
            host_id (Union[None, Unset, str]):
            allow_multiple (Union[Unset, bool]):
            expires_at (Union[None, Unset, str]):
     """

    question: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    host_kind: Union[None, Unset, str] = UNSET
    host_id: Union[None, Unset, str] = UNSET
    allow_multiple: Union[Unset, bool] = UNSET
    expires_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        question = self.question

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        host_kind: Union[None, Unset, str]
        if isinstance(self.host_kind, Unset):
            host_kind = UNSET
        else:
            host_kind = self.host_kind

        host_id: Union[None, Unset, str]
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        allow_multiple = self.allow_multiple

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question": question,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if host_kind is not UNSET:
            field_dict["hostKind"] = host_kind
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if allow_multiple is not UNSET:
            field_dict["allowMultiple"] = allow_multiple
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        question = d.pop("question")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_host_kind(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host_kind = _parse_host_kind(d.pop("hostKind", UNSET))


        def _parse_host_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host_id = _parse_host_id(d.pop("hostId", UNSET))


        allow_multiple = d.pop("allowMultiple", UNSET)

        def _parse_expires_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        post_content_polls_body = cls(
            question=question,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            host_kind=host_kind,
            host_id=host_id,
            allow_multiple=allow_multiple,
            expires_at=expires_at,
        )

        return post_content_polls_body

