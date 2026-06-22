from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentCountersIdBody")



@_attrs_define
class PutContentCountersIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            name (Union[Unset, str]):
            value (Union[Unset, int]):
     """

    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        name = self.name

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        put_content_counters_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            name=name,
            value=value,
        )

        return put_content_counters_id_body

