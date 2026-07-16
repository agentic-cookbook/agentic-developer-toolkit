from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_project_work_items_id_body_assignee_kind import PatchProjectWorkItemsIdBodyAssigneeKind
from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PatchProjectWorkItemsIdBody")



@_attrs_define
class PatchProjectWorkItemsIdBody:
    """ At least one mutable field is required (a no-op patch is a 400).

        Attributes:
            title (Union[Unset, str]):
            description (Union[Unset, str]):
            status_id (Union[Unset, str]):
            assignee_kind (Union[Unset, PatchProjectWorkItemsIdBodyAssigneeKind]): null clears the assignee (with
                assigneeId)
            assignee_id (Union[None, Unset, str]):
            priority (Union[Unset, int]):
            start_date (Union[None, Unset, str]):
            due_date (Union[None, Unset, str]):
            labels (Union[Unset, list[str]]):
            parent_id (Union[None, Unset, str]): null detaches the parent
     """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status_id: Union[Unset, str] = UNSET
    assignee_kind: Union[Unset, PatchProjectWorkItemsIdBodyAssigneeKind] = UNSET
    assignee_id: Union[None, Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    start_date: Union[None, Unset, str] = UNSET
    due_date: Union[None, Unset, str] = UNSET
    labels: Union[Unset, list[str]] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        status_id = self.status_id

        assignee_kind: Union[Unset, str] = UNSET
        if not isinstance(self.assignee_kind, Unset):
            assignee_kind = self.assignee_kind.value


        assignee_id: Union[None, Unset, str]
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        priority = self.priority

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

        labels: Union[Unset, list[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels



        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if assignee_kind is not UNSET:
            field_dict["assigneeKind"] = assignee_kind
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if labels is not UNSET:
            field_dict["labels"] = labels
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        status_id = d.pop("statusId", UNSET)

        _assignee_kind = d.pop("assigneeKind", UNSET)
        assignee_kind: Union[Unset, PatchProjectWorkItemsIdBodyAssigneeKind]
        if isinstance(_assignee_kind,  Unset):
            assignee_kind = UNSET
        else:
            assignee_kind = PatchProjectWorkItemsIdBodyAssigneeKind(_assignee_kind)




        def _parse_assignee_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))


        priority = d.pop("priority", UNSET)

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


        labels = cast(list[str], d.pop("labels", UNSET))


        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        patch_project_work_items_id_body = cls(
            title=title,
            description=description,
            status_id=status_id,
            assignee_kind=assignee_kind,
            assignee_id=assignee_id,
            priority=priority,
            start_date=start_date,
            due_date=due_date,
            labels=labels,
            parent_id=parent_id,
        )


        patch_project_work_items_id_body.additional_properties = d
        return patch_project_work_items_id_body

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
