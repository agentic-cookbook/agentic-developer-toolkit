from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutPersonalPrivacyGrantsIdResponse200")



@_attrs_define
class PutPersonalPrivacyGrantsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            target_table (str):
            target_id (str):
            audience_mask (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    target_table: str
    target_id: str
    audience_mask: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        target_table = self.target_table

        target_id = self.target_id

        audience_mask = self.audience_mask

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "targetTable": target_table,
            "targetId": target_id,
            "audienceMask": audience_mask,
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

        target_table = d.pop("targetTable")

        target_id = d.pop("targetId")

        audience_mask = d.pop("audienceMask")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_personal_privacy_grants_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            target_table=target_table,
            target_id=target_id,
            audience_mask=audience_mask,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_personal_privacy_grants_id_response_200

