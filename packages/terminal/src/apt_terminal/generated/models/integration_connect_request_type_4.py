from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_connect_request_type_4_type import IntegrationConnectRequestType4Type






T = TypeVar("T", bound="IntegrationConnectRequestType4")



@_attrs_define
class IntegrationConnectRequestType4:
    """ 
        Attributes:
            type_ (IntegrationConnectRequestType4Type):
            provider_id (str):
            service_type (str):
            code (str):
            state (str):
     """

    type_: IntegrationConnectRequestType4Type
    provider_id: str
    service_type: str
    code: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        provider_id = self.provider_id

        service_type = self.service_type

        code = self.code

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "providerId": provider_id,
            "serviceType": service_type,
            "code": code,
            "state": state,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = IntegrationConnectRequestType4Type(d.pop("type"))




        provider_id = d.pop("providerId")

        service_type = d.pop("serviceType")

        code = d.pop("code")

        state = d.pop("state")

        integration_connect_request_type_4 = cls(
            type_=type_,
            provider_id=provider_id,
            service_type=service_type,
            code=code,
            state=state,
        )


        integration_connect_request_type_4.additional_properties = d
        return integration_connect_request_type_4

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
