from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






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
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            artist (Union[None, Unset, str]):
            album (Union[None, Unset, str]):
            image_url (Union[None, Unset, str]):
            external_url (Union[None, Unset, str]):
            duration_ms (Union[None, Unset, int]):
            popularity (Union[None, Unset, int]):
            is_saved (Union[Unset, bool]):
            last_played_at (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    connection_id: str
    external_id: str
    source_provider: str
    media_type: str
    title: str
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    artist: Union[None, Unset, str] = UNSET
    album: Union[None, Unset, str] = UNSET
    image_url: Union[None, Unset, str] = UNSET
    external_url: Union[None, Unset, str] = UNSET
    duration_ms: Union[None, Unset, int] = UNSET
    popularity: Union[None, Unset, int] = UNSET
    is_saved: Union[Unset, bool] = UNSET
    last_played_at: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        source_provider = self.source_provider

        media_type = self.media_type

        title = self.title

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        artist: Union[None, Unset, str]
        if isinstance(self.artist, Unset):
            artist = UNSET
        else:
            artist = self.artist

        album: Union[None, Unset, str]
        if isinstance(self.album, Unset):
            album = UNSET
        else:
            album = self.album

        image_url: Union[None, Unset, str]
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        external_url: Union[None, Unset, str]
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        duration_ms: Union[None, Unset, int]
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        popularity: Union[None, Unset, int]
        if isinstance(self.popularity, Unset):
            popularity = UNSET
        else:
            popularity = self.popularity

        is_saved = self.is_saved

        last_played_at: Union[None, Unset, str]
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

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_artist(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist = _parse_artist(d.pop("artist", UNSET))


        def _parse_album(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album = _parse_album(d.pop("album", UNSET))


        def _parse_image_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_url = _parse_image_url(d.pop("imageUrl", UNSET))


        def _parse_external_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_url = _parse_external_url(d.pop("externalUrl", UNSET))


        def _parse_duration_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_ms = _parse_duration_ms(d.pop("durationMs", UNSET))


        def _parse_popularity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        popularity = _parse_popularity(d.pop("popularity", UNSET))


        is_saved = d.pop("isSaved", UNSET)

        def _parse_last_played_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

