from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_ecosystem_ecosystem_capabilities_body_config_type_0_type_1 import PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1





T = TypeVar("T", bound="PostEcosystemEcosystemCapabilitiesBody")



@_attrs_define
class PostEcosystemEcosystemCapabilitiesBody:
    """ 
        Attributes:
            capability (str):
            ecosystem_id (str | Unset):
            config (bool | float | list[Any] | None | PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1 | str | Unset):
     """

    capability: str
    ecosystem_id: str | Unset = UNSET
    config: bool | float | list[Any] | None | PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_ecosystem_ecosystem_capabilities_body_config_type_0_type_1 import PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1
        capability = self.capability

        ecosystem_id = self.ecosystem_id

        config: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1):
            config = self.config.to_dict()
        elif isinstance(self.config, list):
            config = self.config


        else:
            config = self.config


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "capability": capability,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_ecosystem_ecosystem_capabilities_body_config_type_0_type_1 import PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1
        d = dict(src_dict)
        capability = d.pop("capability")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_config(data: object) -> bool | float | list[Any] | None | PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostEcosystemEcosystemCapabilitiesBodyConfigType0Type1 | str | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        post_ecosystem_ecosystem_capabilities_body = cls(
            capability=capability,
            ecosystem_id=ecosystem_id,
            config=config,
        )

        return post_ecosystem_ecosystem_capabilities_body

