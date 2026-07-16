from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union

if TYPE_CHECKING:
  from ..models.post_bucket_buckets_response_201_metadata_type_0_type_1 import PostBucketBucketsResponse201MetadataType0Type1





T = TypeVar("T", bound="PostBucketBucketsResponse201")



@_attrs_define
class PostBucketBucketsResponse201:
    """ 
        Attributes:
            id (str):
            ecosystem_id (str):
            parent_id (Union[None, str]):
            name (str):
            description (str):
            kind (str):
            metadata (Union['PostBucketBucketsResponse201MetadataType0Type1', None, bool, float, list[Any], str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    ecosystem_id: str
    parent_id: Union[None, str]
    name: str
    description: str
    kind: str
    metadata: Union['PostBucketBucketsResponse201MetadataType0Type1', None, bool, float, list[Any], str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_bucket_buckets_response_201_metadata_type_0_type_1 import PostBucketBucketsResponse201MetadataType0Type1
        id = self.id

        ecosystem_id = self.ecosystem_id

        parent_id: Union[None, str]
        parent_id = self.parent_id

        name = self.name

        description = self.description

        kind = self.kind

        metadata: Union[None, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.metadata, PostBucketBucketsResponse201MetadataType0Type1):
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
            "parentId": parent_id,
            "name": name,
            "description": description,
            "kind": kind,
            "metadata": metadata,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_bucket_buckets_response_201_metadata_type_0_type_1 import PostBucketBucketsResponse201MetadataType0Type1
        d = dict(src_dict)
        id = d.pop("id")

        ecosystem_id = d.pop("ecosystemId")

        def _parse_parent_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        parent_id = _parse_parent_id(d.pop("parentId"))


        name = d.pop("name")

        description = d.pop("description")

        kind = d.pop("kind")

        def _parse_metadata(data: object) -> Union['PostBucketBucketsResponse201MetadataType0Type1', None, bool, float, list[Any], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PostBucketBucketsResponse201MetadataType0Type1.from_dict(data)



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
            return cast(Union['PostBucketBucketsResponse201MetadataType0Type1', None, bool, float, list[Any], str], data)

        metadata = _parse_metadata(d.pop("metadata"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        post_bucket_buckets_response_201 = cls(
            id=id,
            ecosystem_id=ecosystem_id,
            parent_id=parent_id,
            name=name,
            description=description,
            kind=kind,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_bucket_buckets_response_201

