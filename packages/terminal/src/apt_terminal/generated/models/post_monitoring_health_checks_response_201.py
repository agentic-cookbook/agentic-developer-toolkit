from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PostMonitoringHealthChecksResponse201")



@_attrs_define
class PostMonitoringHealthChecksResponse201:
    """ 
        Attributes:
            id (str):
            endpoint_id (str):
            status (str):
            response_time_ms (Union[None, int]):
            status_code (Union[None, int]):
            error_message (Union[None, str]):
            checked_at (str):
     """

    id: str
    endpoint_id: str
    status: str
    response_time_ms: Union[None, int]
    status_code: Union[None, int]
    error_message: Union[None, str]
    checked_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        endpoint_id = self.endpoint_id

        status = self.status

        response_time_ms: Union[None, int]
        response_time_ms = self.response_time_ms

        status_code: Union[None, int]
        status_code = self.status_code

        error_message: Union[None, str]
        error_message = self.error_message

        checked_at = self.checked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "endpointId": endpoint_id,
            "status": status,
            "responseTimeMs": response_time_ms,
            "statusCode": status_code,
            "errorMessage": error_message,
            "checkedAt": checked_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        endpoint_id = d.pop("endpointId")

        status = d.pop("status")

        def _parse_response_time_ms(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        response_time_ms = _parse_response_time_ms(d.pop("responseTimeMs"))


        def _parse_status_code(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        status_code = _parse_status_code(d.pop("statusCode"))


        def _parse_error_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error_message = _parse_error_message(d.pop("errorMessage"))


        checked_at = d.pop("checkedAt")

        post_monitoring_health_checks_response_201 = cls(
            id=id,
            endpoint_id=endpoint_id,
            status=status,
            response_time_ms=response_time_ms,
            status_code=status_code,
            error_message=error_message,
            checked_at=checked_at,
        )

        return post_monitoring_health_checks_response_201

