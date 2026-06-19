from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutEcosystemApplicationsIdBody")



@_attrs_define
class PutEcosystemApplicationsIdBody:
    """ 
        Attributes:
            ecosystem_id (str | Unset):
            slug (str | Unset):
            display_name (str | Unset):
            consumer_kind (str | Unset):
            is_deleted (bool | Unset):
     """

    ecosystem_id: str | Unset = UNSET
    slug: str | Unset = UNSET
    display_name: str | Unset = UNSET
    consumer_kind: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        slug = self.slug

        display_name = self.display_name

        consumer_kind = self.consumer_kind

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if consumer_kind is not UNSET:
            field_dict["consumerKind"] = consumer_kind
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        slug = d.pop("slug", UNSET)

        display_name = d.pop("displayName", UNSET)

        consumer_kind = d.pop("consumerKind", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        put_ecosystem_applications_id_body = cls(
            ecosystem_id=ecosystem_id,
            slug=slug,
            display_name=display_name,
            consumer_kind=consumer_kind,
            is_deleted=is_deleted,
        )

        return put_ecosystem_applications_id_body

