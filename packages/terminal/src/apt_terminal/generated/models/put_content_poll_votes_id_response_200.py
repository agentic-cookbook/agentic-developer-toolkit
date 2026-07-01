from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutContentPollVotesIdResponse200")



@_attrs_define
class PutContentPollVotesIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            option_id (str):
            created_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: Union[None, str]
    option_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        option_id = self.option_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "optionId": option_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        option_id = d.pop("optionId")

        created_at = d.pop("createdAt")

        put_content_poll_votes_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            option_id=option_id,
            created_at=created_at,
        )

        return put_content_poll_votes_id_response_200

