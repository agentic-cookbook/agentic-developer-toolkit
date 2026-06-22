from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetContentUrlsResponse200Item")



@_attrs_define
class GetContentUrlsResponse200Item:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            owner_id (str):
            original_url (str):
            canonical_url (str):
            canonical_url_hash (str):
            title (Union[None, str]):
            description (Union[None, str]):
            note (Union[None, str]):
            preview_storage_key (Union[None, str]):
            preview_url (Union[None, str]):
            preview_status (str):
            preview_error (Union[None, str]):
            preview_generated_at (Union[None, str]):
            preview_attempts (int):
            created_at (str):
            updated_at (str):
            is_deleted (bool):
     """

    id: str
    customer_id: str
    deleted_at: Union[None, str]
    owner_id: str
    original_url: str
    canonical_url: str
    canonical_url_hash: str
    title: Union[None, str]
    description: Union[None, str]
    note: Union[None, str]
    preview_storage_key: Union[None, str]
    preview_url: Union[None, str]
    preview_status: str
    preview_error: Union[None, str]
    preview_generated_at: Union[None, str]
    preview_attempts: int
    created_at: str
    updated_at: str
    is_deleted: bool





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        owner_id = self.owner_id

        original_url = self.original_url

        canonical_url = self.canonical_url

        canonical_url_hash = self.canonical_url_hash

        title: Union[None, str]
        title = self.title

        description: Union[None, str]
        description = self.description

        note: Union[None, str]
        note = self.note

        preview_storage_key: Union[None, str]
        preview_storage_key = self.preview_storage_key

        preview_url: Union[None, str]
        preview_url = self.preview_url

        preview_status = self.preview_status

        preview_error: Union[None, str]
        preview_error = self.preview_error

        preview_generated_at: Union[None, str]
        preview_generated_at = self.preview_generated_at

        preview_attempts = self.preview_attempts

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "ownerId": owner_id,
            "originalUrl": original_url,
            "canonicalUrl": canonical_url,
            "canonicalUrlHash": canonical_url_hash,
            "title": title,
            "description": description,
            "note": note,
            "previewStorageKey": preview_storage_key,
            "previewUrl": preview_url,
            "previewStatus": preview_status,
            "previewError": preview_error,
            "previewGeneratedAt": preview_generated_at,
            "previewAttempts": preview_attempts,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
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

        original_url = d.pop("originalUrl")

        canonical_url = d.pop("canonicalUrl")

        canonical_url_hash = d.pop("canonicalUrlHash")

        def _parse_title(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        title = _parse_title(d.pop("title"))


        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))


        def _parse_note(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        note = _parse_note(d.pop("note"))


        def _parse_preview_storage_key(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_storage_key = _parse_preview_storage_key(d.pop("previewStorageKey"))


        def _parse_preview_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_url = _parse_preview_url(d.pop("previewUrl"))


        preview_status = d.pop("previewStatus")

        def _parse_preview_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_error = _parse_preview_error(d.pop("previewError"))


        def _parse_preview_generated_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        preview_generated_at = _parse_preview_generated_at(d.pop("previewGeneratedAt"))


        preview_attempts = d.pop("previewAttempts")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        get_content_urls_response_200_item = cls(
            id=id,
            customer_id=customer_id,
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
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
        )

        return get_content_urls_response_200_item

