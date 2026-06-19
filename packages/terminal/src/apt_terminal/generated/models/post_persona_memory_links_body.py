from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostPersonaMemoryLinksBody")



@_attrs_define
class PostPersonaMemoryLinksBody:
    """ 
        Attributes:
            src_id (str):
            dst_id (str):
            owner_id (str | Unset):
            relation (str | Unset):
     """

    src_id: str
    dst_id: str
    owner_id: str | Unset = UNSET
    relation: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        src_id = self.src_id

        dst_id = self.dst_id

        owner_id = self.owner_id

        relation = self.relation


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "srcId": src_id,
            "dstId": dst_id,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        src_id = d.pop("srcId")

        dst_id = d.pop("dstId")

        owner_id = d.pop("ownerId", UNSET)

        relation = d.pop("relation", UNSET)

        post_persona_memory_links_body = cls(
            src_id=src_id,
            dst_id=dst_id,
            owner_id=owner_id,
            relation=relation,
        )

        return post_persona_memory_links_body

