from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentDatesIdBody")



@_attrs_define
class PutContentDatesIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            owner_kind (Union[Unset, str]):
            owner_id (Union[Unset, str]):
            label (Union[Unset, str]):
            date (Union[Unset, str]):
            recurrence (Union[Unset, str]):
            contact_id (Union[None, Unset, str]):
            notes (Union[Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    owner_kind: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    recurrence: Union[Unset, str] = UNSET
    contact_id: Union[None, Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        owner_kind = self.owner_kind

        owner_id = self.owner_id

        label = self.label

        date = self.date

        recurrence = self.recurrence

        contact_id: Union[None, Unset, str]
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
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if owner_kind is not UNSET:
            field_dict["ownerKind"] = owner_kind
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
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        owner_kind = d.pop("ownerKind", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        label = d.pop("label", UNSET)

        date = d.pop("date", UNSET)

        recurrence = d.pop("recurrence", UNSET)

        def _parse_contact_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contact_id = _parse_contact_id(d.pop("contactId", UNSET))


        notes = d.pop("notes", UNSET)

        put_content_dates_id_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            owner_kind=owner_kind,
            owner_id=owner_id,
            label=label,
            date=date,
            recurrence=recurrence,
            contact_id=contact_id,
            notes=notes,
        )

        return put_content_dates_id_body

