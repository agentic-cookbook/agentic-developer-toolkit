from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostProjectTasksBody")



@_attrs_define
class PostProjectTasksBody:
    """ 
        Attributes:
            connection_id (str):
            external_id (str):
            source_provider (str):
            title (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            description (Union[None, Unset, str]):
            is_completed (Union[Unset, bool]):
            priority (Union[Unset, int]):
            due_date (Union[None, Unset, str]):
            due_datetime (Union[None, Unset, str]):
            external_project_id (Union[None, Unset, str]):
            external_project_name (Union[None, Unset, str]):
            labels (Union[None, Unset, str]):
            url (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    connection_id: str
    external_id: str
    source_provider: str
    title: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    is_completed: Union[Unset, bool] = UNSET
    priority: Union[Unset, int] = UNSET
    due_date: Union[None, Unset, str] = UNSET
    due_datetime: Union[None, Unset, str] = UNSET
    external_project_id: Union[None, Unset, str] = UNSET
    external_project_name: Union[None, Unset, str] = UNSET
    labels: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        title = self.title

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_completed = self.is_completed

        priority = self.priority

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        due_datetime: Union[None, Unset, str]
        if isinstance(self.due_datetime, Unset):
            due_datetime = UNSET
        else:
            due_datetime = self.due_datetime

        external_project_id: Union[None, Unset, str]
        if isinstance(self.external_project_id, Unset):
            external_project_id = UNSET
        else:
            external_project_id = self.external_project_id

        external_project_name: Union[None, Unset, str]
        if isinstance(self.external_project_name, Unset):
            external_project_name = UNSET
        else:
            external_project_name = self.external_project_name

        labels: Union[None, Unset, str]
        if isinstance(self.labels, Unset):
            labels = UNSET
        else:
            labels = self.labels

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connectionId": connection_id,
            "externalId": external_id,
            "sourceProvider": source_provider,
            "title": title,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if due_datetime is not UNSET:
            field_dict["dueDatetime"] = due_datetime
        if external_project_id is not UNSET:
            field_dict["externalProjectId"] = external_project_id
        if external_project_name is not UNSET:
            field_dict["externalProjectName"] = external_project_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if url is not UNSET:
            field_dict["url"] = url
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        source_provider = d.pop("sourceProvider")

        title = d.pop("title")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        is_completed = d.pop("isCompleted", UNSET)

        priority = d.pop("priority", UNSET)

        def _parse_due_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))


        def _parse_due_datetime(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        due_datetime = _parse_due_datetime(d.pop("dueDatetime", UNSET))


        def _parse_external_project_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_project_id = _parse_external_project_id(d.pop("externalProjectId", UNSET))


        def _parse_external_project_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_project_name = _parse_external_project_name(d.pop("externalProjectName", UNSET))


        def _parse_labels(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        labels = _parse_labels(d.pop("labels", UNSET))


        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        post_project_tasks_body = cls(
            connection_id=connection_id,
            external_id=external_id,
            source_provider=source_provider,
            title=title,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
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
        )

        return post_project_tasks_body

