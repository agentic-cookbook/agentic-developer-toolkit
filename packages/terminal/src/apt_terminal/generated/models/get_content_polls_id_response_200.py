from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetContentPollsIdResponse200")



@_attrs_define
class GetContentPollsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            host_kind (Union[None, str]):
            host_id (Union[None, str]):
            question (str):
            allow_multiple (bool):
            expires_at (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    host_kind: Union[None, str]
    host_id: Union[None, str]
    question: str
    allow_multiple: bool
    expires_at: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        host_kind: Union[None, str]
        host_kind = self.host_kind

        host_id: Union[None, str]
        host_id = self.host_id

        question = self.question

        allow_multiple = self.allow_multiple

        expires_at: Union[None, str]
        expires_at = self.expires_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "hostKind": host_kind,
            "hostId": host_id,
            "question": question,
            "allowMultiple": allow_multiple,
            "expiresAt": expires_at,
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

        def _parse_host_kind(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        host_kind = _parse_host_kind(d.pop("hostKind"))


        def _parse_host_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        host_id = _parse_host_id(d.pop("hostId"))


        question = d.pop("question")

        allow_multiple = d.pop("allowMultiple")

        def _parse_expires_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_content_polls_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            host_kind=host_kind,
            host_id=host_id,
            question=question,
            allow_multiple=allow_multiple,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_content_polls_id_response_200

