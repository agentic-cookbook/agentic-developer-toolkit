from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.post_bucket_schema_tables_response_201_metadata_type_0_type_1 import PostBucketSchemaTablesResponse201MetadataType0Type1





T = TypeVar("T", bound="PostBucketSchemaTablesResponse201")



@_attrs_define
class PostBucketSchemaTablesResponse201:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            schema_id (str):
            sql_table_name (str):
            name (str):
            metadata (bool | float | list[Any] | None | PostBucketSchemaTablesResponse201MetadataType0Type1 | str):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    schema_id: str
    sql_table_name: str
    name: str
    metadata: bool | float | list[Any] | None | PostBucketSchemaTablesResponse201MetadataType0Type1 | str
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_bucket_schema_tables_response_201_metadata_type_0_type_1 import PostBucketSchemaTablesResponse201MetadataType0Type1
        id = self.id

        owner_id = self.owner_id

        schema_id = self.schema_id

        sql_table_name = self.sql_table_name

        name = self.name

        metadata: bool | dict[str, Any] | float | list[Any] | None | str
        if isinstance(self.metadata, PostBucketSchemaTablesResponse201MetadataType0Type1):
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
            "schemaId": schema_id,
            "sqlTableName": sql_table_name,
            "name": name,
            "metadata": metadata,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_bucket_schema_tables_response_201_metadata_type_0_type_1 import PostBucketSchemaTablesResponse201MetadataType0Type1
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        schema_id = d.pop("schemaId")

        sql_table_name = d.pop("sqlTableName")

        name = d.pop("name")

        def _parse_metadata(data: object) -> bool | float | list[Any] | None | PostBucketSchemaTablesResponse201MetadataType0Type1 | str:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PostBucketSchemaTablesResponse201MetadataType0Type1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostBucketSchemaTablesResponse201MetadataType0Type1 | str, data)

        metadata = _parse_metadata(d.pop("metadata"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_bucket_schema_tables_response_201 = cls(
            id=id,
            owner_id=owner_id,
            schema_id=schema_id,
            sql_table_name=sql_table_name,
            name=name,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_bucket_schema_tables_response_201

