from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalEducationBody")



@_attrs_define
class PostPersonalEducationBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            institution (Union[Unset, str]):
            degree (Union[Unset, str]):
            field_of_study (Union[Unset, str]):
            start_date (Union[Unset, str]):
            end_date (Union[None, Unset, str]):
            location (Union[Unset, str]):
            description (Union[Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    institution: Union[Unset, str] = UNSET
    degree: Union[Unset, str] = UNSET
    field_of_study: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        institution = self.institution

        degree = self.degree

        field_of_study = self.field_of_study

        start_date = self.start_date

        end_date: Union[None, Unset, str]
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
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        institution = d.pop("institution", UNSET)

        degree = d.pop("degree", UNSET)

        field_of_study = d.pop("fieldOfStudy", UNSET)

        start_date = d.pop("startDate", UNSET)

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        location = d.pop("location", UNSET)

        description = d.pop("description", UNSET)

        post_personal_education_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            institution=institution,
            degree=degree,
            field_of_study=field_of_study,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
        )

        return post_personal_education_body

