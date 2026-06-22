from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalNotesBody")



@_attrs_define
class PostPersonalNotesBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            subject_table (Union[None, Unset, str]):
            subject_id (Union[None, Unset, str]):
            title (Union[Unset, str]):
            body (Union[Unset, str]):
            occurred_at (Union[Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    subject_table: Union[None, Unset, str] = UNSET
    subject_id: Union[None, Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    occurred_at: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        subject_table: Union[None, Unset, str]
        if isinstance(self.subject_table, Unset):
            subject_table = UNSET
        else:
            subject_table = self.subject_table

        subject_id: Union[None, Unset, str]
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id

        title = self.title

        body = self.body

        occurred_at = self.occurred_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if subject_table is not UNSET:
            field_dict["subjectTable"] = subject_table
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_subject_table(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_table = _parse_subject_table(d.pop("subjectTable", UNSET))


        def _parse_subject_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))


        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        occurred_at = d.pop("occurredAt", UNSET)

        post_personal_notes_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            subject_table=subject_table,
            subject_id=subject_id,
            title=title,
            body=body,
            occurred_at=occurred_at,
        )

        return post_personal_notes_body

