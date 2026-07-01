from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDiscussionPostsBody")



@_attrs_define
class PostDiscussionPostsBody:
    """ 
        Attributes:
            topic_id (str):
            post_number (int):
            owner_id (Union[Unset, str]):
            parent_post_id (Union[None, Unset, str]):
            body_document_id (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
            deleted_at (Union[None, Unset, str]):
     """

    topic_id: str
    post_number: int
    owner_id: Union[Unset, str] = UNSET
    parent_post_id: Union[None, Unset, str] = UNSET
    body_document_id: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        topic_id = self.topic_id

        post_number = self.post_number

        owner_id = self.owner_id

        parent_post_id: Union[None, Unset, str]
        if isinstance(self.parent_post_id, Unset):
            parent_post_id = UNSET
        else:
            parent_post_id = self.parent_post_id

        body_document_id: Union[None, Unset, str]
        if isinstance(self.body_document_id, Unset):
            body_document_id = UNSET
        else:
            body_document_id = self.body_document_id

        is_deleted = self.is_deleted

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "topicId": topic_id,
            "postNumber": post_number,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_post_id is not UNSET:
            field_dict["parentPostId"] = parent_post_id
        if body_document_id is not UNSET:
            field_dict["bodyDocumentId"] = body_document_id
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic_id = d.pop("topicId")

        post_number = d.pop("postNumber")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_parent_post_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_post_id = _parse_parent_post_id(d.pop("parentPostId", UNSET))


        def _parse_body_document_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        body_document_id = _parse_body_document_id(d.pop("bodyDocumentId", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_discussion_posts_body = cls(
            topic_id=topic_id,
            post_number=post_number,
            owner_id=owner_id,
            parent_post_id=parent_post_id,
            body_document_id=body_document_id,
            is_deleted=is_deleted,
            deleted_at=deleted_at,
        )

        return post_discussion_posts_body

