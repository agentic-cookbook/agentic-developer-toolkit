from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutUsageRateLimitTiersIdBody")



@_attrs_define
class PutUsageRateLimitTiersIdBody:
    """ 
        Attributes:
            slug (Union[Unset, str]):
            name (Union[Unset, str]):
            rate_capacity (Union[Unset, int]):
            rate_refill_tokens (Union[Unset, int]):
            rate_refill_seconds (Union[Unset, int]):
            quota_requests (Union[None, Unset, int]):
            quota_bytes (Union[None, Unset, int]):
            quota_period_days (Union[Unset, int]):
            quota_enforced (Union[Unset, bool]):
            is_default (Union[Unset, bool]):
            is_active (Union[Unset, bool]):
     """

    slug: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rate_capacity: Union[Unset, int] = UNSET
    rate_refill_tokens: Union[Unset, int] = UNSET
    rate_refill_seconds: Union[Unset, int] = UNSET
    quota_requests: Union[None, Unset, int] = UNSET
    quota_bytes: Union[None, Unset, int] = UNSET
    quota_period_days: Union[Unset, int] = UNSET
    quota_enforced: Union[Unset, bool] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        rate_capacity = self.rate_capacity

        rate_refill_tokens = self.rate_refill_tokens

        rate_refill_seconds = self.rate_refill_seconds

        quota_requests: Union[None, Unset, int]
        if isinstance(self.quota_requests, Unset):
            quota_requests = UNSET
        else:
            quota_requests = self.quota_requests

        quota_bytes: Union[None, Unset, int]
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
        })
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if rate_capacity is not UNSET:
            field_dict["rateCapacity"] = rate_capacity
        if rate_refill_tokens is not UNSET:
            field_dict["rateRefillTokens"] = rate_refill_tokens
        if rate_refill_seconds is not UNSET:
            field_dict["rateRefillSeconds"] = rate_refill_seconds
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
        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        rate_capacity = d.pop("rateCapacity", UNSET)

        rate_refill_tokens = d.pop("rateRefillTokens", UNSET)

        rate_refill_seconds = d.pop("rateRefillSeconds", UNSET)

        def _parse_quota_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quota_requests = _parse_quota_requests(d.pop("quotaRequests", UNSET))


        def _parse_quota_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quota_bytes = _parse_quota_bytes(d.pop("quotaBytes", UNSET))


        quota_period_days = d.pop("quotaPeriodDays", UNSET)

        quota_enforced = d.pop("quotaEnforced", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_active = d.pop("isActive", UNSET)

        put_usage_rate_limit_tiers_id_body = cls(
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

        return put_usage_rate_limit_tiers_id_body

