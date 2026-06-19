from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_bucket_schemas_id_body_metadata_type_0_type_1 import PutBucketSchemasIdBodyMetadataType0Type1





T = TypeVar("T", bound="PutBucketSchemasIdBody")



@_attrs_define
class PutBucketSchemasIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            name (str | Unset):
            metadata (bool | float | list[Any] | None | PutBucketSchemasIdBodyMetadataType0Type1 | str | Unset):
     """

    owner_id: str | Unset = UNSET
    name: str | Unset = UNSET
    metadata: bool | float | list[Any] | None | PutBucketSchemasIdBodyMetadataType0Type1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_bucket_schemas_id_body_metadata_type_0_type_1 import PutBucketSchemasIdBodyMetadataType0Type1
        owner_id = self.owner_id

        name = self.name

        metadata: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PutBucketSchemasIdBodyMetadataType0Type1):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, list):
            metadata = self.metadata


        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_bucket_schemas_id_body_metadata_type_0_type_1 import PutBucketSchemasIdBodyMetadataType0Type1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_metadata(data: object) -> bool | float | list[Any] | None | PutBucketSchemasIdBodyMetadataType0Type1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PutBucketSchemasIdBodyMetadataType0Type1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PutBucketSchemasIdBodyMetadataType0Type1 | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        put_bucket_schemas_id_body = cls(
            owner_id=owner_id,
            name=name,
            metadata=metadata,
        )

        return put_bucket_schemas_id_body

