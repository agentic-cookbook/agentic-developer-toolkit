from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="Notification")



@_attrs_define
class Notification:
    """ 
        Attributes:
            id (str):
            user_id (str):
            owner_id (str):
            type_ (str):
            topic_id (str):
            actor_id (str):
            is_read (bool):
            created_at (str):
            customer_id (Union[Unset, str]):
            post_id (Union[None, Unset, str]):
     """

    id: str
    user_id: str
    owner_id: str
    type_: str
    topic_id: str
    actor_id: str
    is_read: bool
    created_at: str
    customer_id: Union[Unset, str] = UNSET
    post_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        owner_id = self.owner_id

        type_ = self.type_

        topic_id = self.topic_id

        actor_id = self.actor_id

        is_read = self.is_read

        created_at = self.created_at

        customer_id = self.customer_id

        post_id: Union[None, Unset, str]
        if isinstance(self.post_id, Unset):
            post_id = UNSET
        else:
            post_id = self.post_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "userId": user_id,
            "ownerId": owner_id,
            "type": type_,
            "topicId": topic_id,
            "actorId": actor_id,
            "isRead": is_read,
            "createdAt": created_at,
        })
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if post_id is not UNSET:
            field_dict["postId"] = post_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        owner_id = d.pop("ownerId")

        type_ = d.pop("type")

        topic_id = d.pop("topicId")

        actor_id = d.pop("actorId")

        is_read = d.pop("isRead")

        created_at = d.pop("createdAt")

        customer_id = d.pop("customerId", UNSET)

        def _parse_post_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_id = _parse_post_id(d.pop("postId", UNSET))


        notification = cls(
            id=id,
            user_id=user_id,
            owner_id=owner_id,
            type_=type_,
            topic_id=topic_id,
            actor_id=actor_id,
            is_read=is_read,
            created_at=created_at,
            customer_id=customer_id,
            post_id=post_id,
        )


        notification.additional_properties = d
        return notification

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
