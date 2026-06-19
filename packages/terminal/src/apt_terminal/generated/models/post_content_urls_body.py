from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostContentUrlsBody")



@_attrs_define
class PostContentUrlsBody:
    """ 
        Attributes:
            original_url (str):
            canonical_url (str):
            canonical_url_hash (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            title (None | str | Unset):
            description (None | str | Unset):
            note (None | str | Unset):
            preview_storage_key (None | str | Unset):
            preview_url (None | str | Unset):
            preview_status (str | Unset):
            preview_error (None | str | Unset):
            preview_generated_at (None | str | Unset):
            preview_attempts (int | Unset):
            is_deleted (bool | Unset):
     """

    original_url: str
    canonical_url: str
    canonical_url_hash: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    preview_storage_key: None | str | Unset = UNSET
    preview_url: None | str | Unset = UNSET
    preview_status: str | Unset = UNSET
    preview_error: None | str | Unset = UNSET
    preview_generated_at: None | str | Unset = UNSET
    preview_attempts: int | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        original_url = self.original_url

        canonical_url = self.canonical_url

        canonical_url_hash = self.canonical_url_hash

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        preview_storage_key: None | str | Unset
        if isinstance(self.preview_storage_key, Unset):
            preview_storage_key = UNSET
        else:
            preview_storage_key = self.preview_storage_key

        preview_url: None | str | Unset
        if isinstance(self.preview_url, Unset):
            preview_url = UNSET
        else:
            preview_url = self.preview_url

        preview_status = self.preview_status

        preview_error: None | str | Unset
        if isinstance(self.preview_error, Unset):
            preview_error = UNSET
        else:
            preview_error = self.preview_error

        preview_generated_at: None | str | Unset
        if isinstance(self.preview_generated_at, Unset):
            preview_generated_at = UNSET
        else:
            preview_generated_at = self.preview_generated_at

        preview_attempts = self.preview_attempts

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "originalUrl": original_url,
            "canonicalUrl": canonical_url,
            "canonicalUrlHash": canonical_url_hash,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
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
        original_url = d.pop("originalUrl")

        canonical_url = d.pop("canonicalUrl")

        canonical_url_hash = d.pop("canonicalUrlHash")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))


        def _parse_preview_storage_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_storage_key = _parse_preview_storage_key(d.pop("previewStorageKey", UNSET))


        def _parse_preview_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_url = _parse_preview_url(d.pop("previewUrl", UNSET))


        preview_status = d.pop("previewStatus", UNSET)

        def _parse_preview_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_error = _parse_preview_error(d.pop("previewError", UNSET))


        def _parse_preview_generated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_generated_at = _parse_preview_generated_at(d.pop("previewGeneratedAt", UNSET))


        preview_attempts = d.pop("previewAttempts", UNSET)

        is_deleted = d.pop("isDeleted", UNSET)

        post_content_urls_body = cls(
            original_url=original_url,
            canonical_url=canonical_url,
            canonical_url_hash=canonical_url_hash,
            deleted_at=deleted_at,
            owner_id=owner_id,
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

        return post_content_urls_body

