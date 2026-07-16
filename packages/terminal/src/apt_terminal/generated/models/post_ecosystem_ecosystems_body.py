from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostEcosystemEcosystemsBody")



@_attrs_define
class PostEcosystemEcosystemsBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            owner_id (Union[Unset, str]):
            description (Union[Unset, str]):
            region (Union[Unset, str]):
            dedicated_db_connection_id (Union[None, Unset, str]):
            primary_domain (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
            is_default (Union[Unset, bool]):
            is_infrastructure (Union[Unset, bool]):
            namespace_id (Union[None, Unset, str]):
            id (Union[Unset, str]):
     """

    slug: str
    name: str
    owner_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    dedicated_db_connection_id: Union[None, Unset, str] = UNSET
    primary_domain: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_infrastructure: Union[Unset, bool] = UNSET
    namespace_id: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        owner_id = self.owner_id

        description = self.description

        region = self.region

        dedicated_db_connection_id: Union[None, Unset, str]
        if isinstance(self.dedicated_db_connection_id, Unset):
            dedicated_db_connection_id = UNSET
        else:
            dedicated_db_connection_id = self.dedicated_db_connection_id

        primary_domain = self.primary_domain

        is_deleted = self.is_deleted

        is_default = self.is_default

        is_infrastructure = self.is_infrastructure

        namespace_id: Union[None, Unset, str]
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
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_infrastructure is not UNSET:
            field_dict["isInfrastructure"] = is_infrastructure
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

        def _parse_dedicated_db_connection_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dedicated_db_connection_id = _parse_dedicated_db_connection_id(d.pop("dedicatedDbConnectionId", UNSET))


        primary_domain = d.pop("primaryDomain", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_infrastructure = d.pop("isInfrastructure", UNSET)

        def _parse_namespace_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
            is_default=is_default,
            is_infrastructure=is_infrastructure,
            namespace_id=namespace_id,
            id=id,
        )

        return post_ecosystem_ecosystems_body

