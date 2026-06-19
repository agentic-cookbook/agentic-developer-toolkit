from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostIntegrationIntegrationItemsBody")



@_attrs_define
class PostIntegrationIntegrationItemsBody:
    """ 
        Attributes:
            connection_id (str):
            external_id (str):
            item_type (str):
            title (str):
            state (str):
            repo_full_name (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            body (None | str | Unset):
            repo_url (None | str | Unset):
            item_url (None | str | Unset):
            number (int | None | Unset):
            labels (None | str | Unset):
            assignees (None | str | Unset):
            is_read (bool | Unset):
            notification_reason (None | str | Unset):
            is_deleted (bool | Unset):
            external_created_at (None | str | Unset):
            external_updated_at (None | str | Unset):
     """

    connection_id: str
    external_id: str
    item_type: str
    title: str
    state: str
    repo_full_name: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    body: None | str | Unset = UNSET
    repo_url: None | str | Unset = UNSET
    item_url: None | str | Unset = UNSET
    number: int | None | Unset = UNSET
    labels: None | str | Unset = UNSET
    assignees: None | str | Unset = UNSET
    is_read: bool | Unset = UNSET
    notification_reason: None | str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    external_created_at: None | str | Unset = UNSET
    external_updated_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        item_type = self.item_type

        title = self.title

        state = self.state

        repo_full_name = self.repo_full_name

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        repo_url: None | str | Unset
        if isinstance(self.repo_url, Unset):
            repo_url = UNSET
        else:
            repo_url = self.repo_url

        item_url: None | str | Unset
        if isinstance(self.item_url, Unset):
            item_url = UNSET
        else:
            item_url = self.item_url

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        labels: None | str | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        else:
            labels = self.labels

        assignees: None | str | Unset
        if isinstance(self.assignees, Unset):
            assignees = UNSET
        else:
            assignees = self.assignees

        is_read = self.is_read

        notification_reason: None | str | Unset
        if isinstance(self.notification_reason, Unset):
            notification_reason = UNSET
        else:
            notification_reason = self.notification_reason

        is_deleted = self.is_deleted

        external_created_at: None | str | Unset
        if isinstance(self.external_created_at, Unset):
            external_created_at = UNSET
        else:
            external_created_at = self.external_created_at

        external_updated_at: None | str | Unset
        if isinstance(self.external_updated_at, Unset):
            external_updated_at = UNSET
        else:
            external_updated_at = self.external_updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connectionId": connection_id,
            "externalId": external_id,
            "itemType": item_type,
            "title": title,
            "state": state,
            "repoFullName": repo_full_name,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if body is not UNSET:
            field_dict["body"] = body
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
        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        item_type = d.pop("itemType")

        title = d.pop("title")

        state = d.pop("state")

        repo_full_name = d.pop("repoFullName")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_repo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repo_url = _parse_repo_url(d.pop("repoUrl", UNSET))


        def _parse_item_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        item_url = _parse_item_url(d.pop("itemUrl", UNSET))


        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))


        def _parse_labels(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))


        def _parse_assignees(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignees = _parse_assignees(d.pop("assignees", UNSET))


        is_read = d.pop("isRead", UNSET)

        def _parse_notification_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_reason = _parse_notification_reason(d.pop("notificationReason", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_external_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt", UNSET))


        def _parse_external_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_updated_at = _parse_external_updated_at(d.pop("externalUpdatedAt", UNSET))


        post_integration_integration_items_body = cls(
            connection_id=connection_id,
            external_id=external_id,
            item_type=item_type,
            title=title,
            state=state,
            repo_full_name=repo_full_name,
            deleted_at=deleted_at,
            owner_id=owner_id,
            body=body,
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

        return post_integration_integration_items_body

