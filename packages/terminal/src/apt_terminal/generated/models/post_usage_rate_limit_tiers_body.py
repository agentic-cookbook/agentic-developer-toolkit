from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostUsageRateLimitTiersBody")



@_attrs_define
class PostUsageRateLimitTiersBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            rate_capacity (int):
            rate_refill_tokens (int):
            rate_refill_seconds (int):
            quota_requests (int | None | Unset):
            quota_bytes (int | None | Unset):
            quota_period_days (int | Unset):
            quota_enforced (bool | Unset):
            is_default (bool | Unset):
            is_active (bool | Unset):
     """

    slug: str
    name: str
    rate_capacity: int
    rate_refill_tokens: int
    rate_refill_seconds: int
    quota_requests: int | None | Unset = UNSET
    quota_bytes: int | None | Unset = UNSET
    quota_period_days: int | Unset = UNSET
    quota_enforced: bool | Unset = UNSET
    is_default: bool | Unset = UNSET
    is_active: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        rate_capacity = self.rate_capacity

        rate_refill_tokens = self.rate_refill_tokens

        rate_refill_seconds = self.rate_refill_seconds

        quota_requests: int | None | Unset
        if isinstance(self.quota_requests, Unset):
            quota_requests = UNSET
        else:
            quota_requests = self.quota_requests

        quota_bytes: int | None | Unset
        if isinstance(self.quota_bytes, Unset):
            quota_bytes = UNSET
        else:
            quota_bytes = self.quota_bytes

        quota_period_days = self.quota_period_days

        quota_enforced = self.quota_enforced

        is_default = self.is_default

        is_active = self.is_active


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "name": name,
            "rateCapacity": rate_capacity,
            "rateRefillTokens": rate_refill_tokens,
            "rateRefillSeconds": rate_refill_seconds,
        })
        if quota_requests is not UNSET:
            field_dict["quotaRequests"] = quota_requests
        if quota_bytes is not UNSET:
            field_dict["quotaBytes"] = quota_bytes
        if quota_period_days is not UNSET:
            field_dict["quotaPeriodDays"] = quota_period_days
        if quota_enforced is not UNSET:
            field_dict["quotaEnforced"] = quota_enforced
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        rate_capacity = d.pop("rateCapacity")

        rate_refill_tokens = d.pop("rateRefillTokens")

        rate_refill_seconds = d.pop("rateRefillSeconds")

        def _parse_quota_requests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_requests = _parse_quota_requests(d.pop("quotaRequests", UNSET))


        def _parse_quota_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_bytes = _parse_quota_bytes(d.pop("quotaBytes", UNSET))


        quota_period_days = d.pop("quotaPeriodDays", UNSET)

        quota_enforced = d.pop("quotaEnforced", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_active = d.pop("isActive", UNSET)

        post_usage_rate_limit_tiers_body = cls(
            slug=slug,
            name=name,
            rate_capacity=rate_capacity,
            rate_refill_tokens=rate_refill_tokens,
            rate_refill_seconds=rate_refill_seconds,
            quota_requests=quota_requests,
            quota_bytes=quota_bytes,
            quota_period_days=quota_period_days,
            quota_enforced=quota_enforced,
            is_default=is_default,
            is_active=is_active,
        )

        return post_usage_rate_limit_tiers_body

