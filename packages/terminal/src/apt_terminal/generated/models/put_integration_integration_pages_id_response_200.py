from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutIntegrationIntegrationPagesIdResponse200")



@_attrs_define
class PutIntegrationIntegrationPagesIdResponse200:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            connection_id (str):
            external_id (str):
            title (str):
            object_type (str):
            url (Union[None, str]):
            icon (Union[None, str]):
            parent_type (Union[None, str]):
            parent_id (Union[None, str]):
            is_archived (bool):
            last_edited_at (Union[None, str]):
            is_deleted (bool):
            sync_version (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    connection_id: str
    external_id: str
    title: str
    object_type: str
    url: Union[None, str]
    icon: Union[None, str]
    parent_type: Union[None, str]
    parent_id: Union[None, str]
    is_archived: bool
    last_edited_at: Union[None, str]
    is_deleted: bool
    sync_version: int
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        connection_id = self.connection_id

        external_id = self.external_id

        title = self.title

        object_type = self.object_type

        url: Union[None, str]
        url = self.url

        icon: Union[None, str]
        icon = self.icon

        parent_type: Union[None, str]
        parent_type = self.parent_type

        parent_id: Union[None, str]
        parent_id = self.parent_id

        is_archived = self.is_archived

        last_edited_at: Union[None, str]
        last_edited_at = self.last_edited_at

        is_deleted = self.is_deleted

        sync_version = self.sync_version

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "connectionId": connection_id,
            "externalId": external_id,
            "title": title,
            "objectType": object_type,
            "url": url,
            "icon": icon,
            "parentType": parent_type,
            "parentId": parent_id,
            "isArchived": is_archived,
            "lastEditedAt": last_edited_at,
            "isDeleted": is_deleted,
            "syncVersion": sync_version,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        owner_id = d.pop("ownerId")

        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        title = d.pop("title")

        object_type = d.pop("objectType")

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop("url"))


        def _parse_icon(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        icon = _parse_icon(d.pop("icon"))


        def _parse_parent_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_type = _parse_parent_type(d.pop("parentType"))


        def _parse_parent_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_id = _parse_parent_id(d.pop("parentId"))


        is_archived = d.pop("isArchived")

        def _parse_last_edited_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_edited_at = _parse_last_edited_at(d.pop("lastEditedAt"))


        is_deleted = d.pop("isDeleted")

        sync_version = d.pop("syncVersion")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_integration_integration_pages_id_response_200 = cls(
            id=id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            connection_id=connection_id,
            external_id=external_id,
            title=title,
            object_type=object_type,
            url=url,
            icon=icon,
            parent_type=parent_type,
            parent_id=parent_id,
            is_archived=is_archived,
            last_edited_at=last_edited_at,
            is_deleted=is_deleted,
            sync_version=sync_version,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_integration_integration_pages_id_response_200

