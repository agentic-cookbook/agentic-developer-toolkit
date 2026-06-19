from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_bucket_schemas_response_200_item_metadata_type_0_type_1 import GetBucketSchemasResponse200ItemMetadataType0Type1





T = TypeVar("T", bound="GetBucketSchemasResponse200Item")



@_attrs_define
class GetBucketSchemasResponse200Item:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            name (str):
            metadata (bool | float | GetBucketSchemasResponse200ItemMetadataType0Type1 | list[Any] | None | str):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    name: str
    metadata: bool | float | GetBucketSchemasResponse200ItemMetadataType0Type1 | list[Any] | None | str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_bucket_schemas_response_200_item_metadata_type_0_type_1 import GetBucketSchemasResponse200ItemMetadataType0Type1
        id = self.id

        owner_id = self.owner_id

        name = self.name

        metadata: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.metadata, GetBucketSchemasResponse200ItemMetadataType0Type1):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, list):
            metadata = self.metadata


        else:
            metadata = self.metadata

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "name": name,
            "metadata": metadata,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bucket_schemas_response_200_item_metadata_type_0_type_1 import GetBucketSchemasResponse200ItemMetadataType0Type1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        name = d.pop("name")

        def _parse_metadata(data: object) -> bool | float | GetBucketSchemasResponse200ItemMetadataType0Type1 | list[Any] | None | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = GetBucketSchemasResponse200ItemMetadataType0Type1.from_dict(data)



                return metadata_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_type_0_type_2 = cast(list[Any], data)

                return metadata_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | GetBucketSchemasResponse200ItemMetadataType0Type1 | list[Any] | None | str, data)

        metadata = _parse_metadata(d.pop("metadata"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_bucket_schemas_response_200_item = cls(
            id=id,
            owner_id=owner_id,
            name=name,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_bucket_schemas_response_200_item

