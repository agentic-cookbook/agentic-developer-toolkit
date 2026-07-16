from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.integration_provider_config_config import IntegrationProviderConfigConfig





T = TypeVar("T", bound="IntegrationProviderConfig")



@_attrs_define
class IntegrationProviderConfig:
    """ 
        Attributes:
            id (UUID):
            ecosystem_id (str): Ecosystem id (the RLS owner)
            provider_id (str):
            config (IntegrationProviderConfigConfig): Non-secret config: clientId, scopes, URLs, endpoints, credentialStyle
            has_secret (bool): Whether a client secret is stored (the value is never returned)
            updated_by (Union[None, Unset, str]):
            created_at (Union[Unset, str]):
            updated_at (Union[Unset, str]):
     """

    id: UUID
    ecosystem_id: str
    provider_id: str
    config: 'IntegrationProviderConfigConfig'
    has_secret: bool
    updated_by: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_provider_config_config import IntegrationProviderConfigConfig
        id = str(self.id)

        ecosystem_id = self.ecosystem_id

        provider_id = self.provider_id

        config = self.config.to_dict()

        has_secret = self.has_secret

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ecosystemId": ecosystem_id,
            "providerId": provider_id,
            "config": config,
            "hasSecret": has_secret,
        })
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_provider_config_config import IntegrationProviderConfigConfig
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        ecosystem_id = d.pop("ecosystemId")

        provider_id = d.pop("providerId")

        config = IntegrationProviderConfigConfig.from_dict(d.pop("config"))




        has_secret = d.pop("hasSecret")

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))


        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        integration_provider_config = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            provider_id=provider_id,
            config=config,
            has_secret=has_secret,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
        )


        integration_provider_config.additional_properties = d
        return integration_provider_config

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
