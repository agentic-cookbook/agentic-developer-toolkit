from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostBillingSubscriptionTiersBody")



@_attrs_define
class PostBillingSubscriptionTiersBody:
    """ 
        Attributes:
            key (str):
            name (str):
            description (Union[None, Unset, str]):
            display_order (Union[Unset, int]):
            is_active (Union[Unset, bool]):
     """

    key: str
    name: str
    description: Union[None, Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        display_order = self.display_order

        is_active = self.is_active


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))


        display_order = d.pop("displayOrder", UNSET)

        is_active = d.pop("isActive", UNSET)

        post_billing_subscription_tiers_body = cls(
            key=key,
            name=name,
            description=description,
            display_order=display_order,
            is_active=is_active,
        )

        return post_billing_subscription_tiers_body

