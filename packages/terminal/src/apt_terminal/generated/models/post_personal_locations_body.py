from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalLocationsBody")



@_attrs_define
class PostPersonalLocationsBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            place (Union[Unset, str]):
            region (Union[Unset, str]):
            country (Union[Unset, str]):
            start_date (Union[Unset, str]):
            end_date (Union[None, Unset, str]):
            notes (Union[Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    place: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[None, Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        place = self.place

        region = self.region

        country = self.country

        start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if place is not UNSET:
            field_dict["place"] = place
        if region is not UNSET:
            field_dict["region"] = region
        if country is not UNSET:
            field_dict["country"] = country
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
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


        owner_id = d.pop("ownerId", UNSET)

        place = d.pop("place", UNSET)

        region = d.pop("region", UNSET)

        country = d.pop("country", UNSET)

        start_date = d.pop("startDate", UNSET)

        def _parse_end_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        notes = d.pop("notes", UNSET)

        post_personal_locations_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            place=place,
            region=region,
            country=country,
            start_date=start_date,
            end_date=end_date,
            notes=notes,
        )

        return post_personal_locations_body

