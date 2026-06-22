from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostPersonalPrivacyGrantsBody")



@_attrs_define
class PostPersonalPrivacyGrantsBody:
    """ 
        Attributes:
            target_table (str):
            target_id (str):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            audience_mask (Union[Unset, int]):
     """

    target_table: str
    target_id: str
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    audience_mask: Union[Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        target_table = self.target_table

        target_id = self.target_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        audience_mask = self.audience_mask


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "targetTable": target_table,
            "targetId": target_id,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if audience_mask is not UNSET:
            field_dict["audienceMask"] = audience_mask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_table = d.pop("targetTable")

        target_id = d.pop("targetId")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        audience_mask = d.pop("audienceMask", UNSET)

        post_personal_privacy_grants_body = cls(
            target_table=target_table,
            target_id=target_id,
            deleted_at=deleted_at,
            owner_id=owner_id,
            audience_mask=audience_mask,
        )

        return post_personal_privacy_grants_body

