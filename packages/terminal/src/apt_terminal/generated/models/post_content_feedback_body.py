from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentFeedbackBody")



@_attrs_define
class PostContentFeedbackBody:
    """ 
        Attributes:
            user_email (str):
            category (str):
            subject (str):
            body (str):
            platform (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            app_version (Union[Unset, str]):
            os_version (Union[Unset, str]):
            device_info (Union[Unset, str]):
            status (Union[Unset, str]):
            admin_notes (Union[Unset, str]):
     """

    user_email: str
    category: str
    subject: str
    body: str
    platform: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    device_info: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    admin_notes: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        user_email = self.user_email

        category = self.category

        subject = self.subject

        body = self.body

        platform = self.platform

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        app_version = self.app_version

        os_version = self.os_version

        device_info = self.device_info

        status = self.status

        admin_notes = self.admin_notes


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "userEmail": user_email,
            "category": category,
            "subject": subject,
            "body": body,
            "platform": platform,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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
        user_email = d.pop("userEmail")

        category = d.pop("category")

        subject = d.pop("subject")

        body = d.pop("body")

        platform = d.pop("platform")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        app_version = d.pop("appVersion", UNSET)

        os_version = d.pop("osVersion", UNSET)

        device_info = d.pop("deviceInfo", UNSET)

        status = d.pop("status", UNSET)

        admin_notes = d.pop("adminNotes", UNSET)

        post_content_feedback_body = cls(
            user_email=user_email,
            category=category,
            subject=subject,
            body=body,
            platform=platform,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            app_version=app_version,
            os_version=os_version,
            device_info=device_info,
            status=status,
            admin_notes=admin_notes,
        )

        return post_content_feedback_body

