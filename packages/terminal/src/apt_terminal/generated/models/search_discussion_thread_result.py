from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SearchDiscussionThreadResult")



@_attrs_define
class SearchDiscussionThreadResult:
    """ 
        Attributes:
            id (str):
            title (str):
            body (str):
            author_id (str):
            category_id (str):
            created_at (str):
            rank (float): ts_rank relevance score
     """

    id: str
    title: str
    body: str
    author_id: str
    category_id: str
    created_at: str
    rank: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        body = self.body

        author_id = self.author_id

        category_id = self.category_id

        created_at = self.created_at

        rank = self.rank


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "body": body,
            "authorId": author_id,
            "categoryId": category_id,
            "createdAt": created_at,
            "rank": rank,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        body = d.pop("body")

        author_id = d.pop("authorId")

        category_id = d.pop("categoryId")

        created_at = d.pop("createdAt")

        rank = d.pop("rank")

        search_discussion_thread_result = cls(
            id=id,
            title=title,
            body=body,
            author_id=author_id,
            category_id=category_id,
            created_at=created_at,
            rank=rank,
        )


        search_discussion_thread_result.additional_properties = d
        return search_discussion_thread_result

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
