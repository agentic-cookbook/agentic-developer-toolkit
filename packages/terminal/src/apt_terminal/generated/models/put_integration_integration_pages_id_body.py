from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutIntegrationIntegrationPagesIdBody")



@_attrs_define
class PutIntegrationIntegrationPagesIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            connection_id (Union[Unset, str]):
            external_id (Union[Unset, str]):
            title (Union[Unset, str]):
            object_type (Union[Unset, str]):
            url (Union[None, Unset, str]):
            icon (Union[None, Unset, str]):
            parent_type (Union[None, Unset, str]):
            parent_id (Union[None, Unset, str]):
            is_archived (Union[Unset, bool]):
            last_edited_at (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    object_type: Union[Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    parent_type: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    is_archived: Union[Unset, bool] = UNSET
    last_edited_at: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        connection_id = self.connection_id

        external_id = self.external_id

        title = self.title

        object_type = self.object_type

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        parent_type: Union[None, Unset, str]
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = self.parent_type

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        is_archived = self.is_archived

        last_edited_at: Union[None, Unset, str]
        if isinstance(self.last_edited_at, Unset):
            last_edited_at = UNSET
        else:
            last_edited_at = self.last_edited_at

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if title is not UNSET:
            field_dict["title"] = title
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if url is not UNSET:
            field_dict["url"] = url
        if icon is not UNSET:
            field_dict["icon"] = icon
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if last_edited_at is not UNSET:
            field_dict["lastEditedAt"] = last_edited_at
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        external_id = d.pop("externalId", UNSET)

        title = d.pop("title", UNSET)

        object_type = d.pop("objectType", UNSET)

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))


        def _parse_parent_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))


        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        is_archived = d.pop("isArchived", UNSET)

        def _parse_last_edited_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_edited_at = _parse_last_edited_at(d.pop("lastEditedAt", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        put_integration_integration_pages_id_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
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
        )

        return put_integration_integration_pages_id_body

