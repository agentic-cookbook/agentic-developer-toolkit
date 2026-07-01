from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="GetDiscussionNotificationsResponse200Item")



@_attrs_define
class GetDiscussionNotificationsResponse200Item:
    """ 
        Attributes:
            id (str):
            user_id (str):
            owner_id (str):
            customer_id (str):
            type_ (str):
            topic_id (str):
            post_id (Union[None, str]):
            actor_id (str):
            is_read (bool):
            created_at (str):
     """

    id: str
    user_id: str
    owner_id: str
    customer_id: str
    type_: str
    topic_id: str
    post_id: Union[None, str]
    actor_id: str
    is_read: bool
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        owner_id = self.owner_id

        customer_id = self.customer_id

        type_ = self.type_

        topic_id = self.topic_id

        post_id: Union[None, str]
        post_id = self.post_id

        actor_id = self.actor_id

        is_read = self.is_read

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "type": type_,
            "topicId": topic_id,
            "postId": post_id,
            "actorId": actor_id,
            "isRead": is_read,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        type_ = d.pop("type")

        topic_id = d.pop("topicId")

        def _parse_post_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        post_id = _parse_post_id(d.pop("postId"))


        actor_id = d.pop("actorId")

        is_read = d.pop("isRead")

        created_at = d.pop("createdAt")

        get_discussion_notifications_response_200_item = cls(
            id=id,
            user_id=user_id,
            owner_id=owner_id,
            customer_id=customer_id,
            type_=type_,
            topic_id=topic_id,
            post_id=post_id,
            actor_id=actor_id,
            is_read=is_read,
            created_at=created_at,
        )

        return get_discussion_notifications_response_200_item

