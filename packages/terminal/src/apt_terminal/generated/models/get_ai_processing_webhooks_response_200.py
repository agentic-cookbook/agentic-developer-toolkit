from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.ai_processing_webhook_endpoint import AiProcessingWebhookEndpoint





T = TypeVar("T", bound="GetAiProcessingWebhooksResponse200")



@_attrs_define
class GetAiProcessingWebhooksResponse200:
    """ 
        Attributes:
            endpoints (list['AiProcessingWebhookEndpoint']):
     """

    endpoints: list['AiProcessingWebhookEndpoint']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_processing_webhook_endpoint import AiProcessingWebhookEndpoint
        endpoints = []
        for endpoints_item_data in self.endpoints:
            endpoints_item = endpoints_item_data.to_dict()
            endpoints.append(endpoints_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "endpoints": endpoints,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_processing_webhook_endpoint import AiProcessingWebhookEndpoint
        d = dict(src_dict)
        endpoints = []
        _endpoints = d.pop("endpoints")
        for endpoints_item_data in (_endpoints):
            endpoints_item = AiProcessingWebhookEndpoint.from_dict(endpoints_item_data)



            endpoints.append(endpoints_item)


        get_ai_processing_webhooks_response_200 = cls(
            endpoints=endpoints,
        )


        get_ai_processing_webhooks_response_200.additional_properties = d
        return get_ai_processing_webhooks_response_200

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
