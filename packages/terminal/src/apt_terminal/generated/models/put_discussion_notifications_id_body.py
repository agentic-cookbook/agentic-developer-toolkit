from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutDiscussionNotificationsIdBody")



@_attrs_define
class PutDiscussionNotificationsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            type_ (Union[Unset, str]):
            topic_id (Union[Unset, str]):
            post_id (Union[None, Unset, str]):
            actor_id (Union[Unset, str]):
            is_read (Union[Unset, bool]):
     """

    owner_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    topic_id: Union[Unset, str] = UNSET
    post_id: Union[None, Unset, str] = UNSET
    actor_id: Union[Unset, str] = UNSET
    is_read: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        type_ = self.type_

        topic_id = self.topic_id

        post_id: Union[None, Unset, str]
        if isinstance(self.post_id, Unset):
            post_id = UNSET
        else:
            post_id = self.post_id

        actor_id = self.actor_id

        is_read = self.is_read


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if topic_id is not UNSET:
            field_dict["topicId"] = topic_id
        if post_id is not UNSET:
            field_dict["postId"] = post_id
        if actor_id is not UNSET:
            field_dict["actorId"] = actor_id
        if is_read is not UNSET:
            field_dict["isRead"] = is_read

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        type_ = d.pop("type", UNSET)

        topic_id = d.pop("topicId", UNSET)

        def _parse_post_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_id = _parse_post_id(d.pop("postId", UNSET))


        actor_id = d.pop("actorId", UNSET)

        is_read = d.pop("isRead", UNSET)

        put_discussion_notifications_id_body = cls(
            owner_id=owner_id,
            type_=type_,
            topic_id=topic_id,
            post_id=post_id,
            actor_id=actor_id,
            is_read=is_read,
        )

        return put_discussion_notifications_id_body

