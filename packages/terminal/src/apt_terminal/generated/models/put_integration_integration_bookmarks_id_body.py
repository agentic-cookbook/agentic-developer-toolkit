from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutIntegrationIntegrationBookmarksIdBody")



@_attrs_define
class PutIntegrationIntegrationBookmarksIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            connection_id (Union[Unset, str]):
            external_id (Union[Unset, str]):
            source_provider (Union[Unset, str]):
            title (Union[Unset, str]):
            url (Union[Unset, str]):
            excerpt (Union[None, Unset, str]):
            note (Union[None, Unset, str]):
            tags (Union[None, Unset, str]):
            image_url (Union[None, Unset, str]):
            collection_id (Union[None, Unset, str]):
            collection_name (Union[None, Unset, str]):
            is_favorite (Union[Unset, bool]):
            is_deleted (Union[Unset, bool]):
            external_created_at (Union[None, Unset, str]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    source_provider: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    excerpt: Union[None, Unset, str] = UNSET
    note: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    collection_id: Union[None, Unset, str] = UNSET
    collection_name: Union[None, Unset, str] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    external_created_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        title = self.title

        url = self.url

        excerpt: Union[None, Unset, str]
        if isinstance(self.excerpt, Unset):
            excerpt = UNSET
        else:
            excerpt = self.excerpt

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        tags: Union[None, Unset, str]
        if isinstance(self.tags, Unset):
            tags = UNSET
        else:
            tags = self.tags

        image_url: Union[None, Unset, str]
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        collection_id: Union[None, Unset, str]
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        collection_name: Union[None, Unset, str]
        if isinstance(self.collection_name, Unset):
            collection_name = UNSET
        else:
            collection_name = self.collection_name

        is_favorite = self.is_favorite

        is_deleted = self.is_deleted

        external_created_at: Union[None, Unset, str]
        if isinstance(self.external_created_at, Unset):
            external_created_at = UNSET
        else:
            external_created_at = self.external_created_at


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
        if source_provider is not UNSET:
            field_dict["sourceProvider"] = source_provider
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if note is not UNSET:
            field_dict["note"] = note
        if tags is not UNSET:
            field_dict["tags"] = tags
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if collection_id is not UNSET:
            field_dict["collectionId"] = collection_id
        if collection_name is not UNSET:
            field_dict["collectionName"] = collection_name
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if external_created_at is not UNSET:
            field_dict["externalCreatedAt"] = external_created_at

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

        source_provider = d.pop("sourceProvider", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        def _parse_excerpt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        excerpt = _parse_excerpt(d.pop("excerpt", UNSET))


        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_tags(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        def _parse_collection_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        collection_id = _parse_collection_id(d.pop("collectionId", UNSET))


        def _parse_collection_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        collection_name = _parse_collection_name(d.pop("collectionName", UNSET))


        is_favorite = d.pop("isFavorite", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_external_created_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_created_at = _parse_external_created_at(d.pop("externalCreatedAt", UNSET))


        put_integration_integration_bookmarks_id_body = cls(
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            connection_id=connection_id,
            external_id=external_id,
            source_provider=source_provider,
            title=title,
            url=url,
            excerpt=excerpt,
            note=note,
            tags=tags,
            image_url=image_url,
            collection_id=collection_id,
            collection_name=collection_name,
            is_favorite=is_favorite,
            is_deleted=is_deleted,
            external_created_at=external_created_at,
        )

        return put_integration_integration_bookmarks_id_body

