from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_persona_memory_blocks_body_content_type_1 import PostPersonaMemoryBlocksBodyContentType1





T = TypeVar("T", bound="PostPersonaMemoryBlocksBody")



@_attrs_define
class PostPersonaMemoryBlocksBody:
    """ 
        Attributes:
            name (str):
            content (bool | float | list[Any] | None | PostPersonaMemoryBlocksBodyContentType1 | str):
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            size_limit (int | None | Unset):
     """

    name: str
    content: bool | float | list[Any] | None | PostPersonaMemoryBlocksBodyContentType1 | str
    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    size_limit: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_persona_memory_blocks_body_content_type_1 import PostPersonaMemoryBlocksBodyContentType1
        name = self.name

        content: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.content, PostPersonaMemoryBlocksBodyContentType1):
            content = self.content.to_dict()
        elif isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        size_limit: int | None | Unset
        if isinstance(self.size_limit, Unset):
            size_limit = UNSET
        else:
            size_limit = self.size_limit


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "content": content,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if size_limit is not UNSET:
            field_dict["sizeLimit"] = size_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_persona_memory_blocks_body_content_type_1 import PostPersonaMemoryBlocksBodyContentType1
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_content(data: object) -> bool | float | list[Any] | None | PostPersonaMemoryBlocksBodyContentType1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = PostPersonaMemoryBlocksBodyContentType1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostPersonaMemoryBlocksBodyContentType1 | str, data)

        content = _parse_content(d.pop("content"))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_size_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_limit = _parse_size_limit(d.pop("sizeLimit", UNSET))


        post_persona_memory_blocks_body = cls(
            name=name,
            content=content,
            owner_id=owner_id,
            deleted_at=deleted_at,
            size_limit=size_limit,
        )

        return post_persona_memory_blocks_body

