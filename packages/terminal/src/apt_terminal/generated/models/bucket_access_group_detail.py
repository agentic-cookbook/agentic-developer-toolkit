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
  from ..models.bucket_grant import BucketGrant
  from ..models.bucket_access_group_member import BucketAccessGroupMember
  from ..models.bucket_access_group_metadata_type_0 import BucketAccessGroupMetadataType0





T = TypeVar("T", bound="BucketAccessGroupDetail")



@_attrs_define
class BucketAccessGroupDetail:
    """ 
        Attributes:
            id (str):
            owner_id (str): owning ecosystem
            bucket_id (str):
            name (str):
            description (str):
            kind (str): 'everyone' (seeded) or 'custom'
            created_at (str):
            updated_at (str):
            members (list['BucketAccessGroupMember']):
            grants (list['BucketGrant']):
            metadata (Union['BucketAccessGroupMetadataType0', None, Unset]):
     """

    id: str
    owner_id: str
    bucket_id: str
    name: str
    description: str
    kind: str
    created_at: str
    updated_at: str
    members: list['BucketAccessGroupMember']
    grants: list['BucketGrant']
    metadata: Union['BucketAccessGroupMetadataType0', None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bucket_grant import BucketGrant
        from ..models.bucket_access_group_member import BucketAccessGroupMember
        from ..models.bucket_access_group_metadata_type_0 import BucketAccessGroupMetadataType0
        id = self.id

        owner_id = self.owner_id

        bucket_id = self.bucket_id

        name = self.name

        description = self.description

        kind = self.kind

        created_at = self.created_at

        updated_at = self.updated_at

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)



        grants = []
        for grants_item_data in self.grants:
            grants_item = grants_item_data.to_dict()
            grants.append(grants_item)



        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BucketAccessGroupMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "bucketId": bucket_id,
            "name": name,
            "description": description,
            "kind": kind,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "members": members,
            "grants": grants,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_grant import BucketGrant
        from ..models.bucket_access_group_member import BucketAccessGroupMember
        from ..models.bucket_access_group_metadata_type_0 import BucketAccessGroupMetadataType0
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        bucket_id = d.pop("bucketId")

        name = d.pop("name")

        description = d.pop("description")

        kind = d.pop("kind")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        members = []
        _members = d.pop("members")
        for members_item_data in (_members):
            members_item = BucketAccessGroupMember.from_dict(members_item_data)



            members.append(members_item)


        grants = []
        _grants = d.pop("grants")
        for grants_item_data in (_grants):
            grants_item = BucketGrant.from_dict(grants_item_data)



            grants.append(grants_item)


        def _parse_metadata(data: object) -> Union['BucketAccessGroupMetadataType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BucketAccessGroupMetadataType0.from_dict(data)



                return metadata_type_0
            except: # noqa: E722
                pass
            return cast(Union['BucketAccessGroupMetadataType0', None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        bucket_access_group_detail = cls(
            id=id,
            owner_id=owner_id,
            bucket_id=bucket_id,
            name=name,
            description=description,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
            members=members,
            grants=grants,
            metadata=metadata,
        )


        bucket_access_group_detail.additional_properties = d
        return bucket_access_group_detail

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
