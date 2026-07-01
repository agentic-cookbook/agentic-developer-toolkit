from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.markdown_document_frontmatter_type_0 import MarkdownDocumentFrontmatterType0





T = TypeVar("T", bound="MarkdownDocument")



@_attrs_define
class MarkdownDocument:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            owner_id (str): Ecosystem (tenant) id.
            title (str):
            content (str): Full raw markdown, byte-exact.
            tags (list[str]): Tag set (defaults to []).
            published (bool): True when readable on the public surface.
            content_hash (str): SHA-256 hex of content (ETag).
            size_bytes (int):
            current_version (int): The current revision number (incremented on every edit).
            created_at (str):
            updated_at (str):
            is_deleted (bool):
            deleted_at (Union[None, Unset, str]):
            frontmatter (Union['MarkdownDocumentFrontmatterType0', None, Unset]):
            category (Union[None, Unset, str]): Optional classification label.
            public_route (Union[None, Unset, str]): Public route slug (non-null iff published); unique per author.
            latest_version_id (Union[None, Unset, str]):
     """

    id: str
    customer_id: str
    owner_id: str
    title: str
    content: str
    tags: list[str]
    published: bool
    content_hash: str
    size_bytes: int
    current_version: int
    created_at: str
    updated_at: str
    is_deleted: bool
    deleted_at: Union[None, Unset, str] = UNSET
    frontmatter: Union['MarkdownDocumentFrontmatterType0', None, Unset] = UNSET
    category: Union[None, Unset, str] = UNSET
    public_route: Union[None, Unset, str] = UNSET
    latest_version_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.markdown_document_frontmatter_type_0 import MarkdownDocumentFrontmatterType0
        id = self.id

        customer_id = self.customer_id

        owner_id = self.owner_id

        title = self.title

        content = self.content

        tags = self.tags



        published = self.published

        content_hash = self.content_hash

        size_bytes = self.size_bytes

        current_version = self.current_version

        created_at = self.created_at

        updated_at = self.updated_at

        is_deleted = self.is_deleted

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        frontmatter: Union[None, Unset, dict[str, Any]]
        if isinstance(self.frontmatter, Unset):
            frontmatter = UNSET
        elif isinstance(self.frontmatter, MarkdownDocumentFrontmatterType0):
            frontmatter = self.frontmatter.to_dict()
        else:
            frontmatter = self.frontmatter

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        public_route: Union[None, Unset, str]
        if isinstance(self.public_route, Unset):
            public_route = UNSET
        else:
            public_route = self.public_route

        latest_version_id: Union[None, Unset, str]
        if isinstance(self.latest_version_id, Unset):
            latest_version_id = UNSET
        else:
            latest_version_id = self.latest_version_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "ownerId": owner_id,
            "title": title,
            "content": content,
            "tags": tags,
            "published": published,
            "contentHash": content_hash,
            "sizeBytes": size_bytes,
            "currentVersion": current_version,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "isDeleted": is_deleted,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if frontmatter is not UNSET:
            field_dict["frontmatter"] = frontmatter
        if category is not UNSET:
            field_dict["category"] = category
        if public_route is not UNSET:
            field_dict["publicRoute"] = public_route
        if latest_version_id is not UNSET:
            field_dict["latestVersionId"] = latest_version_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.markdown_document_frontmatter_type_0 import MarkdownDocumentFrontmatterType0
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        owner_id = d.pop("ownerId")

        title = d.pop("title")

        content = d.pop("content")

        tags = cast(list[str], d.pop("tags"))


        published = d.pop("published")

        content_hash = d.pop("contentHash")

        size_bytes = d.pop("sizeBytes")

        current_version = d.pop("currentVersion")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        is_deleted = d.pop("isDeleted")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_frontmatter(data: object) -> Union['MarkdownDocumentFrontmatterType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                frontmatter_type_0 = MarkdownDocumentFrontmatterType0.from_dict(data)



                return frontmatter_type_0
            except: # noqa: E722
                pass
            return cast(Union['MarkdownDocumentFrontmatterType0', None, Unset], data)

        frontmatter = _parse_frontmatter(d.pop("frontmatter", UNSET))


        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_public_route(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_route = _parse_public_route(d.pop("publicRoute", UNSET))


        def _parse_latest_version_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        latest_version_id = _parse_latest_version_id(d.pop("latestVersionId", UNSET))


        markdown_document = cls(
            id=id,
            customer_id=customer_id,
            owner_id=owner_id,
            title=title,
            content=content,
            tags=tags,
            published=published,
            content_hash=content_hash,
            size_bytes=size_bytes,
            current_version=current_version,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
            frontmatter=frontmatter,
            category=category,
            public_route=public_route,
            latest_version_id=latest_version_id,
        )


        markdown_document.additional_properties = d
        return markdown_document

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
