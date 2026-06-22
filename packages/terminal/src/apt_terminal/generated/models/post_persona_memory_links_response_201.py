from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostPersonaMemoryLinksResponse201")



@_attrs_define
class PostPersonaMemoryLinksResponse201:
    """ 
        Attributes:
            owner_id (str):
            src_id (str):
            dst_id (str):
            relation (str):
            created_at (str):
     """

    owner_id: str
    src_id: str
    dst_id: str
    relation: str
    created_at: str





    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        src_id = self.src_id

        dst_id = self.dst_id

        relation = self.relation

        created_at = self.created_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ownerId": owner_id,
            "srcId": src_id,
            "dstId": dst_id,
            "relation": relation,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId")

        src_id = d.pop("srcId")

        dst_id = d.pop("dstId")

        relation = d.pop("relation")

        created_at = d.pop("createdAt")

        post_persona_memory_links_response_201 = cls(
            owner_id=owner_id,
            src_id=src_id,
            dst_id=dst_id,
            relation=relation,
            created_at=created_at,
        )

        return post_persona_memory_links_response_201

