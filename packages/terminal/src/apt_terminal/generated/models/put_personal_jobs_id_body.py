from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonalJobsIdBody")



@_attrs_define
class PutPersonalJobsIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            company (str | Unset):
            role (str | Unset):
            start_date (str | Unset):
            end_date (None | str | Unset):
            location (str | Unset):
            description (str | Unset):
            is_current (bool | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    company: str | Unset = UNSET
    role: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    location: str | Unset = UNSET
    description: str | Unset = UNSET
    is_current: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        company = self.company

        role = self.role

        start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        location = self.location

        description = self.description

        is_current = self.is_current


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if company is not UNSET:
            field_dict["company"] = company
        if role is not UNSET:
            field_dict["role"] = role
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if location is not UNSET:
            field_dict["location"] = location
        if description is not UNSET:
            field_dict["description"] = description
        if is_current is not UNSET:
            field_dict["isCurrent"] = is_current

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

        company = d.pop("company", UNSET)

        role = d.pop("role", UNSET)

        start_date = d.pop("startDate", UNSET)

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        location = d.pop("location", UNSET)

        description = d.pop("description", UNSET)

        is_current = d.pop("isCurrent", UNSET)

        put_personal_jobs_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            company=company,
            role=role,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
            is_current=is_current,
        )

        return put_personal_jobs_id_body

