from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentQueuesBody")



@_attrs_define
class PostContentQueuesBody:
    """ 
        Attributes:
            name (str):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    name: str
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_content_queues_body = cls(
            name=name,
            owner_id=owner_id,
            deleted_at=deleted_at,
        )

        return post_content_queues_body

