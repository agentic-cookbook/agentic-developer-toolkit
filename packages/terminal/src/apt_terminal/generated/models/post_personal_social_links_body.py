from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalSocialLinksBody")



@_attrs_define
class PostPersonalSocialLinksBody:
    """ 
        Attributes:
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            platform (Union[Unset, str]):
            url (Union[Unset, str]):
            handle (Union[Unset, str]):
            sort_order (Union[Unset, int]):
     """

    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    handle: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        platform = self.platform

        url = self.url

        handle = self.handle

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if url is not UNSET:
            field_dict["url"] = url
        if handle is not UNSET:
            field_dict["handle"] = handle
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

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

        platform = d.pop("platform", UNSET)

        url = d.pop("url", UNSET)

        handle = d.pop("handle", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        post_personal_social_links_body = cls(
            deleted_at=deleted_at,
            owner_id=owner_id,
            platform=platform,
            url=url,
            handle=handle,
            sort_order=sort_order,
        )

        return post_personal_social_links_body

