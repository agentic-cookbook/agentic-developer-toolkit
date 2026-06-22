from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostUsageUsageCountersBody")



@_attrs_define
class PostUsageUsageCountersBody:
    """ 
        Attributes:
            scope (str):
            principal_id (str):
            period_start (str):
            requests (int):
            bytes_ (int):
     """

    scope: str
    principal_id: str
    period_start: str
    requests: int
    bytes_: int





    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        principal_id = self.principal_id

        period_start = self.period_start

        requests = self.requests

        bytes_ = self.bytes_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope": scope,
            "principalId": principal_id,
            "periodStart": period_start,
            "requests": requests,
            "bytes": bytes_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope")

        principal_id = d.pop("principalId")

        period_start = d.pop("periodStart")

        requests = d.pop("requests")

        bytes_ = d.pop("bytes")

        post_usage_usage_counters_body = cls(
            scope=scope,
            principal_id=principal_id,
            period_start=period_start,
            requests=requests,
            bytes_=bytes_,
        )

        return post_usage_usage_counters_body

