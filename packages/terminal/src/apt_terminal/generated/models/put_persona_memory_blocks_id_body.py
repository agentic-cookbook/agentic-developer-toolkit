from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.put_persona_memory_blocks_id_body_content_type_1 import PutPersonaMemoryBlocksIdBodyContentType1





T = TypeVar("T", bound="PutPersonaMemoryBlocksIdBody")



@_attrs_define
class PutPersonaMemoryBlocksIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            name (Union[Unset, str]):
            content (Union['PutPersonaMemoryBlocksIdBodyContentType1', None, Unset, bool, float, list[Any], str]):
            size_limit (Union[None, Unset, int]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    content: Union['PutPersonaMemoryBlocksIdBodyContentType1', None, Unset, bool, float, list[Any], str] = UNSET
    size_limit: Union[None, Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_persona_memory_blocks_id_body_content_type_1 import PutPersonaMemoryBlocksIdBodyContentType1
        ecosystem_id = self.ecosystem_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        name = self.name

        content: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, PutPersonaMemoryBlocksIdBodyContentType1):
            content = self.content.to_dict()
        elif isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        size_limit: Union[None, Unset, int]
        if isinstance(self.size_limit, Unset):
            size_limit = UNSET
        else:
            size_limit = self.size_limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if size_limit is not UNSET:
            field_dict["sizeLimit"] = size_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_persona_memory_blocks_id_body_content_type_1 import PutPersonaMemoryBlocksIdBodyContentType1
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

        def _parse_content(data: object) -> Union['PutPersonaMemoryBlocksIdBodyContentType1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = PutPersonaMemoryBlocksIdBodyContentType1.from_dict(data)



                return content_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_2 = cast(list[Any], data)

                return content_type_2
            except: # noqa: E722
                pass
            return cast(Union['PutPersonaMemoryBlocksIdBodyContentType1', None, Unset, bool, float, list[Any], str], data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_size_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_limit = _parse_size_limit(d.pop("sizeLimit", UNSET))


        put_persona_memory_blocks_id_body = cls(
            ecosystem_id=ecosystem_id,
            deleted_at=deleted_at,
            name=name,
            content=content,
            size_limit=size_limit,
        )

        return put_persona_memory_blocks_id_body

