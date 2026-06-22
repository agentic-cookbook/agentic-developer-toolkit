from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutUsagePrincipalTiersScopePrincipalIdBody")



@_attrs_define
class PutUsagePrincipalTiersScopePrincipalIdBody:
    """ 
        Attributes:
            scope (Union[Unset, str]):
            principal_id (Union[Unset, str]):
            tier_id (Union[Unset, str]):
     """

    scope: Union[Unset, str] = UNSET
    principal_id: Union[Unset, str] = UNSET
    tier_id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        principal_id = self.principal_id

        tier_id = self.tier_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if scope is not UNSET:
            field_dict["scope"] = scope
        if principal_id is not UNSET:
            field_dict["principalId"] = principal_id
        if tier_id is not UNSET:
            field_dict["tierId"] = tier_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope = d.pop("scope", UNSET)

        principal_id = d.pop("principalId", UNSET)

        tier_id = d.pop("tierId", UNSET)

        put_usage_principal_tiers_scope_principal_id_body = cls(
            scope=scope,
            principal_id=principal_id,
            tier_id=tier_id,
        )

        return put_usage_principal_tiers_scope_principal_id_body

