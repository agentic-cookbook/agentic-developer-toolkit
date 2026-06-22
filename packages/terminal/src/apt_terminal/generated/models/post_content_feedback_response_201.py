from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostContentFeedbackResponse201")



@_attrs_define
class PostContentFeedbackResponse201:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            user_email (str):
            category (str):
            subject (str):
            body (str):
            platform (str):
            app_version (str):
            os_version (str):
            device_info (str):
            status (str):
            admin_notes (str):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    user_email: str
    category: str
    subject: str
    body: str
    platform: str
    app_version: str
    os_version: str
    device_info: str
    status: str
    admin_notes: str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
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

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "userEmail": user_email,
            "category": category,
            "subject": subject,
            "body": body,
            "platform": platform,
            "appVersion": app_version,
            "osVersion": os_version,
            "deviceInfo": device_info,
            "status": status,
            "adminNotes": admin_notes,
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

        user_email = d.pop("userEmail")

        category = d.pop("category")

        subject = d.pop("subject")

        body = d.pop("body")

        platform = d.pop("platform")

        app_version = d.pop("appVersion")

        os_version = d.pop("osVersion")

        device_info = d.pop("deviceInfo")

        status = d.pop("status")

        admin_notes = d.pop("adminNotes")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_content_feedback_response_201 = cls(
            id=id,
            customer_id=customer_id,
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
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_content_feedback_response_201

