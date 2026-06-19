from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PostPersonalRelationshipsResponse201")



@_attrs_define
class PostPersonalRelationshipsResponse201:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
            contact_id (str):
            relationship_kind (str):
            since_date (str):
            notes (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: None | str
    owner_id: str
    contact_id: str
    relationship_kind: str
    since_date: str
    notes: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        contact_id = self.contact_id

        relationship_kind = self.relationship_kind

        since_date = self.since_date

        notes = self.notes

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "contactId": contact_id,
            "relationshipKind": relationship_kind,
            "sinceDate": since_date,
            "notes": notes,
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

        contact_id = d.pop("contactId")

        relationship_kind = d.pop("relationshipKind")

        since_date = d.pop("sinceDate")

        notes = d.pop("notes")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_personal_relationships_response_201 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            contact_id=contact_id,
            relationship_kind=relationship_kind,
            since_date=since_date,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_personal_relationships_response_201

