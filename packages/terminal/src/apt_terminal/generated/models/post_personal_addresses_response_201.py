from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostPersonalAddressesResponse201")



@_attrs_define
class PostPersonalAddressesResponse201:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            label (str):
            line1 (str):
            line2 (str):
            city (str):
            region (str):
            postal_code (str):
            country (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    label: str
    line1: str
    line2: str
    city: str
    region: str
    postal_code: str
    country: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        label = self.label

        line1 = self.line1

        line2 = self.line2

        city = self.city

        region = self.region

        postal_code = self.postal_code

        country = self.country

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "label": label,
            "line1": line1,
            "line2": line2,
            "city": city,
            "region": region,
            "postalCode": postal_code,
            "country": country,
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


        owner_id = d.pop("ownerId")

        label = d.pop("label")

        line1 = d.pop("line1")

        line2 = d.pop("line2")

        city = d.pop("city")

        region = d.pop("region")

        postal_code = d.pop("postalCode")

        country = d.pop("country")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_personal_addresses_response_201 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            label=label,
            line1=line1,
            line2=line2,
            city=city,
            region=region,
            postal_code=postal_code,
            country=country,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_personal_addresses_response_201

