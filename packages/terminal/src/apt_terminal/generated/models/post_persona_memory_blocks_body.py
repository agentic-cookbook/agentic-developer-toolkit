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
  from ..models.post_persona_memory_blocks_body_content_type_1 import PostPersonaMemoryBlocksBodyContentType1





T = TypeVar("T", bound="PostPersonaMemoryBlocksBody")



@_attrs_define
class PostPersonaMemoryBlocksBody:
    """ 
        Attributes:
            name (str):
            content (Union['PostPersonaMemoryBlocksBodyContentType1', None, bool, float, list[Any], str]):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            size_limit (Union[None, Unset, int]):
     """

    name: str
    content: Union['PostPersonaMemoryBlocksBodyContentType1', None, bool, float, list[Any], str]
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    size_limit: Union[None, Unset, int] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_persona_memory_blocks_body_content_type_1 import PostPersonaMemoryBlocksBodyContentType1
        name = self.name

        content: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.content, PostPersonaMemoryBlocksBodyContentType1):
            content = self.content.to_dict()
        elif isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        size_limit: Union[None, Unset, int]
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

        def _parse_content(data: object) -> Union['PostPersonaMemoryBlocksBodyContentType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = PostPersonaMemoryBlocksBodyContentType1.from_dict(data)



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
            return cast(Union['PostPersonaMemoryBlocksBodyContentType1', None, bool, float, list[Any], str], data)

        content = _parse_content(d.pop("content"))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        def _parse_size_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_limit = _parse_size_limit(d.pop("sizeLimit", UNSET))


        post_persona_memory_blocks_body = cls(
            name=name,
            content=content,
            owner_id=owner_id,
            deleted_at=deleted_at,
            size_limit=size_limit,
        )

        return post_persona_memory_blocks_body

