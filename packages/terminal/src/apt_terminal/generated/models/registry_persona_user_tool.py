from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="RegistryPersonaUserTool")



@_attrs_define
class RegistryPersonaUserTool:
    """ 
        Attributes:
            tool_name (str):
            source (Union[None, str]): null for curated internal tools; else the source id (e.g. "web", "mcp.<server>")
            read_only (bool):
            allowed (bool): true iff the calling user has allowed the persona to invoke this tool for them
     """

    tool_name: str
    source: Union[None, str]
    read_only: bool
    allowed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tool_name = self.tool_name

        source: Union[None, str]
        source = self.source

        read_only = self.read_only

        allowed = self.allowed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "toolName": tool_name,
            "source": source,
            "readOnly": read_only,
            "allowed": allowed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tool_name = d.pop("toolName")

        def _parse_source(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        source = _parse_source(d.pop("source"))


        read_only = d.pop("readOnly")

        allowed = d.pop("allowed")

        registry_persona_user_tool = cls(
            tool_name=tool_name,
            source=source,
            read_only=read_only,
            allowed=allowed,
        )


        registry_persona_user_tool.additional_properties = d
        return registry_persona_user_tool

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
