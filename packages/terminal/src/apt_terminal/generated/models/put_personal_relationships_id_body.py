from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonalRelationshipsIdBody")



@_attrs_define
class PutPersonalRelationshipsIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            contact_id (str | Unset):
            relationship_kind (str | Unset):
            since_date (str | Unset):
            notes (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    contact_id: str | Unset = UNSET
    relationship_kind: str | Unset = UNSET
    since_date: str | Unset = UNSET
    notes: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        contact_id = self.contact_id

        relationship_kind = self.relationship_kind

        since_date = self.since_date

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if relationship_kind is not UNSET:
            field_dict["relationshipKind"] = relationship_kind
        if since_date is not UNSET:
            field_dict["sinceDate"] = since_date
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

        contact_id = d.pop("contactId", UNSET)

        relationship_kind = d.pop("relationshipKind", UNSET)

        since_date = d.pop("sinceDate", UNSET)

        notes = d.pop("notes", UNSET)

        put_personal_relationships_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            contact_id=contact_id,
            relationship_kind=relationship_kind,
            since_date=since_date,
            notes=notes,
        )

        return put_personal_relationships_id_body

