from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.registry_agent_mcp_server import RegistryAgentMcpServer





T = TypeVar("T", bound="GetRegistryMcpServersResponse200")



@_attrs_define
class GetRegistryMcpServersResponse200:
    """ 
        Attributes:
            servers (list['RegistryAgentMcpServer']):
     """

    servers: list['RegistryAgentMcpServer']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.registry_agent_mcp_server import RegistryAgentMcpServer
        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()
            servers.append(servers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "servers": servers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registry_agent_mcp_server import RegistryAgentMcpServer
        d = dict(src_dict)
        servers = []
        _servers = d.pop("servers")
        for servers_item_data in (_servers):
            servers_item = RegistryAgentMcpServer.from_dict(servers_item_data)



            servers.append(servers_item)


        get_registry_mcp_servers_response_200 = cls(
            servers=servers,
        )


        get_registry_mcp_servers_response_200.additional_properties = d
        return get_registry_mcp_servers_response_200

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
