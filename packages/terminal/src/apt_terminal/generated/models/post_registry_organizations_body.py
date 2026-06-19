from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostRegistryOrganizationsBody")



@_attrs_define
class PostRegistryOrganizationsBody:
    """ 
        Attributes:
            slug (str):
            name (str):
            namespace (str): The reverse-domain prefix the org's namespace will own
            default_ecosystem_slug (str | Unset):  Default: 'default'.
     """

    slug: str
    name: str
    namespace: str
    default_ecosystem_slug: str | Unset = 'default'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        namespace = self.namespace

        default_ecosystem_slug = self.default_ecosystem_slug


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slug": slug,
            "name": name,
            "namespace": namespace,
        })
        if default_ecosystem_slug is not UNSET:
            field_dict["defaultEcosystemSlug"] = default_ecosystem_slug

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        namespace = d.pop("namespace")

        default_ecosystem_slug = d.pop("defaultEcosystemSlug", UNSET)

        post_registry_organizations_body = cls(
            slug=slug,
            name=name,
            namespace=namespace,
            default_ecosystem_slug=default_ecosystem_slug,
        )


        post_registry_organizations_body.additional_properties = d
        return post_registry_organizations_body

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
