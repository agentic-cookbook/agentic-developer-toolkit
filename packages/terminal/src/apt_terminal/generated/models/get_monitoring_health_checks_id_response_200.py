from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetMonitoringHealthChecksIdResponse200")



@_attrs_define
class GetMonitoringHealthChecksIdResponse200:
    """ 
        Attributes:
            id (str):
            endpoint_id (str):
            status (str):
            response_time_ms (int | None):
            status_code (int | None):
            error_message (None | str):
            checked_at (str):
     """

    id: str
    endpoint_id: str
    status: str
    response_time_ms: int | None
    status_code: int | None
    error_message: None | str
    checked_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        endpoint_id = self.endpoint_id

        status = self.status

        response_time_ms: int | None
        response_time_ms = self.response_time_ms

        status_code: int | None
        status_code = self.status_code

        error_message: None | str
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

        def _parse_response_time_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_time_ms = _parse_response_time_ms(d.pop("responseTimeMs"))


        def _parse_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status_code = _parse_status_code(d.pop("statusCode"))


        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("errorMessage"))


        checked_at = d.pop("checkedAt")

        get_monitoring_health_checks_id_response_200 = cls(
            id=id,
            endpoint_id=endpoint_id,
            status=status,
            response_time_ms=response_time_ms,
            status_code=status_code,
            error_message=error_message,
            checked_at=checked_at,
        )

        return get_monitoring_health_checks_id_response_200

