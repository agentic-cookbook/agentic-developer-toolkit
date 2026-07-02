from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_provider_auth_method import IntegrationProviderAuthMethod
from typing import cast






T = TypeVar("T", bound="IntegrationProvider")



@_attrs_define
class IntegrationProvider:
    """ 
        Attributes:
            provider_id (str):
            display_name (str):
            auth_method (IntegrationProviderAuthMethod):
            service_types (list[str]):
            capabilities (list[str]): read | write | auth
            default_poll_interval_ms (int): Default minimum sync interval (ms)
     """

    provider_id: str
    display_name: str
    auth_method: IntegrationProviderAuthMethod
    service_types: list[str]
    capabilities: list[str]
    default_poll_interval_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        display_name = self.display_name

        auth_method = self.auth_method.value

        service_types = self.service_types



        capabilities = self.capabilities



        default_poll_interval_ms = self.default_poll_interval_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "providerId": provider_id,
            "displayName": display_name,
            "authMethod": auth_method,
            "serviceTypes": service_types,
            "capabilities": capabilities,
            "defaultPollIntervalMs": default_poll_interval_ms,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_id = d.pop("providerId")

        display_name = d.pop("displayName")

        auth_method = IntegrationProviderAuthMethod(d.pop("authMethod"))




        service_types = cast(list[str], d.pop("serviceTypes"))


        capabilities = cast(list[str], d.pop("capabilities"))


        default_poll_interval_ms = d.pop("defaultPollIntervalMs")

        integration_provider = cls(
            provider_id=provider_id,
            display_name=display_name,
            auth_method=auth_method,
            service_types=service_types,
            capabilities=capabilities,
            default_poll_interval_ms=default_poll_interval_ms,
        )


        integration_provider.additional_properties = d
        return integration_provider

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
