from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PutContentQueuesIdBody")



@_attrs_define
class PutContentQueuesIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            name (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        name = d.pop("name", UNSET)

        put_content_queues_id_body = cls(
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
            name=name,
        )

        return put_content_queues_id_body

