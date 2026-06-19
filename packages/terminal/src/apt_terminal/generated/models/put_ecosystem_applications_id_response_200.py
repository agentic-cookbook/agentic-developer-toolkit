from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PutEcosystemApplicationsIdResponse200")



@_attrs_define
class PutEcosystemApplicationsIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            slug (str):
            display_name (str):
            consumer_kind (str):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
     """

    id: str
    ecosystem_id: str
    slug: str
    display_name: str
    consumer_kind: str
    created_at: str
    updated_at: str
    is_deleted: bool





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ecosystem_id = self.ecosystem_id

        slug = self.slug

        display_name = self.display_name

        consumer_kind = self.consumer_kind

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "slug": slug,
            "displayName": display_name,
            "consumerKind": consumer_kind,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        slug = d.pop("slug")

        display_name = d.pop("displayName")

        consumer_kind = d.pop("consumerKind")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        put_ecosystem_applications_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            slug=slug,
            display_name=display_name,
            consumer_kind=consumer_kind,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
        )

        return put_ecosystem_applications_id_response_200

