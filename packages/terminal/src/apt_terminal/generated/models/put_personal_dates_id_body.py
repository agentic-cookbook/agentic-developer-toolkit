from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonalDatesIdBody")



@_attrs_define
class PutPersonalDatesIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            label (str | Unset):
            date (str | Unset):
            recurrence (str | Unset):
            contact_id (None | str | Unset):
            notes (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    label: str | Unset = UNSET
    date: str | Unset = UNSET
    recurrence: str | Unset = UNSET
    contact_id: None | str | Unset = UNSET
    notes: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        label = self.label

        date = self.date

        recurrence = self.recurrence

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if label is not UNSET:
            field_dict["label"] = label
        if date is not UNSET:
            field_dict["date"] = date
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        label = d.pop("label", UNSET)

        date = d.pop("date", UNSET)

        recurrence = d.pop("recurrence", UNSET)

        def _parse_contact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_id = _parse_contact_id(d.pop("contactId", UNSET))


        notes = d.pop("notes", UNSET)

        put_personal_dates_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            label=label,
            date=date,
            recurrence=recurrence,
            contact_id=contact_id,
            notes=notes,
        )

        return put_personal_dates_id_body

