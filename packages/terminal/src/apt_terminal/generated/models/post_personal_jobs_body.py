from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalJobsBody")



@_attrs_define
class PostPersonalJobsBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            company (Union[Unset, str]):
            role (Union[Unset, str]):
            start_date (Union[Unset, str]):
            end_date (Union[None, Unset, str]):
            location (Union[Unset, str]):
            description (Union[Unset, str]):
            is_current (Union[Unset, bool]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_current: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        company = self.company

        role = self.role

        start_date = self.start_date

        end_date: Union[None, Unset, str]
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
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        company = d.pop("company", UNSET)

        role = d.pop("role", UNSET)

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

        is_current = d.pop("isCurrent", UNSET)

        post_personal_jobs_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            company=company,
            role=role,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
            is_current=is_current,
        )

        return post_personal_jobs_body

