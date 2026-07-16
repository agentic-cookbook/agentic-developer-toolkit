from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_template_provider_kind import ProviderTemplateProviderKind
from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.provider_template_model import ProviderTemplateModel





T = TypeVar("T", bound="ProviderTemplate")



@_attrs_define
class ProviderTemplate:
    """ 
        Attributes:
            id (str):
            provider_kind (ProviderTemplateProviderKind):
            name (str):
            base_url (str):
            documentation_url (Union[None, str]):
            status_url (Union[None, str]):
            created_at (str):
            updated_at (str):
            models (list['ProviderTemplateModel']):
     """

    id: str
    provider_kind: ProviderTemplateProviderKind
    name: str
    base_url: str
    documentation_url: Union[None, str]
    status_url: Union[None, str]
    created_at: str
    updated_at: str
    models: list['ProviderTemplateModel']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_template_model import ProviderTemplateModel
        id = self.id

        provider_kind = self.provider_kind.value

        name = self.name

        base_url = self.base_url

        documentation_url: Union[None, str]
        documentation_url = self.documentation_url

        status_url: Union[None, str]
        status_url = self.status_url

        created_at = self.created_at

        updated_at = self.updated_at

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "providerKind": provider_kind,
            "name": name,
            "baseUrl": base_url,
            "documentationUrl": documentation_url,
            "statusUrl": status_url,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "models": models,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_template_model import ProviderTemplateModel
        d = dict(src_dict)
        id = d.pop("id")

        provider_kind = ProviderTemplateProviderKind(d.pop("providerKind"))




        name = d.pop("name")

        base_url = d.pop("baseUrl")

        def _parse_documentation_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl"))


        def _parse_status_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        status_url = _parse_status_url(d.pop("statusUrl"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        models = []
        _models = d.pop("models")
        for models_item_data in (_models):
            models_item = ProviderTemplateModel.from_dict(models_item_data)



            models.append(models_item)


        provider_template = cls(
            id=id,
            provider_kind=provider_kind,
            name=name,
            base_url=base_url,
            documentation_url=documentation_url,
            status_url=status_url,
            created_at=created_at,
            updated_at=updated_at,
            models=models,
        )


        provider_template.additional_properties = d
        return provider_template

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
