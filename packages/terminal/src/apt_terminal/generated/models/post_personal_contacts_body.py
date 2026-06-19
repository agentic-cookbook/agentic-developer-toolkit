from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostPersonalContactsBody")



@_attrs_define
class PostPersonalContactsBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            person_user_id (None | str | Unset):
            full_name (str | Unset):
            nickname (str | Unset):
            email (str | Unset):
            phone (str | Unset):
            notes (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    person_user_id: None | str | Unset = UNSET
    full_name: str | Unset = UNSET
    nickname: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    notes: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        person_user_id: None | str | Unset
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
        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_person_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_user_id = _parse_person_user_id(d.pop("personUserId", UNSET))


        full_name = d.pop("fullName", UNSET)

        nickname = d.pop("nickname", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        notes = d.pop("notes", UNSET)

        post_personal_contacts_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            person_user_id=person_user_id,
            full_name=full_name,
            nickname=nickname,
            email=email,
            phone=phone,
            notes=notes,
        )

        return post_personal_contacts_body

