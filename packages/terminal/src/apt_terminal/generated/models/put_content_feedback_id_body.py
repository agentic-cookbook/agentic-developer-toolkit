from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutContentFeedbackIdBody")



@_attrs_define
class PutContentFeedbackIdBody:
    """ 
        Attributes:
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            user_email (str | Unset):
            category (str | Unset):
            subject (str | Unset):
            body (str | Unset):
            platform (str | Unset):
            app_version (str | Unset):
            os_version (str | Unset):
            device_info (str | Unset):
            status (str | Unset):
            admin_notes (str | Unset):
     """

    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    user_email: str | Unset = UNSET
    category: str | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    platform: str | Unset = UNSET
    app_version: str | Unset = UNSET
    os_version: str | Unset = UNSET
    device_info: str | Unset = UNSET
    status: str | Unset = UNSET
    admin_notes: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        user_email = self.user_email

        category = self.category

        subject = self.subject

        body = self.body

        platform = self.platform

        app_version = self.app_version

        os_version = self.os_version

        device_info = self.device_info

        status = self.status

        admin_notes = self.admin_notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email
        if category is not UNSET:
            field_dict["category"] = category
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if platform is not UNSET:
            field_dict["platform"] = platform
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info
        if status is not UNSET:
            field_dict["status"] = status
        if admin_notes is not UNSET:
            field_dict["adminNotes"] = admin_notes

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

        user_email = d.pop("userEmail", UNSET)

        category = d.pop("category", UNSET)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        platform = d.pop("platform", UNSET)

        app_version = d.pop("appVersion", UNSET)

        os_version = d.pop("osVersion", UNSET)

        device_info = d.pop("deviceInfo", UNSET)

        status = d.pop("status", UNSET)

        admin_notes = d.pop("adminNotes", UNSET)

        put_content_feedback_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            user_email=user_email,
            category=category,
            subject=subject,
            body=body,
            platform=platform,
            app_version=app_version,
            os_version=os_version,
            device_info=device_info,
            status=status,
            admin_notes=admin_notes,
        )

        return put_content_feedback_id_body

