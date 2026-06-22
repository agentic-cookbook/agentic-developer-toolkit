from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionReactionsIdBody")



@_attrs_define
class PutCommunityDiscussionReactionsIdBody:
    """ 
        Attributes:
            target_type (Union[Unset, str]):
            target_id (Union[Unset, str]):
            ecosystem_id (Union[Unset, str]):
            emoji (Union[Unset, str]):
     """

    target_type: Union[Unset, str] = UNSET
    target_id: Union[Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    emoji: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type

        target_id = self.target_id

        ecosystem_id = self.ecosystem_id

        emoji = self.emoji


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if emoji is not UNSET:
            field_dict["emoji"] = emoji

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = d.pop("targetType", UNSET)

        target_id = d.pop("targetId", UNSET)

        ecosystem_id = d.pop("ecosystemId", UNSET)

        emoji = d.pop("emoji", UNSET)

        put_community_discussion_reactions_id_body = cls(
            target_type=target_type,
            target_id=target_id,
            ecosystem_id=ecosystem_id,
            emoji=emoji,
        )

        return put_community_discussion_reactions_id_body

