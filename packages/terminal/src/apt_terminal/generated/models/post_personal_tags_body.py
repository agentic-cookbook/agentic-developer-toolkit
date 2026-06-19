from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostPersonalTagsBody")



@_attrs_define
class PostPersonalTagsBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            kind (str | Unset):
            label (str | Unset):
            level (str | Unset):
            since_date (str | Unset):
            notes (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    kind: str | Unset = UNSET
    label: str | Unset = UNSET
    level: str | Unset = UNSET
    since_date: str | Unset = UNSET
    notes: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        kind = self.kind

        label = self.label

        level = self.level

        since_date = self.since_date

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if level is not UNSET:
            field_dict["level"] = level
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

        kind = d.pop("kind", UNSET)

        label = d.pop("label", UNSET)

        level = d.pop("level", UNSET)

        since_date = d.pop("sinceDate", UNSET)

        notes = d.pop("notes", UNSET)

        post_personal_tags_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            kind=kind,
            label=label,
            level=level,
            since_date=since_date,
            notes=notes,
        )

        return post_personal_tags_body

