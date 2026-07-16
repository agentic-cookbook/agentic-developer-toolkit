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
  from ..models.post_bucket_buckets_body_metadata_type_0_type_1 import PostBucketBucketsBodyMetadataType0Type1





T = TypeVar("T", bound="PostBucketBucketsBody")



@_attrs_define
class PostBucketBucketsBody:
    """ 
        Attributes:
            name (str):
            ecosystem_id (Union[Unset, str]):
            parent_id (Union[None, Unset, str]):
            description (Union[Unset, str]):
            kind (Union[Unset, str]):
            metadata (Union['PostBucketBucketsBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]):
            id (Union[Unset, str]):
     """

    name: str
    ecosystem_id: Union[Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    metadata: Union['PostBucketBucketsBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str] = UNSET
    id: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_bucket_buckets_body_metadata_type_0_type_1 import PostBucketBucketsBodyMetadataType0Type1
        name = self.name

        ecosystem_id = self.ecosystem_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        description = self.description

        kind = self.kind

        metadata: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PostBucketBucketsBodyMetadataType0Type1):
            metadata = self.metadata.to_dict()
        elif isinstance(self.metadata, list):
            metadata = self.metadata


        else:
            metadata = self.metadata

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_bucket_buckets_body_metadata_type_0_type_1 import PostBucketBucketsBodyMetadataType0Type1
        d = dict(src_dict)
        name = d.pop("name")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        description = d.pop("description", UNSET)

        kind = d.pop("kind", UNSET)

        def _parse_metadata(data: object) -> Union['PostBucketBucketsBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PostBucketBucketsBodyMetadataType0Type1.from_dict(data)



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
            return cast(Union['PostBucketBucketsBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        id = d.pop("id", UNSET)

        post_bucket_buckets_body = cls(
            name=name,
            ecosystem_id=ecosystem_id,
            parent_id=parent_id,
            description=description,
            kind=kind,
            metadata=metadata,
            id=id,
        )

        return post_bucket_buckets_body

