from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostEcosystemApplicationsBody")



@_attrs_define
class PostEcosystemApplicationsBody:
    """ 
        Attributes:
            slug (str):
            display_name (str):
            consumer_kind (str):
            ecosystem_id (str | Unset):
            is_deleted (bool | Unset):
            id (str | Unset):
     """

    slug: str
    display_name: str
    consumer_kind: str
    ecosystem_id: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        display_name = self.display_name

        consumer_kind = self.consumer_kind

        ecosystem_id = self.ecosystem_id

        is_deleted = self.is_deleted

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "displayName": display_name,
            "consumerKind": consumer_kind,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        display_name = d.pop("displayName")

        consumer_kind = d.pop("consumerKind")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        id = d.pop("id", UNSET)

        post_ecosystem_applications_body = cls(
            slug=slug,
            display_name=display_name,
            consumer_kind=consumer_kind,
            ecosystem_id=ecosystem_id,
            is_deleted=is_deleted,
            id=id,
        )

        return post_ecosystem_applications_body

