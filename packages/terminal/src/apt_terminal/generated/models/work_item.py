from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.work_item_assignee_kind import WorkItemAssigneeKind
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="WorkItem")



@_attrs_define
class WorkItem:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            project_id (str):
            title (str):
            description (str):
            status_id (str): the board column this card sits in
            priority (int):
            labels (list[str]):
            position (int): board order within the project (ascending)
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            assignee_kind (Union[Unset, WorkItemAssigneeKind]):
            assignee_id (Union[None, Unset, str]):
            start_date (Union[None, Unset, str]): date (YYYY-MM-DD)
            due_date (Union[None, Unset, str]): date (YYYY-MM-DD)
            parent_id (Union[None, Unset, str]): a parent work item in the same project
            created_by (Union[None, Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    id: str
    ecosystem_id: str
    project_id: str
    title: str
    description: str
    status_id: str
    priority: int
    labels: list[str]
    position: int
    created_at: str
    updated_at: str
    is_deleted: bool
    assignee_kind: Union[Unset, WorkItemAssigneeKind] = UNSET
    assignee_id: Union[None, Unset, str] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    due_date: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        project_id = self.project_id

        title = self.title

        description = self.description

        status_id = self.status_id

        priority = self.priority

        labels = self.labels



        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted

        assignee_kind: Union[Unset, str] = UNSET
        if not isinstance(self.assignee_kind, Unset):
            assignee_kind = self.assignee_kind.value


        assignee_id: Union[None, Unset, str]
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "projectId": project_id,
            "title": title,
            "description": description,
            "statusId": status_id,
            "priority": priority,
            "labels": labels,
            "position": position,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
        })
        if assignee_kind is not UNSET:
            field_dict["assigneeKind"] = assignee_kind
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        project_id = d.pop("projectId")

        title = d.pop("title")

        description = d.pop("description")

        status_id = d.pop("statusId")

        priority = d.pop("priority")

        labels = cast(list[str], d.pop("labels"))


        position = d.pop("position")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        _assignee_kind = d.pop("assigneeKind", UNSET)
        assignee_kind: Union[Unset, WorkItemAssigneeKind]
        if isinstance(_assignee_kind,  Unset):
            assignee_kind = UNSET
        else:
            assignee_kind = WorkItemAssigneeKind(_assignee_kind)




        def _parse_assignee_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))


        def _parse_start_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))


        def _parse_due_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))


        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))


        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        work_item = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            project_id=project_id,
            title=title,
            description=description,
            status_id=status_id,
            priority=priority,
            labels=labels,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            assignee_kind=assignee_kind,
            assignee_id=assignee_id,
            start_date=start_date,
            due_date=due_date,
            parent_id=parent_id,
            created_by=created_by,
            deleted_at=deleted_at,
        )


        work_item.additional_properties = d
        return work_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
