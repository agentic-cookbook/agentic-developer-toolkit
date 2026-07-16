from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutContentContactsIdResponse200")



@_attrs_define
class PutContentContactsIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            ecosystem_id (str):
            owner_kind (str):
            owner_id (str):
            person_user_id (Union[None, str]):
            full_name (str):
            nickname (str):
            email (str):
            phone (str):
            notes (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    ecosystem_id: str
    owner_kind: str
    owner_id: str
    person_user_id: Union[None, str]
    full_name: str
    nickname: str
    email: str
    phone: str
    notes: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        owner_kind = self.owner_kind

        owner_id = self.owner_id

        person_user_id: Union[None, str]
        person_user_id = self.person_user_id

        full_name = self.full_name

        nickname = self.nickname

        email = self.email

        phone = self.phone

        notes = self.notes

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ecosystemId": ecosystem_id,
            "ownerKind": owner_kind,
            "ownerId": owner_id,
            "personUserId": person_user_id,
            "fullName": full_name,
            "nickname": nickname,
            "email": email,
            "phone": phone,
            "notes": notes,
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

        owner_kind = d.pop("ownerKind")

        owner_id = d.pop("ownerId")

        def _parse_person_user_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        person_user_id = _parse_person_user_id(d.pop("personUserId"))


        full_name = d.pop("fullName")

        nickname = d.pop("nickname")

        email = d.pop("email")

        phone = d.pop("phone")

        notes = d.pop("notes")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_content_contacts_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            owner_kind=owner_kind,
            owner_id=owner_id,
            person_user_id=person_user_id,
            full_name=full_name,
            nickname=nickname,
            email=email,
            phone=phone,
            notes=notes,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_content_contacts_id_response_200

