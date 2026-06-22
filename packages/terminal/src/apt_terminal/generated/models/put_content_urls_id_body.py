from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentUrlsIdBody")



@_attrs_define
class PutContentUrlsIdBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            original_url (Union[Unset, str]):
            canonical_url (Union[Unset, str]):
            canonical_url_hash (Union[Unset, str]):
            title (Union[None, Unset, str]):
            description (Union[None, Unset, str]):
            note (Union[None, Unset, str]):
            preview_storage_key (Union[None, Unset, str]):
            preview_url (Union[None, Unset, str]):
            preview_status (Union[Unset, str]):
            preview_error (Union[None, Unset, str]):
            preview_generated_at (Union[None, Unset, str]):
            preview_attempts (Union[Unset, int]):
            is_deleted (Union[Unset, bool]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    original_url: Union[Unset, str] = UNSET
    canonical_url: Union[Unset, str] = UNSET
    canonical_url_hash: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    note: Union[None, Unset, str] = UNSET
    preview_storage_key: Union[None, Unset, str] = UNSET
    preview_url: Union[None, Unset, str] = UNSET
    preview_status: Union[Unset, str] = UNSET
    preview_error: Union[None, Unset, str] = UNSET
    preview_generated_at: Union[None, Unset, str] = UNSET
    preview_attempts: Union[Unset, int] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        original_url = self.original_url

        canonical_url = self.canonical_url

        canonical_url_hash = self.canonical_url_hash

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        preview_storage_key: Union[None, Unset, str]
        if isinstance(self.preview_storage_key, Unset):
            preview_storage_key = UNSET
        else:
            preview_storage_key = self.preview_storage_key

        preview_url: Union[None, Unset, str]
        if isinstance(self.preview_url, Unset):
            preview_url = UNSET
        else:
            preview_url = self.preview_url

        preview_status = self.preview_status

        preview_error: Union[None, Unset, str]
        if isinstance(self.preview_error, Unset):
            preview_error = UNSET
        else:
            preview_error = self.preview_error

        preview_generated_at: Union[None, Unset, str]
        if isinstance(self.preview_generated_at, Unset):
            preview_generated_at = UNSET
        else:
            preview_generated_at = self.preview_generated_at

        preview_attempts = self.preview_attempts

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if original_url is not UNSET:
            field_dict["originalUrl"] = original_url
        if canonical_url is not UNSET:
            field_dict["canonicalUrl"] = canonical_url
        if canonical_url_hash is not UNSET:
            field_dict["canonicalUrlHash"] = canonical_url_hash
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if note is not UNSET:
            field_dict["note"] = note
        if preview_storage_key is not UNSET:
            field_dict["previewStorageKey"] = preview_storage_key
        if preview_url is not UNSET:
            field_dict["previewUrl"] = preview_url
        if preview_status is not UNSET:
            field_dict["previewStatus"] = preview_status
        if preview_error is not UNSET:
            field_dict["previewError"] = preview_error
        if preview_generated_at is not UNSET:
            field_dict["previewGeneratedAt"] = preview_generated_at
        if preview_attempts is not UNSET:
            field_dict["previewAttempts"] = preview_attempts
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


        owner_id = d.pop("ownerId", UNSET)

        original_url = d.pop("originalUrl", UNSET)

        canonical_url = d.pop("canonicalUrl", UNSET)

        canonical_url_hash = d.pop("canonicalUrlHash", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_preview_storage_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_storage_key = _parse_preview_storage_key(d.pop("previewStorageKey", UNSET))


        def _parse_preview_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_url = _parse_preview_url(d.pop("previewUrl", UNSET))


        preview_status = d.pop("previewStatus", UNSET)

        def _parse_preview_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_error = _parse_preview_error(d.pop("previewError", UNSET))


        def _parse_preview_generated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preview_generated_at = _parse_preview_generated_at(d.pop("previewGeneratedAt", UNSET))


        preview_attempts = d.pop("previewAttempts", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        put_content_urls_id_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            original_url=original_url,
            canonical_url=canonical_url,
            canonical_url_hash=canonical_url_hash,
            title=title,
            description=description,
            note=note,
            preview_storage_key=preview_storage_key,
            preview_url=preview_url,
            preview_status=preview_status,
            preview_error=preview_error,
            preview_generated_at=preview_generated_at,
            preview_attempts=preview_attempts,
            is_deleted=is_deleted,
        )

        return put_content_urls_id_body

