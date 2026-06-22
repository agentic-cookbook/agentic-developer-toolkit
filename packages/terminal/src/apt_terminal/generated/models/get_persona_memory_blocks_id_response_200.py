from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.get_persona_memory_blocks_id_response_200_content_type_1 import GetPersonaMemoryBlocksIdResponse200ContentType1





T = TypeVar("T", bound="GetPersonaMemoryBlocksIdResponse200")



@_attrs_define
class GetPersonaMemoryBlocksIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            name (str):
            content (Union['GetPersonaMemoryBlocksIdResponse200ContentType1', None, bool, float, list[Any], str]):
            size_limit (Union[None, int]):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: Union[None, str]
    name: str
    content: Union['GetPersonaMemoryBlocksIdResponse200ContentType1', None, bool, float, list[Any], str]
    size_limit: Union[None, int]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_persona_memory_blocks_id_response_200_content_type_1 import GetPersonaMemoryBlocksIdResponse200ContentType1
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        name = self.name

        content: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.content, GetPersonaMemoryBlocksIdResponse200ContentType1):
            content = self.content.to_dict()
        elif isinstance(self.content, list):
            content = self.content


        else:
            content = self.content

        size_limit: Union[None, int]
        size_limit = self.size_limit

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "name": name,
            "content": content,
            "sizeLimit": size_limit,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_persona_memory_blocks_id_response_200_content_type_1 import GetPersonaMemoryBlocksIdResponse200ContentType1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        name = d.pop("name")

        def _parse_content(data: object) -> Union['GetPersonaMemoryBlocksIdResponse200ContentType1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = GetPersonaMemoryBlocksIdResponse200ContentType1.from_dict(data)



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
            return cast(Union['GetPersonaMemoryBlocksIdResponse200ContentType1', None, bool, float, list[Any], str], data)

        content = _parse_content(d.pop("content"))


        def _parse_size_limit(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        size_limit = _parse_size_limit(d.pop("sizeLimit"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_persona_memory_blocks_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            name=name,
            content=content,
            size_limit=size_limit,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_persona_memory_blocks_id_response_200

