from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_project_projects_id_statuses_status_id_body_category import PatchProjectProjectsIdStatusesStatusIdBodyCategory
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PatchProjectProjectsIdStatusesStatusIdBody")



@_attrs_define
class PatchProjectProjectsIdStatusesStatusIdBody:
    """ 
        Attributes:
            label (Union[Unset, str]):
            category (Union[Unset, PatchProjectProjectsIdStatusesStatusIdBodyCategory]):
            position (Union[Unset, int]):
     """

    label: Union[Unset, str] = UNSET
    category: Union[Unset, PatchProjectProjectsIdStatusesStatusIdBodyCategory] = UNSET
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        label = self.label

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        position = self.position


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if category is not UNSET:
            field_dict["category"] = category
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PatchProjectProjectsIdStatusesStatusIdBodyCategory]
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = PatchProjectProjectsIdStatusesStatusIdBodyCategory(_category)




        position = d.pop("position", UNSET)

        patch_project_projects_id_statuses_status_id_body = cls(
            label=label,
            category=category,
            position=position,
        )


        patch_project_projects_id_statuses_status_id_body.additional_properties = d
        return patch_project_projects_id_statuses_status_id_body

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
