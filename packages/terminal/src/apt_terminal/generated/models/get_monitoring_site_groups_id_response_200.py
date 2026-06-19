from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetMonitoringSiteGroupsIdResponse200")



@_attrs_define
class GetMonitoringSiteGroupsIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (str):
            name (str):
            slug (str):
            description (None | str):
            retention_days (int):
            display_order (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    user_id: str
    name: str
    slug: str
    description: None | str
    retention_days: int
    display_order: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        name = self.name

        slug = self.slug

        description: None | str
        description = self.description

        retention_days = self.retention_days

        display_order = self.display_order

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "name": name,
            "slug": slug,
            "description": description,
            "retentionDays": retention_days,
            "displayOrder": display_order,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        retention_days = d.pop("retentionDays")

        display_order = d.pop("displayOrder")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_monitoring_site_groups_id_response_200 = cls(
            id=id,
            user_id=user_id,
            name=name,
            slug=slug,
            description=description,
            retention_days=retention_days,
            display_order=display_order,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_monitoring_site_groups_id_response_200

