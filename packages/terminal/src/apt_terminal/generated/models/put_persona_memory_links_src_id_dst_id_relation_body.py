from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutPersonaMemoryLinksSrcIdDstIdRelationBody")



@_attrs_define
class PutPersonaMemoryLinksSrcIdDstIdRelationBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            src_id (Union[Unset, str]):
            dst_id (Union[Unset, str]):
            relation (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    src_id: Union[Unset, str] = UNSET
    dst_id: Union[Unset, str] = UNSET
    relation: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        src_id = self.src_id

        dst_id = self.dst_id

        relation = self.relation


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if src_id is not UNSET:
            field_dict["srcId"] = src_id
        if dst_id is not UNSET:
            field_dict["dstId"] = dst_id
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        src_id = d.pop("srcId", UNSET)

        dst_id = d.pop("dstId", UNSET)

        relation = d.pop("relation", UNSET)

        put_persona_memory_links_src_id_dst_id_relation_body = cls(
            ecosystem_id=ecosystem_id,
            src_id=src_id,
            dst_id=dst_id,
            relation=relation,
        )

        return put_persona_memory_links_src_id_dst_id_relation_body

