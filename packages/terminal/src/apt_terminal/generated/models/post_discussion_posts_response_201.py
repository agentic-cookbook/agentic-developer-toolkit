from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostDiscussionPostsResponse201")



@_attrs_define
class PostDiscussionPostsResponse201:
    """ 
        Attributes:
            id (str):
            customer_id (str):
            owner_id (str):
            topic_id (str):
            parent_post_id (Union[None, str]):
            post_number (int):
            body_document_id (Union[None, str]):
            is_deleted (bool):
            created_at (str):
            updated_at (str):
            deleted_at (Union[None, str]):
     """

    id: str
    customer_id: str
    owner_id: str
    topic_id: str
    parent_post_id: Union[None, str]
    post_number: int
    body_document_id: Union[None, str]
    is_deleted: bool
    created_at: str
    updated_at: str
    deleted_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        owner_id = self.owner_id

        topic_id = self.topic_id

        parent_post_id: Union[None, str]
        parent_post_id = self.parent_post_id

        post_number = self.post_number

        body_document_id: Union[None, str]
        body_document_id = self.body_document_id

        is_deleted = self.is_deleted

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "customerId": customer_id,
            "ownerId": owner_id,
            "topicId": topic_id,
            "parentPostId": parent_post_id,
            "postNumber": post_number,
            "bodyDocumentId": body_document_id,
            "isDeleted": is_deleted,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "deletedAt": deleted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        owner_id = d.pop("ownerId")

        topic_id = d.pop("topicId")

        def _parse_parent_post_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_post_id = _parse_parent_post_id(d.pop("parentPostId"))


        post_number = d.pop("postNumber")

        def _parse_body_document_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        body_document_id = _parse_body_document_id(d.pop("bodyDocumentId"))


        is_deleted = d.pop("isDeleted")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        post_discussion_posts_response_201 = cls(
            id=id,
            customer_id=customer_id,
            owner_id=owner_id,
            topic_id=topic_id,
            parent_post_id=parent_post_id,
            post_number=post_number,
            body_document_id=body_document_id,
            is_deleted=is_deleted,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        return post_discussion_posts_response_201

