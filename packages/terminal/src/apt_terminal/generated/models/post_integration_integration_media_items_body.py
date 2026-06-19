from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostIntegrationIntegrationMediaItemsBody")



@_attrs_define
class PostIntegrationIntegrationMediaItemsBody:
    """ 
        Attributes:
            connection_id (str):
            external_id (str):
            source_provider (str):
            media_type (str):
            title (str):
            deleted_at (None | str | Unset):
            owner_id (str | Unset):
            artist (None | str | Unset):
            album (None | str | Unset):
            image_url (None | str | Unset):
            external_url (None | str | Unset):
            duration_ms (int | None | Unset):
            popularity (int | None | Unset):
            is_saved (bool | Unset):
            last_played_at (None | str | Unset):
            is_deleted (bool | Unset):
     """

    connection_id: str
    external_id: str
    source_provider: str
    media_type: str
    title: str
    deleted_at: None | str | Unset = UNSET
    owner_id: str | Unset = UNSET
    artist: None | str | Unset = UNSET
    album: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    popularity: int | None | Unset = UNSET
    is_saved: bool | Unset = UNSET
    last_played_at: None | str | Unset = UNSET
    is_deleted: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        media_type = self.media_type

        title = self.title

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        artist: None | str | Unset
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        album: None | str | Unset
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        popularity: int | None | Unset
        if isinstance(self.popularity, Unset):
            popularity = UNSET
        else:
            popularity = self.popularity

        is_saved = self.is_saved

        last_played_at: None | str | Unset
        if isinstance(self.last_played_at, Unset):
            last_played_at = UNSET
        else:
            last_played_at = self.last_played_at

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connectionId": connection_id,
            "externalId": external_id,
            "sourceProvider": source_provider,
            "mediaType": media_type,
            "title": title,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if artist is not UNSET:
            field_dict["artist"] = artist
        if album is not UNSET:
            field_dict["album"] = album
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if is_saved is not UNSET:
            field_dict["isSaved"] = is_saved
        if last_played_at is not UNSET:
            field_dict["lastPlayedAt"] = last_played_at
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        source_provider = d.pop("sourceProvider")

        media_type = d.pop("mediaType")

        title = d.pop("title")

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_artist(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        artist = _parse_artist(d.pop("artist", UNSET))


        def _parse_album(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        album = _parse_album(d.pop("album", UNSET))


        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("externalUrl", UNSET))


        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))


        def _parse_popularity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        popularity = _parse_popularity(d.pop("popularity", UNSET))


        is_saved = d.pop("isSaved", UNSET)

        def _parse_last_played_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_played_at = _parse_last_played_at(d.pop("lastPlayedAt", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        post_integration_integration_media_items_body = cls(
            connection_id=connection_id,
            external_id=external_id,
            source_provider=source_provider,
            media_type=media_type,
            title=title,
            deleted_at=deleted_at,
            owner_id=owner_id,
            artist=artist,
            album=album,
            image_url=image_url,
            external_url=external_url,
            duration_ms=duration_ms,
            popularity=popularity,
            is_saved=is_saved,
            last_played_at=last_played_at,
            is_deleted=is_deleted,
        )

        return post_integration_integration_media_items_body

