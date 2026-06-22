from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostIntegrationIntegrationSocialNotificationsBody")



@_attrs_define
class PostIntegrationIntegrationSocialNotificationsBody:
    """ 
        Attributes:
            connection_id (str):
            external_id (str):
            source_provider (str):
            notification_type (str):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            title (Union[None, Unset, str]):
            body (Union[None, Unset, str]):
            author_handle (Union[None, Unset, str]):
            author_display_name (Union[None, Unset, str]):
            item_url (Union[None, Unset, str]):
            is_read (Union[Unset, bool]):
            is_deleted (Union[Unset, bool]):
            external_created_at (Union[None, Unset, str]):
     """

    connection_id: str
    external_id: str
    source_provider: str
    notification_type: str
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    body: Union[None, Unset, str] = UNSET
    author_handle: Union[None, Unset, str] = UNSET
    author_display_name: Union[None, Unset, str] = UNSET
    item_url: Union[None, Unset, str] = UNSET
    is_read: Union[Unset, bool] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    external_created_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        notification_type = self.notification_type

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        body: Union[None, Unset, str]
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        author_handle: Union[None, Unset, str]
        if isinstance(self.author_handle, Unset):
            author_handle = UNSET
        else:
            author_handle = self.author_handle

        author_display_name: Union[None, Unset, str]
        if isinstance(self.author_display_name, Unset):
            author_display_name = UNSET
        else:
            author_display_name = self.author_display_name

        item_url: Union[None, Unset, str]
        if isinstance(self.item_url, Unset):
            item_url = UNSET
        else:
            item_url = self.item_url

        is_read = self.is_read

        is_deleted = self.is_deleted

        external_created_at: Union[None, Unset, str]
        if isinstance(self.external_created_at, Unset):
            external_created_at = UNSET
        else:
            external_created_at = self.external_created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connectionId": connection_id,
            "externalId": external_id,
            "sourceProvider": source_provider,
            "notificationType": notification_type,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if author_handle is not UNSET:
            field_dict["authorHandle"] = author_handle
        if author_display_name is not UNSET:
            field_dict["authorDisplayName"] = author_display_name
        if item_url is not UNSET:
            field_dict["itemUrl"] = item_url
        if is_read is not UNSET:
            field_dict["isRead"] = is_read
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if external_created_at is not UNSET:
            field_dict["externalCreatedAt"] = external_created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        source_provider = d.pop("sourceProvider")

        notification_type = d.pop("notificationType")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_body(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_author_handle(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author_handle = _parse_author_handle(d.pop("authorHandle", UNSET))


        def _parse_author_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        author_display_name = _parse_author_display_name(d.pop("authorDisplayName", UNSET))


        def _parse_item_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_url = _parse_item_url(d.pop("itemUrl", UNSET))


        is_read = d.pop("isRead", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_external_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt", UNSET))


        post_integration_integration_social_notifications_body = cls(
            connection_id=connection_id,
            external_id=external_id,
            source_provider=source_provider,
            notification_type=notification_type,
            deleted_at=deleted_at,
            owner_id=owner_id,
            title=title,
            body=body,
            author_handle=author_handle,
            author_display_name=author_display_name,
            item_url=item_url,
            is_read=is_read,
            is_deleted=is_deleted,
            external_created_at=external_created_at,
        )

        return post_integration_integration_social_notifications_body

