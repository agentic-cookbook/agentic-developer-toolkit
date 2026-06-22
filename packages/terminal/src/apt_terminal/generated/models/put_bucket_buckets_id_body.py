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
  from ..models.put_bucket_buckets_id_body_metadata_type_0_type_1 import PutBucketBucketsIdBodyMetadataType0Type1





T = TypeVar("T", bound="PutBucketBucketsIdBody")



@_attrs_define
class PutBucketBucketsIdBody:
    """ 
        Attributes:
            owner_id (Union[Unset, str]):
            parent_id (Union[None, Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            kind (Union[Unset, str]):
            metadata (Union['PutBucketBucketsIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]):
     """

    owner_id: Union[Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    metadata: Union['PutBucketBucketsIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_bucket_buckets_id_body_metadata_type_0_type_1 import PutBucketBucketsIdBodyMetadataType0Type1
        owner_id = self.owner_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        name = self.name

        description = self.description

        kind = self.kind

        metadata: Union[None, Unset, bool, dict[str, Any], float, list[Any], str]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PutBucketBucketsIdBodyMetadataType0Type1):
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
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_bucket_buckets_id_body_metadata_type_0_type_1 import PutBucketBucketsIdBodyMetadataType0Type1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        kind = d.pop("kind", UNSET)

        def _parse_metadata(data: object) -> Union['PutBucketBucketsIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0_type_1 = PutBucketBucketsIdBodyMetadataType0Type1.from_dict(data)



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
            return cast(Union['PutBucketBucketsIdBodyMetadataType0Type1', None, Unset, bool, float, list[Any], str], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        put_bucket_buckets_id_body = cls(
            owner_id=owner_id,
            parent_id=parent_id,
            name=name,
            description=description,
            kind=kind,
            metadata=metadata,
        )

        return put_bucket_buckets_id_body

