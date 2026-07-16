from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.put_bucket_bucket_types_id_response_200_metadata_type_0_type_1 import PutBucketBucketTypesIdResponse200MetadataType0Type1





T = TypeVar("T", bound="PutBucketBucketTypesIdResponse200")



@_attrs_define
class PutBucketBucketTypesIdResponse200:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            bucket_id (str):
            sql_table_name (str):
            name (str):
            description (str):
            ref_mode (str):
            metadata (Union['PutBucketBucketTypesIdResponse200MetadataType0Type1', None, bool, float, list[Any], str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    bucket_id: str
    sql_table_name: str
    name: str
    description: str
    ref_mode: str
    metadata: Union['PutBucketBucketTypesIdResponse200MetadataType0Type1', None, bool, float, list[Any], str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_bucket_bucket_types_id_response_200_metadata_type_0_type_1 import PutBucketBucketTypesIdResponse200MetadataType0Type1
        id = self.id

        ecosystem_id = self.ecosystem_id

        bucket_id = self.bucket_id

        sql_table_name = self.sql_table_name

        name = self.name

        description = self.description

        ref_mode = self.ref_mode

        metadata: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.metadata, PutBucketBucketTypesIdResponse200MetadataType0Type1):
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
            "ecosystemId": ecosystem_id,
            "bucketId": bucket_id,
            "sqlTableName": sql_table_name,
            "name": name,
            "description": description,
            "refMode": ref_mode,
            "metadata": metadata,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_bucket_bucket_types_id_response_200_metadata_type_0_type_1 import PutBucketBucketTypesIdResponse200MetadataType0Type1
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        bucket_id = d.pop("bucketId")

        sql_table_name = d.pop("sqlTableName")

        name = d.pop("name")

        description = d.pop("description")

        ref_mode = d.pop("refMode")

        def _parse_metadata(data: object) -> Union['PutBucketBucketTypesIdResponse200MetadataType0Type1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PutBucketBucketTypesIdResponse200MetadataType0Type1.from_dict(data)



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
            return cast(Union['PutBucketBucketTypesIdResponse200MetadataType0Type1', None, bool, float, list[Any], str], data)

        metadata = _parse_metadata(d.pop("metadata"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        put_bucket_bucket_types_id_response_200 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            bucket_id=bucket_id,
            sql_table_name=sql_table_name,
            name=name,
            description=description,
            ref_mode=ref_mode,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        return put_bucket_bucket_types_id_response_200

