from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1





T = TypeVar("T", bound="PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200")



@_attrs_define
class PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200:
    """ 
        Attributes:
            ecosystem_id (str):
            capability (str):
            config (bool | float | list[Any] | None |
                PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1 | str):
            created_at (str):
            updated_at (str):
     """

    ecosystem_id: str
    capability: str
    config: bool | float | list[Any] | None | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1 | str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1
        ecosystem_id = self.ecosystem_id

        capability = self.capability

        config: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.config, PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1):
            config = self.config.to_dict()
        elif isinstance(self.config, list):
            config = self.config


        else:
            config = self.config

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ecosystemId": ecosystem_id,
            "capability": capability,
            "config": config,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200_config_type_0_type_1 import PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId")

        capability = d.pop("capability")

        def _parse_config(data: object) -> bool | float | list[Any] | None | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1.from_dict(data)



                return config_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_type_0_type_2 = cast(list[Any], data)

                return config_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | list[Any] | None | PutEcosystemEcosystemCapabilitiesEcosystemIdCapabilityResponse200ConfigType0Type1 | str, data)

        config = _parse_config(d.pop("config"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200 = cls(
            ecosystem_id=ecosystem_id,
            capability=capability,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_ecosystem_ecosystem_capabilities_ecosystem_id_capability_response_200

