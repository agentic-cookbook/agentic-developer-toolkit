from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetProjectTasksResponse200Item")



@_attrs_define
class GetProjectTasksResponse200Item:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (None | str):
            owner_id (str):
            connection_id (str):
            external_id (str):
            source_provider (str):
            title (str):
            description (None | str):
            is_completed (bool):
            priority (int):
            due_date (None | str):
            due_datetime (None | str):
            external_project_id (None | str):
            external_project_name (None | str):
            labels (None | str):
            url (None | str):
            is_deleted (bool):
            sync_version (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: None | str
    owner_id: str
    connection_id: str
    external_id: str
    source_provider: str
    title: str
    description: None | str
    is_completed: bool
    priority: int
    due_date: None | str
    due_datetime: None | str
    external_project_id: None | str
    external_project_name: None | str
    labels: None | str
    url: None | str
    is_deleted: bool
    sync_version: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: None | str
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        title = self.title

        description: None | str
        description = self.description

        is_completed = self.is_completed

        priority = self.priority

        due_date: None | str
        due_date = self.due_date

        due_datetime: None | str
        due_datetime = self.due_datetime

        external_project_id: None | str
        external_project_id = self.external_project_id

        external_project_name: None | str
        external_project_name = self.external_project_name

        labels: None | str
        labels = self.labels

        url: None | str
        url = self.url

        is_deleted = self.is_deleted

        sync_version = self.sync_version

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
            "sourceProvider": source_provider,
            "title": title,
            "description": description,
            "isCompleted": is_completed,
            "priority": priority,
            "dueDate": due_date,
            "dueDatetime": due_datetime,
            "externalProjectId": external_project_id,
            "externalProjectName": external_project_name,
            "labels": labels,
            "url": url,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        source_provider = d.pop("sourceProvider")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        is_completed = d.pop("isCompleted")

        priority = d.pop("priority")

        def _parse_due_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        due_date = _parse_due_date(d.pop("dueDate"))


        def _parse_due_datetime(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        due_datetime = _parse_due_datetime(d.pop("dueDatetime"))


        def _parse_external_project_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_project_id = _parse_external_project_id(d.pop("externalProjectId"))


        def _parse_external_project_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_project_name = _parse_external_project_name(d.pop("externalProjectName"))


        def _parse_labels(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        labels = _parse_labels(d.pop("labels"))


        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))


        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_project_tasks_response_200_item = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            connection_id=connection_id,
            external_id=external_id,
            source_provider=source_provider,
            title=title,
            description=description,
            is_completed=is_completed,
            priority=priority,
            due_date=due_date,
            due_datetime=due_datetime,
            external_project_id=external_project_id,
            external_project_name=external_project_name,
            labels=labels,
            url=url,
            is_deleted=is_deleted,
            sync_version=sync_version,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_project_tasks_response_200_item

