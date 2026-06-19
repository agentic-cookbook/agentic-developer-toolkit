from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostEcosystemEcosystemsBody")



@_attrs_define
class PostEcosystemEcosystemsBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            owner_id (str | Unset):
            description (str | Unset):
            region (str | Unset):
            dedicated_db_connection_id (None | str | Unset):
            primary_domain (str | Unset):
            is_deleted (bool | Unset):
            type_ (str | Unset):
            namespace_id (None | str | Unset):
            id (str | Unset):
     """

    slug: str
    name: str
    owner_id: str | Unset = UNSET
    description: str | Unset = UNSET
    region: str | Unset = UNSET
    dedicated_db_connection_id: None | str | Unset = UNSET
    primary_domain: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    type_: str | Unset = UNSET
    namespace_id: None | str | Unset = UNSET
    id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        owner_id = self.owner_id

        description = self.description

        region = self.region

        dedicated_db_connection_id: None | str | Unset
        if isinstance(self.dedicated_db_connection_id, Unset):
            dedicated_db_connection_id = UNSET
        else:
            dedicated_db_connection_id = self.dedicated_db_connection_id

        primary_domain = self.primary_domain

        is_deleted = self.is_deleted

        type_ = self.type_

        namespace_id: None | str | Unset
        if isinstance(self.namespace_id, Unset):
            namespace_id = UNSET
        else:
            namespace_id = self.namespace_id

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "name": name,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if description is not UNSET:
            field_dict["description"] = description
        if region is not UNSET:
            field_dict["region"] = region
        if dedicated_db_connection_id is not UNSET:
            field_dict["dedicatedDbConnectionId"] = dedicated_db_connection_id
        if primary_domain is not UNSET:
            field_dict["primaryDomain"] = primary_domain
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if type_ is not UNSET:
            field_dict["type"] = type_
        if namespace_id is not UNSET:
            field_dict["namespaceId"] = namespace_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        owner_id = d.pop("ownerId", UNSET)

        description = d.pop("description", UNSET)

        region = d.pop("region", UNSET)

        def _parse_dedicated_db_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dedicated_db_connection_id = _parse_dedicated_db_connection_id(d.pop("dedicatedDbConnectionId", UNSET))


        primary_domain = d.pop("primaryDomain", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_namespace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_id = _parse_namespace_id(d.pop("namespaceId", UNSET))


        id = d.pop("id", UNSET)

        post_ecosystem_ecosystems_body = cls(
            slug=slug,
            name=name,
            owner_id=owner_id,
            description=description,
            region=region,
            dedicated_db_connection_id=dedicated_db_connection_id,
            primary_domain=primary_domain,
            is_deleted=is_deleted,
            type_=type_,
            namespace_id=namespace_id,
            id=id,
        )

        return post_ecosystem_ecosystems_body

