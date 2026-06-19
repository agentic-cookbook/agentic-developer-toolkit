from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_discussion_reply_result import SearchDiscussionReplyResult
  from ..models.search_discussion_thread_result import SearchDiscussionThreadResult





T = TypeVar("T", bound="GetSearchDiscussionsResponse200")



@_attrs_define
class GetSearchDiscussionsResponse200:
    """ 
        Attributes:
            threads (list[SearchDiscussionThreadResult]):
            replies (list[SearchDiscussionReplyResult]):
            page (int):
            page_size (int):
            threads_has_more (bool):
            replies_has_more (bool):
     """

    threads: list[SearchDiscussionThreadResult]
    replies: list[SearchDiscussionReplyResult]
    page: int
    page_size: int
    threads_has_more: bool
    replies_has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_discussion_reply_result import SearchDiscussionReplyResult
        from ..models.search_discussion_thread_result import SearchDiscussionThreadResult
        threads = []
        for threads_item_data in self.threads:
            threads_item = threads_item_data.to_dict()
            threads.append(threads_item)



        replies = []
        for replies_item_data in self.replies:
            replies_item = replies_item_data.to_dict()
            replies.append(replies_item)



        page = self.page

        page_size = self.page_size

        threads_has_more = self.threads_has_more

        replies_has_more = self.replies_has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "threads": threads,
            "replies": replies,
            "page": page,
            "pageSize": page_size,
            "threadsHasMore": threads_has_more,
            "repliesHasMore": replies_has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_discussion_reply_result import SearchDiscussionReplyResult
        from ..models.search_discussion_thread_result import SearchDiscussionThreadResult
        d = dict(src_dict)
        threads = []
        _threads = d.pop("threads")
        for threads_item_data in (_threads):
            threads_item = SearchDiscussionThreadResult.from_dict(threads_item_data)



            threads.append(threads_item)


        replies = []
        _replies = d.pop("replies")
        for replies_item_data in (_replies):
            replies_item = SearchDiscussionReplyResult.from_dict(replies_item_data)



            replies.append(replies_item)


        page = d.pop("page")

        page_size = d.pop("pageSize")

        threads_has_more = d.pop("threadsHasMore")

        replies_has_more = d.pop("repliesHasMore")

        get_search_discussions_response_200 = cls(
            threads=threads,
            replies=replies,
            page=page,
            page_size=page_size,
            threads_has_more=threads_has_more,
            replies_has_more=replies_has_more,
        )


        get_search_discussions_response_200.additional_properties = d
        return get_search_discussions_response_200

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
