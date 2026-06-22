from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostCommunityUserPointsBody")



@_attrs_define
class PostCommunityUserPointsBody:
    """ 
        Attributes:
            amount (int):
            reason (str):
            source_type (str):
            source_id (str):
            ecosystem_id (Union[Unset, str]):
     """

    amount: int
    reason: str
    source_type: str
    source_id: str
    ecosystem_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        reason = self.reason

        source_type = self.source_type

        source_id = self.source_id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "amount": amount,
            "reason": reason,
            "sourceType": source_type,
            "sourceId": source_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        reason = d.pop("reason")

        source_type = d.pop("sourceType")

        source_id = d.pop("sourceId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_user_points_body = cls(
            amount=amount,
            reason=reason,
            source_type=source_type,
            source_id=source_id,
            ecosystem_id=ecosystem_id,
        )

        return post_community_user_points_body

