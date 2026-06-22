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
            ecosystem_id (str):
            type_ (str):
            thread_id (str):
            actor_id (str):
            is_read (bool):
            created_at (str):
            reply_id (Union[None, Unset, str]):
     """

    id: str
    user_id: str
    ecosystem_id: str
    type_: str
    thread_id: str
    actor_id: str
    is_read: bool
    created_at: str
    reply_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        type_ = self.type_

        thread_id = self.thread_id

        actor_id = self.actor_id

        is_read = self.is_read

        created_at = self.created_at

        reply_id: Union[None, Unset, str]
        if isinstance(self.reply_id, Unset):
            reply_id = UNSET
        else:
            reply_id = self.reply_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "type": type_,
            "threadId": thread_id,
            "actorId": actor_id,
            "isRead": is_read,
            "createdAt": created_at,
        })
        if reply_id is not UNSET:
            field_dict["replyId"] = reply_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        type_ = d.pop("type")

        thread_id = d.pop("threadId")

        actor_id = d.pop("actorId")

        is_read = d.pop("isRead")

        created_at = d.pop("createdAt")

        def _parse_reply_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reply_id = _parse_reply_id(d.pop("replyId", UNSET))


        notification = cls(
            id=id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            type_=type_,
            thread_id=thread_id,
            actor_id=actor_id,
            is_read=is_read,
            created_at=created_at,
            reply_id=reply_id,
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
