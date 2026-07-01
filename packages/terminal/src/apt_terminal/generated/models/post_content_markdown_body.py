from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.post_content_markdown_body_author import PostContentMarkdownBodyAuthor





T = TypeVar("T", bound="PostContentMarkdownBody")



@_attrs_define
class PostContentMarkdownBody:
    """ 
        Attributes:
            content (str): Full raw markdown (stored byte-exact).
            title (Union[Unset, str]): Optional; derived from frontmatter/H1 if omitted.
            category (Union[Unset, str]): Optional classification label.
            tags (Union[Unset, list[str]]): Optional tag set (trimmed + de-duplicated server-side).
            author (Union[Unset, PostContentMarkdownBodyAuthor]): Author of this revision; omit to attribute to the calling
                customer. customer/user are pinned to the caller; other types are caller-asserted (unverified).
     """

    content: str
    title: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    author: Union[Unset, 'PostContentMarkdownBodyAuthor'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_content_markdown_body_author import PostContentMarkdownBodyAuthor
        content = self.content

        title = self.title

        category = self.category

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "content": content,
        })
        if title is not UNSET:
            field_dict["title"] = title
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_content_markdown_body_author import PostContentMarkdownBodyAuthor
        d = dict(src_dict)
        content = d.pop("content")

        title = d.pop("title", UNSET)

        category = d.pop("category", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


        _author = d.pop("author", UNSET)
        author: Union[Unset, PostContentMarkdownBodyAuthor]
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = PostContentMarkdownBodyAuthor.from_dict(_author)




        post_content_markdown_body = cls(
            content=content,
            title=title,
            category=category,
            tags=tags,
            author=author,
        )


        post_content_markdown_body.additional_properties = d
        return post_content_markdown_body

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
