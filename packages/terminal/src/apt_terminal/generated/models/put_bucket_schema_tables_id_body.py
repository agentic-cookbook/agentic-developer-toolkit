from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_bucket_schema_tables_id_body_metadata_type_0_type_1 import PutBucketSchemaTablesIdBodyMetadataType0Type1





T = TypeVar("T", bound="PutBucketSchemaTablesIdBody")



@_attrs_define
class PutBucketSchemaTablesIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            schema_id (str | Unset):
            sql_table_name (str | Unset):
            name (str | Unset):
            metadata (bool | float | list[Any] | None | PutBucketSchemaTablesIdBodyMetadataType0Type1 | str | Unset):
     """

    owner_id: str | Unset = UNSET
    schema_id: str | Unset = UNSET
    sql_table_name: str | Unset = UNSET
    name: str | Unset = UNSET
    metadata: bool | float | list[Any] | None | PutBucketSchemaTablesIdBodyMetadataType0Type1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_bucket_schema_tables_id_body_metadata_type_0_type_1 import PutBucketSchemaTablesIdBodyMetadataType0Type1
        owner_id = self.owner_id

        schema_id = self.schema_id

        sql_table_name = self.sql_table_name

        name = self.name

        metadata: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PutBucketSchemaTablesIdBodyMetadataType0Type1):
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
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if sql_table_name is not UNSET:
            field_dict["sqlTableName"] = sql_table_name
        if name is not UNSET:
            field_dict["name"] = name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_bucket_schema_tables_id_body_metadata_type_0_type_1 import PutBucketSchemaTablesIdBodyMetadataType0Type1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        sql_table_name = d.pop("sqlTableName", UNSET)

        name = d.pop("name", UNSET)

        def _parse_metadata(data: object) -> bool | float | list[Any] | None | PutBucketSchemaTablesIdBodyMetadataType0Type1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PutBucketSchemaTablesIdBodyMetadataType0Type1.from_dict(data)



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
            return cast(bool | float | list[Any] | None | PutBucketSchemaTablesIdBodyMetadataType0Type1 | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        put_bucket_schema_tables_id_body = cls(
            owner_id=owner_id,
            schema_id=schema_id,
            sql_table_name=sql_table_name,
            name=name,
            metadata=metadata,
        )

        return put_bucket_schema_tables_id_body

