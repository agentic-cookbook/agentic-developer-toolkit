from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_persona_memory_blocks_id_body_content_type_1 import PutPersonaMemoryBlocksIdBodyContentType1





T = TypeVar("T", bound="PutPersonaMemoryBlocksIdBody")



@_attrs_define
class PutPersonaMemoryBlocksIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            name (str | Unset):
            content (bool | float | list[Any] | None | PutPersonaMemoryBlocksIdBodyContentType1 | str | Unset):
            size_limit (int | None | Unset):
     """

    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    name: str | Unset = UNSET
    content: bool | float | list[Any] | None | PutPersonaMemoryBlocksIdBodyContentType1 | str | Unset = UNSET
    size_limit: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_persona_memory_blocks_id_body_content_type_1 import PutPersonaMemoryBlocksIdBodyContentType1
        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        name = self.name

        content: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, PutPersonaMemoryBlocksIdBodyContentType1):
            content = self.content.to_dict()
        elif isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        size_limit: int | None | Unset
        if isinstance(self.size_limit, Unset):
            size_limit = UNSET
        else:
            size_limit = self.size_limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
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
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        name = d.pop("name", UNSET)

        def _parse_content(data: object) -> bool | float | list[Any] | None | PutPersonaMemoryBlocksIdBodyContentType1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = PutPersonaMemoryBlocksIdBodyContentType1.from_dict(data)



                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_2 = cast(list[Any], data)

                return content_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | list[Any] | None | PutPersonaMemoryBlocksIdBodyContentType1 | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_size_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_limit = _parse_size_limit(d.pop("sizeLimit", UNSET))


        put_persona_memory_blocks_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            name=name,
            content=content,
            size_limit=size_limit,
        )

        return put_persona_memory_blocks_id_body

