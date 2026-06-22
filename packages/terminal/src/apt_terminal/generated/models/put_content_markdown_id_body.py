from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.put_content_markdown_id_body_author import PutContentMarkdownIdBodyAuthor





T = TypeVar("T", bound="PutContentMarkdownIdBody")



@_attrs_define
class PutContentMarkdownIdBody:
    """ At least one of content/title. Any real change appends a full-state version (author attaches to it); a no-op returns
    the doc unchanged.

        Attributes:
            content (Union[Unset, str]): New raw markdown; a real change bumps current_version.
            title (Union[Unset, str]):
            author (Union[Unset, PutContentMarkdownIdBodyAuthor]): Author of this revision; omit to attribute to the calling
                customer. customer/user are pinned to the caller; other types are caller-asserted (unverified).
     """

    content: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    author: Union[Unset, 'PutContentMarkdownIdBodyAuthor'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_markdown_id_body_author import PutContentMarkdownIdBodyAuthor
        content = self.content

        title = self.title

        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if title is not UNSET:
            field_dict["title"] = title
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_content_markdown_id_body_author import PutContentMarkdownIdBodyAuthor
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        title = d.pop("title", UNSET)

        _author = d.pop("author", UNSET)
        author: Union[Unset, PutContentMarkdownIdBodyAuthor]
        if isinstance(_author,  Unset):
            author = UNSET
        else:
            author = PutContentMarkdownIdBodyAuthor.from_dict(_author)




        put_content_markdown_id_body = cls(
            content=content,
            title=title,
            author=author,
        )


        put_content_markdown_id_body.additional_properties = d
        return put_content_markdown_id_body

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
