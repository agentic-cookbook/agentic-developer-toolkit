from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutPersonalContactsIdBody")



@_attrs_define
class PutPersonalContactsIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            person_user_id (Union[None, Unset, str]):
            full_name (Union[Unset, str]):
            nickname (Union[Unset, str]):
            email (Union[Unset, str]):
            phone (Union[Unset, str]):
            notes (Union[Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    person_user_id: Union[None, Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        person_user_id: Union[None, Unset, str]
        if isinstance(self.person_user_id, Unset):
            person_user_id = UNSET
        else:
            person_user_id = self.person_user_id

        full_name = self.full_name

        nickname = self.nickname

        email = self.email

        phone = self.phone

        notes = self.notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if person_user_id is not UNSET:
            field_dict["personUserId"] = person_user_id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
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

        def _parse_person_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        person_user_id = _parse_person_user_id(d.pop("personUserId", UNSET))


        full_name = d.pop("fullName", UNSET)

        nickname = d.pop("nickname", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        notes = d.pop("notes", UNSET)

        put_personal_contacts_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            person_user_id=person_user_id,
            full_name=full_name,
            nickname=nickname,
            email=email,
            phone=phone,
            notes=notes,
        )

        return put_personal_contacts_id_body

