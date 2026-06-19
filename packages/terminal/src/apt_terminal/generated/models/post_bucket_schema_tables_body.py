from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_bucket_schema_tables_body_metadata_type_0_type_1 import PostBucketSchemaTablesBodyMetadataType0Type1





T = TypeVar("T", bound="PostBucketSchemaTablesBody")



@_attrs_define
class PostBucketSchemaTablesBody:
    """ 
        Attributes:
            schema_id (str):
            sql_table_name (str):
            name (str):
            owner_id (str | Unset):
            metadata (bool | float | list[Any] | None | PostBucketSchemaTablesBodyMetadataType0Type1 | str | Unset):
     """

    schema_id: str
    sql_table_name: str
    name: str
    owner_id: str | Unset = UNSET
    metadata: bool | float | list[Any] | None | PostBucketSchemaTablesBodyMetadataType0Type1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_bucket_schema_tables_body_metadata_type_0_type_1 import PostBucketSchemaTablesBodyMetadataType0Type1
        schema_id = self.schema_id

        sql_table_name = self.sql_table_name

        name = self.name

        owner_id = self.owner_id

        metadata: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PostBucketSchemaTablesBodyMetadataType0Type1):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, list):
            metadata = self.metadata


        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "schemaId": schema_id,
            "sqlTableName": sql_table_name,
            "name": name,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_bucket_schema_tables_body_metadata_type_0_type_1 import PostBucketSchemaTablesBodyMetadataType0Type1
        d = dict(src_dict)
        schema_id = d.pop("schemaId")

        sql_table_name = d.pop("sqlTableName")

        name = d.pop("name")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_metadata(data: object) -> bool | float | list[Any] | None | PostBucketSchemaTablesBodyMetadataType0Type1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PostBucketSchemaTablesBodyMetadataType0Type1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PostBucketSchemaTablesBodyMetadataType0Type1 | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        post_bucket_schema_tables_body = cls(
            schema_id=schema_id,
            sql_table_name=sql_table_name,
            name=name,
            owner_id=owner_id,
            metadata=metadata,
        )

        return post_bucket_schema_tables_body

