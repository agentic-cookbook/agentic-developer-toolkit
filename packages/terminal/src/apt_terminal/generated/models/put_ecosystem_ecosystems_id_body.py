from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutEcosystemEcosystemsIdBody")



@_attrs_define
class PutEcosystemEcosystemsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            slug (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            region (Union[Unset, str]):
            dedicated_db_connection_id (Union[None, Unset, str]):
            primary_domain (Union[Unset, str]):
            is_deleted (Union[Unset, bool]):
            type_ (Union[Unset, str]):
            namespace_id (Union[None, Unset, str]):
     """

    owner_id: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    dedicated_db_connection_id: Union[None, Unset, str] = UNSET
    primary_domain: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    type_: Union[Unset, str] = UNSET
    namespace_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        slug = self.slug

        name = self.name

        description = self.description

        region = self.region

        dedicated_db_connection_id: Union[None, Unset, str]
        if isinstance(self.dedicated_db_connection_id, Unset):
            dedicated_db_connection_id = UNSET
        else:
            dedicated_db_connection_id = self.dedicated_db_connection_id

        primary_domain = self.primary_domain

        is_deleted = self.is_deleted

        type_ = self.type_

        namespace_id: Union[None, Unset, str]
        if isinstance(self.namespace_id, Unset):
            namespace_id = UNSET
        else:
            namespace_id = self.namespace_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

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

        type_ = d.pop("type", UNSET)

        def _parse_namespace_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        namespace_id = _parse_namespace_id(d.pop("namespaceId", UNSET))


        put_ecosystem_ecosystems_id_body = cls(
            owner_id=owner_id,
            slug=slug,
            name=name,
            description=description,
            region=region,
            dedicated_db_connection_id=dedicated_db_connection_id,
            primary_domain=primary_domain,
            is_deleted=is_deleted,
            type_=type_,
            namespace_id=namespace_id,
        )

        return put_ecosystem_ecosystems_id_body

