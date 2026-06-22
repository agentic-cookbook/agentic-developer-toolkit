from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityUserPointsIdBody")



@_attrs_define
class PutCommunityUserPointsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            amount (Union[Unset, int]):
            reason (Union[Unset, str]):
            source_type (Union[Unset, str]):
            source_id (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    amount: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        amount = self.amount

        reason = self.reason

        source_type = self.source_type

        source_id = self.source_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reason is not UNSET:
            field_dict["reason"] = reason
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        amount = d.pop("amount", UNSET)

        reason = d.pop("reason", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_id = d.pop("sourceId", UNSET)

        put_community_user_points_id_body = cls(
            ecosystem_id=ecosystem_id,
            amount=amount,
            reason=reason,
            source_type=source_type,
            source_id=source_id,
        )

        return put_community_user_points_id_body

