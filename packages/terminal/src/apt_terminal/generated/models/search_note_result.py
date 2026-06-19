from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchNoteResult")



@_attrs_define
class SearchNoteResult:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            owner_id (str):
            title (str):
            body (str):
            occurred_at (str):
            created_at (str):
            updated_at (str):
            deleted_at (None | str | Unset):
            subject_table (None | str | Unset):
            subject_id (None | str | Unset):
     """

    id: str
    customer_id: str
    owner_id: str
    title: str
    body: str
    occurred_at: str
    created_at: str
    updated_at: str
    deleted_at: None | str | Unset = UNSET
    subject_table: None | str | Unset = UNSET
    subject_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        owner_id = self.owner_id

        title = self.title

        body = self.body

        occurred_at = self.occurred_at

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        subject_table: None | str | Unset
        if isinstance(self.subject_table, Unset):
            subject_table = UNSET
        else:
            subject_table = self.subject_table

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "ownerId": owner_id,
            "title": title,
            "body": body,
            "occurredAt": occurred_at,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if subject_table is not UNSET:
            field_dict["subjectTable"] = subject_table
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        owner_id = d.pop("ownerId")

        title = d.pop("title")

        body = d.pop("body")

        occurred_at = d.pop("occurredAt")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_subject_table(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_table = _parse_subject_table(d.pop("subjectTable", UNSET))


        def _parse_subject_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))


        search_note_result = cls(
            id=id,
            customer_id=customer_id,
            owner_id=owner_id,
            title=title,
            body=body,
            occurred_at=occurred_at,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            subject_table=subject_table,
            subject_id=subject_id,
        )


        search_note_result.additional_properties = d
        return search_note_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
