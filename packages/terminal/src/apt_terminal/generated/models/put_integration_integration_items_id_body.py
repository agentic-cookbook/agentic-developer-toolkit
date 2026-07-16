from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutIntegrationIntegrationItemsIdBody")



@_attrs_define
class PutIntegrationIntegrationItemsIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            connection_id (Union[Unset, str]):
            external_id (Union[Unset, str]):
            item_type (Union[Unset, str]):
            title (Union[Unset, str]):
            body (Union[None, Unset, str]):
            state (Union[Unset, str]):
            repo_full_name (Union[Unset, str]):
            repo_url (Union[None, Unset, str]):
            item_url (Union[None, Unset, str]):
            number (Union[None, Unset, int]):
            labels (Union[None, Unset, str]):
            assignees (Union[None, Unset, str]):
            is_read (Union[Unset, bool]):
            notification_reason (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
            external_created_at (Union[None, Unset, str]):
            external_updated_at (Union[None, Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    item_type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    body: Union[None, Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    repo_full_name: Union[Unset, str] = UNSET
    repo_url: Union[None, Unset, str] = UNSET
    item_url: Union[None, Unset, str] = UNSET
    number: Union[None, Unset, int] = UNSET
    labels: Union[None, Unset, str] = UNSET
    assignees: Union[None, Unset, str] = UNSET
    is_read: Union[Unset, bool] = UNSET
    notification_reason: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    external_created_at: Union[None, Unset, str] = UNSET
    external_updated_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        connection_id = self.connection_id

        external_id = self.external_id

        item_type = self.item_type

        title = self.title

        body: Union[None, Unset, str]
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        state = self.state

        repo_full_name = self.repo_full_name

        repo_url: Union[None, Unset, str]
        if isinstance(self.repo_url, Unset):
            repo_url = UNSET
        else:
            repo_url = self.repo_url

        item_url: Union[None, Unset, str]
        if isinstance(self.item_url, Unset):
            item_url = UNSET
        else:
            item_url = self.item_url

        number: Union[None, Unset, int]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        labels: Union[None, Unset, str]
        if isinstance(self.labels, Unset):
            labels = UNSET
        else:
            labels = self.labels

        assignees: Union[None, Unset, str]
        if isinstance(self.assignees, Unset):
            assignees = UNSET
        else:
            assignees = self.assignees

        is_read = self.is_read

        notification_reason: Union[None, Unset, str]
        if isinstance(self.notification_reason, Unset):
            notification_reason = UNSET
        else:
            notification_reason = self.notification_reason

        is_deleted = self.is_deleted

        external_created_at: Union[None, Unset, str]
        if isinstance(self.external_created_at, Unset):
            external_created_at = UNSET
        else:
            external_created_at = self.external_created_at

        external_updated_at: Union[None, Unset, str]
        if isinstance(self.external_updated_at, Unset):
            external_updated_at = UNSET
        else:
            external_updated_at = self.external_updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if state is not UNSET:
            field_dict["state"] = state
        if repo_full_name is not UNSET:
            field_dict["repoFullName"] = repo_full_name
        if repo_url is not UNSET:
            field_dict["repoUrl"] = repo_url
        if item_url is not UNSET:
            field_dict["itemUrl"] = item_url
        if number is not UNSET:
            field_dict["number"] = number
        if labels is not UNSET:
            field_dict["labels"] = labels
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if is_read is not UNSET:
            field_dict["isRead"] = is_read
        if notification_reason is not UNSET:
            field_dict["notificationReason"] = notification_reason
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if external_created_at is not UNSET:
            field_dict["externalCreatedAt"] = external_created_at
        if external_updated_at is not UNSET:
            field_dict["externalUpdatedAt"] = external_updated_at

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


        ecosystem_id = d.pop("ecosystemId", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        external_id = d.pop("externalId", UNSET)

        item_type = d.pop("itemType", UNSET)

        title = d.pop("title", UNSET)

        def _parse_body(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        body = _parse_body(d.pop("body", UNSET))


        state = d.pop("state", UNSET)

        repo_full_name = d.pop("repoFullName", UNSET)

        def _parse_repo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        repo_url = _parse_repo_url(d.pop("repoUrl", UNSET))


        def _parse_item_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_url = _parse_item_url(d.pop("itemUrl", UNSET))


        def _parse_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number = _parse_number(d.pop("number", UNSET))


        def _parse_labels(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        labels = _parse_labels(d.pop("labels", UNSET))


        def _parse_assignees(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignees = _parse_assignees(d.pop("assignees", UNSET))


        is_read = d.pop("isRead", UNSET)

        def _parse_notification_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notification_reason = _parse_notification_reason(d.pop("notificationReason", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_external_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt", UNSET))


        def _parse_external_updated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_updated_at = _parse_external_updated_at(d.pop("externalUpdatedAt", UNSET))


        put_integration_integration_items_id_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
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
            external_created_at=external_created_at,
            external_updated_at=external_updated_at,
        )

        return put_integration_integration_items_id_body

