from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetCommunityUserPointsIdResponse200")



@_attrs_define
class GetCommunityUserPointsIdResponse200:
    """ 
        Attributes:
            id (str):
            user_id (str):
            ecosystem_id (str):
            amount (int):
            reason (str):
            source_type (str):
            source_id (str):
            created_at (str):
     """

    id: str
    user_id: str
    ecosystem_id: str
    amount: int
    reason: str
    source_type: str
    source_id: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        ecosystem_id = self.ecosystem_id

        amount = self.amount

        reason = self.reason

        source_type = self.source_type

        source_id = self.source_id

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "userId": user_id,
            "ecosystemId": ecosystem_id,
            "amount": amount,
            "reason": reason,
            "sourceType": source_type,
            "sourceId": source_id,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("userId")

        ecosystem_id = d.pop("ecosystemId")

        amount = d.pop("amount")

        reason = d.pop("reason")

        source_type = d.pop("sourceType")

        source_id = d.pop("sourceId")

        created_at = d.pop("createdAt")

        get_community_user_points_id_response_200 = cls(
            id=id,
            user_id=user_id,
            ecosystem_id=ecosystem_id,
            amount=amount,
            reason=reason,
            source_type=source_type,
            source_id=source_id,
            created_at=created_at,
        )

        return get_community_user_points_id_response_200

