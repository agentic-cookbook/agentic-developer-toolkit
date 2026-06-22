from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalRelationshipsBody")



@_attrs_define
class PostPersonalRelationshipsBody:
    """ 
        Attributes:
            contact_id (str):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            relationship_kind (Union[Unset, str]):
            since_date (Union[Unset, str]):
            notes (Union[Unset, str]):
     """

    contact_id: str
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    relationship_kind: Union[Unset, str] = UNSET
    since_date: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        contact_id = self.contact_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        relationship_kind = self.relationship_kind

        since_date = self.since_date

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "contactId": contact_id,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
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
        contact_id = d.pop("contactId")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        relationship_kind = d.pop("relationshipKind", UNSET)

        since_date = d.pop("sinceDate", UNSET)

        notes = d.pop("notes", UNSET)

        post_personal_relationships_body = cls(
            contact_id=contact_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            relationship_kind=relationship_kind,
            since_date=since_date,
            notes=notes,
        )

        return post_personal_relationships_body

