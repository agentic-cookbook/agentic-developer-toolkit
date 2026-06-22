from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1





T = TypeVar("T", bound="PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody")



@_attrs_define
class PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            capability (Union[Unset, str]):
            config (Union['PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1', None, Unset, bool,
                float, list[Any], str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    capability: Union[Unset, str] = UNSET
    config: Union['PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1', None, Unset, bool, float, list[Any], str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1
        ecosystem_id = self.ecosystem_id

        capability = self.capability

        config: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1):
            config = self.config.to_dict()
        elif isinstance(self.config, list):
            config = self.config


        else:
            config = self.config


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if capability is not UNSET:
            field_dict["capability"] = capability
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        capability = d.pop("capability", UNSET)

        def _parse_config(data: object) -> Union['PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1.from_dict(data)



                return config_type_0_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_type_0_type_2 = cast(list[Any], data)

                return config_type_0_type_2
            except: # noqa: E722
                pass
            return cast(Union['PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityBodyConfigType0Type1', None, Unset, bool, float, list[Any], str], data)

        config = _parse_config(d.pop("config", UNSET))


        put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body = cls(
            ecosystem_id=ecosystem_id,
            capability=capability,
            config=config,
        )

        return put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_body

