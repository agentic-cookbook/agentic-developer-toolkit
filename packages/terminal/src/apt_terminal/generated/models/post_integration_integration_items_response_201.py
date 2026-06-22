from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostIntegrationIntegrationItemsResponse201")



@_attrs_define
class PostIntegrationIntegrationItemsResponse201:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            connection_id (str):
            external_id (str):
            item_type (str):
            title (str):
            body (Union[None, str]):
            state (str):
            repo_full_name (str):
            repo_url (Union[None, str]):
            item_url (Union[None, str]):
            number (Union[None, int]):
            labels (Union[None, str]):
            assignees (Union[None, str]):
            is_read (bool):
            notification_reason (Union[None, str]):
            is_deleted (bool):
            sync_version (int):
            external_created_at (Union[None, str]):
            external_updated_at (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    connection_id: str
    external_id: str
    item_type: str
    title: str
    body: Union[None, str]
    state: str
    repo_full_name: str
    repo_url: Union[None, str]
    item_url: Union[None, str]
    number: Union[None, int]
    labels: Union[None, str]
    assignees: Union[None, str]
    is_read: bool
    notification_reason: Union[None, str]
    is_deleted: bool
    sync_version: int
    external_created_at: Union[None, str]
    external_updated_at: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        connection_id = self.connection_id

        external_id = self.external_id

        item_type = self.item_type

        title = self.title

        body: Union[None, str]
        body = self.body

        state = self.state

        repo_full_name = self.repo_full_name

        repo_url: Union[None, str]
        repo_url = self.repo_url

        item_url: Union[None, str]
        item_url = self.item_url

        number: Union[None, int]
        number = self.number

        labels: Union[None, str]
        labels = self.labels

        assignees: Union[None, str]
        assignees = self.assignees

        is_read = self.is_read

        notification_reason: Union[None, str]
        notification_reason = self.notification_reason

        is_deleted = self.is_deleted

        sync_version = self.sync_version

        external_created_at: Union[None, str]
        external_created_at = self.external_created_at

        external_updated_at: Union[None, str]
        external_updated_at = self.external_updated_at

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "connectionId": connection_id,
            "externalId": external_id,
            "itemType": item_type,
            "title": title,
            "body": body,
            "state": state,
            "repoFullName": repo_full_name,
            "repoUrl": repo_url,
            "itemUrl": item_url,
            "number": number,
            "labels": labels,
            "assignees": assignees,
            "isRead": is_read,
            "notificationReason": notification_reason,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
            "externalCreatedAt": external_created_at,
            "externalUpdatedAt": external_updated_at,
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

        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        item_type = d.pop("itemType")

        title = d.pop("title")

        def _parse_body(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        body = _parse_body(d.pop("body"))


        state = d.pop("state")

        repo_full_name = d.pop("repoFullName")

        def _parse_repo_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        repo_url = _parse_repo_url(d.pop("repoUrl"))


        def _parse_item_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        item_url = _parse_item_url(d.pop("itemUrl"))


        def _parse_number(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        number = _parse_number(d.pop("number"))


        def _parse_labels(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        labels = _parse_labels(d.pop("labels"))


        def _parse_assignees(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        assignees = _parse_assignees(d.pop("assignees"))


        is_read = d.pop("isRead")

        def _parse_notification_reason(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        notification_reason = _parse_notification_reason(d.pop("notificationReason"))


        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        def _parse_external_created_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt"))


        def _parse_external_updated_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_updated_at = _parse_external_updated_at(d.pop("externalUpdatedAt"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_integration_integration_items_response_201 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            connection_id=connection_id,
            external_id=external_id,
            item_type=item_type,
            title=title,
            body=body,
            state=state,
            repo_full_name=repo_full_name,
            repo_url=repo_url,
            item_url=item_url,
            number=number,
            labels=labels,
            assignees=assignees,
            is_read=is_read,
            notification_reason=notification_reason,
            is_deleted=is_deleted,
            sync_version=sync_version,
            external_created_at=external_created_at,
            external_updated_at=external_updated_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_integration_integration_items_response_201

