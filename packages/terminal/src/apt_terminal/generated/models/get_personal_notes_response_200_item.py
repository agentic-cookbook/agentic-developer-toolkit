from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetPersonalNotesResponse200Item")



@_attrs_define
class GetPersonalNotesResponse200Item:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
            subject_table (None | str):
            subject_id (None | str):
            title (str):
            body (str):
            occurred_at (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: None | str
    owner_id: str
    subject_table: None | str
    subject_id: None | str
    title: str
    body: str
    occurred_at: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        subject_table: None | str
        subject_table = self.subject_table

        subject_id: None | str
        subject_id = self.subject_id

        title = self.title

        body = self.body

        occurred_at = self.occurred_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "subjectTable": subject_table,
            "subjectId": subject_id,
            "title": title,
            "body": body,
            "occurredAt": occurred_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        def _parse_subject_table(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject_table = _parse_subject_table(d.pop("subjectTable"))


        def _parse_subject_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject_id = _parse_subject_id(d.pop("subjectId"))


        title = d.pop("title")

        body = d.pop("body")

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_personal_notes_response_200_item = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            subject_table=subject_table,
            subject_id=subject_id,
            title=title,
            body=body,
            occurred_at=occurred_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_personal_notes_response_200_item

