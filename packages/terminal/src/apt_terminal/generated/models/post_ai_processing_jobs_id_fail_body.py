from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostAiProcessingJobsIdFailBody")



@_attrs_define
class PostAiProcessingJobsIdFailBody:
    """ 
        Attributes:
            lease_token (str): Opaque lease token returned by /claim
            error (str): Human-readable error stored as last_error
            retry (Union[Unset, bool]): Re-queue if attempts remain (default true)
     """

    lease_token: str
    error: str
    retry: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        lease_token = self.lease_token

        error = self.error

        retry = self.retry


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "leaseToken": lease_token,
            "error": error,
        })
        if retry is not UNSET:
            field_dict["retry"] = retry

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lease_token = d.pop("leaseToken")

        error = d.pop("error")

        retry = d.pop("retry", UNSET)

        post_ai_processing_jobs_id_fail_body = cls(
            lease_token=lease_token,
            error=error,
            retry=retry,
        )


        post_ai_processing_jobs_id_fail_body.additional_properties = d
        return post_ai_processing_jobs_id_fail_body

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
