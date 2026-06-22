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
  from ..models.put_bucket_bucket_types_id_body_metadata_type_0_type_1 import PutBucketBucketTypesIdBodyMetadataType0Type1





T = TypeVar("T", bound="PutBucketBucketTypesIdBody")



@_attrs_define
class PutBucketBucketTypesIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            bucket_id (Union[Unset, str]):
            sql_table_name (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            metadata (Union['PutBucketBucketTypesIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]):
     """

    owner_id: Union[Unset, str] = UNSET
    bucket_id: Union[Unset, str] = UNSET
    sql_table_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    metadata: Union['PutBucketBucketTypesIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_bucket_bucket_types_id_body_metadata_type_0_type_1 import PutBucketBucketTypesIdBodyMetadataType0Type1
        owner_id = self.owner_id

        bucket_id = self.bucket_id

        sql_table_name = self.sql_table_name

        name = self.name

        description = self.description

        metadata: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PutBucketBucketTypesIdBodyMetadataType0Type1):
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
        if bucket_id is not UNSET:
            field_dict["bucketId"] = bucket_id
        if sql_table_name is not UNSET:
            field_dict["sqlTableName"] = sql_table_name
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_bucket_bucket_types_id_body_metadata_type_0_type_1 import PutBucketBucketTypesIdBodyMetadataType0Type1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        bucket_id = d.pop("bucketId", UNSET)

        sql_table_name = d.pop("sqlTableName", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_metadata(data: object) -> Union['PutBucketBucketTypesIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PutBucketBucketTypesIdBodyMetadataType0Type1.from_dict(data)



                return metadata_type_0_type_1
            except: # noqa: E722
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_type_0_type_2 = cast(list[Any], data)

                return metadata_type_0_type_2
            except: # noqa: E722
                pass
            return cast(Union['PutBucketBucketTypesIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        put_bucket_bucket_types_id_body = cls(
            owner_id=owner_id,
            bucket_id=bucket_id,
            sql_table_name=sql_table_name,
            name=name,
            description=description,
            metadata=metadata,
        )

        return put_bucket_bucket_types_id_body

