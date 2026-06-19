from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutPersonalEducationIdBody")



@_attrs_define
class PutPersonalEducationIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            institution (str | Unset):
            degree (str | Unset):
            field_of_study (str | Unset):
            start_date (str | Unset):
            end_date (None | str | Unset):
            location (str | Unset):
            description (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    institution: str | Unset = UNSET
    degree: str | Unset = UNSET
    field_of_study: str | Unset = UNSET
    start_date: str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    location: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        institution = self.institution

        degree = self.degree

        field_of_study = self.field_of_study

        start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        location = self.location

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if institution is not UNSET:
            field_dict["institution"] = institution
        if degree is not UNSET:
            field_dict["degree"] = degree
        if field_of_study is not UNSET:
            field_dict["fieldOfStudy"] = field_of_study
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if location is not UNSET:
            field_dict["location"] = location
        if description is not UNSET:
            field_dict["description"] = description

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

        institution = d.pop("institution", UNSET)

        degree = d.pop("degree", UNSET)

        field_of_study = d.pop("fieldOfStudy", UNSET)

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

        put_personal_education_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            institution=institution,
            degree=degree,
            field_of_study=field_of_study,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
        )

        return put_personal_education_id_body

