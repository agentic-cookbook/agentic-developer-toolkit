from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetPersonalSocialLinksIdResponse200")



@_attrs_define
class GetPersonalSocialLinksIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            platform (str):
            url (str):
            handle (str):
            sort_order (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    platform: str
    url: str
    handle: str
    sort_order: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        platform = self.platform

        url = self.url

        handle = self.handle

        sort_order = self.sort_order

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "platform": platform,
            "url": url,
            "handle": handle,
            "sortOrder": sort_order,
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

        platform = d.pop("platform")

        url = d.pop("url")

        handle = d.pop("handle")

        sort_order = d.pop("sortOrder")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_personal_social_links_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            platform=platform,
            url=url,
            handle=handle,
            sort_order=sort_order,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_personal_social_links_id_response_200

