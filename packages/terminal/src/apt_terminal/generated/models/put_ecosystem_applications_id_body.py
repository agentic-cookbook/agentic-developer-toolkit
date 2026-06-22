from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutEcosystemApplicationsIdBody")



@_attrs_define
class PutEcosystemApplicationsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            slug (Union[Unset, str]):
            display_name (Union[Unset, str]):
            consumer_kind (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    consumer_kind: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





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

