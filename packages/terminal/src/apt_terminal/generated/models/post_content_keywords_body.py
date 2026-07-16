from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostContentKeywordsBody")



@_attrs_define
class PostContentKeywordsBody:
    """ 
        Attributes:
            label (str):
            deleted_at (Union[None, Unset, str]):
            ecosystem_id (Union[Unset, str]):
            color (Union[Unset, str]):
            description (Union[Unset, str]):
     """

    label: str
    deleted_at: Union[None, Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        label = self.label

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        ecosystem_id = self.ecosystem_id

        color = self.color

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "label": label,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        ecosystem_id = d.pop("ecosystemId", UNSET)

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        post_content_keywords_body = cls(
            label=label,
            deleted_at=deleted_at,
            ecosystem_id=ecosystem_id,
            color=color,
            description=description,
        )

        return post_content_keywords_body

