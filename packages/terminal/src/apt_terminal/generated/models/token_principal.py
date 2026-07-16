from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="TokenPrincipal")



@_attrs_define
class TokenPrincipal:
    """ 
        Attributes:
            id (str):
            slug (str):
            description (str):
            prefix (str): Non-secret leading chars of the secret, for display
            rdid (str): reverse-domain id, e.g. token.<owner-slug>.<name>
            bucket_rdid (str): the token’s own isolated bucket, e.g. storage.<owner-slug>.<name>
            created_at (datetime.datetime):
            expires_at (Union[None, Unset, datetime.datetime]):
            last_used_at (Union[None, Unset, datetime.datetime]):
     """

    id: str
    slug: str
    description: str
    prefix: str
    rdid: str
    bucket_rdid: str
    created_at: datetime.datetime
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    last_used_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        description = self.description

        prefix = self.prefix

        rdid = self.rdid

        bucket_rdid = self.bucket_rdid

        created_at = self.created_at.isoformat()

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        last_used_at: Union[None, Unset, str]
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "slug": slug,
            "description": description,
            "prefix": prefix,
            "rdid": rdid,
            "bucketRdid": bucket_rdid,
            "createdAt": created_at,
        })
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        slug = d.pop("slug")

        description = d.pop("description")

        prefix = d.pop("prefix")

        rdid = d.pop("rdid")

        bucket_rdid = d.pop("bucketRdid")

        created_at = isoparse(d.pop("createdAt"))




        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        def _parse_last_used_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)



                return last_used_at_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt", UNSET))


        token_principal = cls(
            id=id,
            slug=slug,
            description=description,
            prefix=prefix,
            rdid=rdid,
            bucket_rdid=bucket_rdid,
            created_at=created_at,
            expires_at=expires_at,
            last_used_at=last_used_at,
        )


        token_principal.additional_properties = d
        return token_principal

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
