from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetPersonalEducationResponse200Item")



@_attrs_define
class GetPersonalEducationResponse200Item:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            ecosystem_id (str):
            institution (str):
            degree (str):
            field_of_study (str):
            start_date (str):
            end_date (Union[None, str]):
            location (str):
            description (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    ecosystem_id: str
    institution: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: Union[None, str]
    location: str
    description: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        institution = self.institution

        degree = self.degree

        field_of_study = self.field_of_study

        start_date = self.start_date

        end_date: Union[None, str]
        end_date = self.end_date

        location = self.location

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ecosystemId": ecosystem_id,
            "institution": institution,
            "degree": degree,
            "fieldOfStudy": field_of_study,
            "startDate": start_date,
            "endDate": end_date,
            "location": location,
            "description": description,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        ecosystem_id = d.pop("ecosystemId")

        institution = d.pop("institution")

        degree = d.pop("degree")

        field_of_study = d.pop("fieldOfStudy")

        start_date = d.pop("startDate")

        def _parse_end_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        end_date = _parse_end_date(d.pop("endDate"))


        location = d.pop("location")

        description = d.pop("description")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_personal_education_response_200_item = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            institution=institution,
            degree=degree,
            field_of_study=field_of_study,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_personal_education_response_200_item

