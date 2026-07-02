from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="IntegrationConnection")



@_attrs_define
class IntegrationConnection:
    """ 
        Attributes:
            id (UUID):
            provider (str): Provider slug (e.g. google-calendar, github)
            service_type (str): Service within the provider (e.g. calendar)
            status (str): active | error | revoked | pending
            display_name (str):
            username (str):
            external_account_id (str): Provider-side account id
            created_at (str):
            last_sync_at (Union[None, Unset, str]): Last successful sync (null = never)
            last_error (Union[None, Unset, str]): Last recorded sync error
     """

    id: UUID
    provider: str
    service_type: str
    status: str
    display_name: str
    username: str
    external_account_id: str
    created_at: str
    last_sync_at: Union[None, Unset, str] = UNSET
    last_error: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        provider = self.provider

        service_type = self.service_type

        status = self.status

        display_name = self.display_name

        username = self.username

        external_account_id = self.external_account_id

        created_at = self.created_at

        last_sync_at: Union[None, Unset, str]
        if isinstance(self.last_sync_at, Unset):
            last_sync_at = UNSET
        else:
            last_sync_at = self.last_sync_at

        last_error: Union[None, Unset, str]
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "provider": provider,
            "serviceType": service_type,
            "status": status,
            "displayName": display_name,
            "username": username,
            "externalAccountId": external_account_id,
            "createdAt": created_at,
        })
        if last_sync_at is not UNSET:
            field_dict["lastSyncAt"] = last_sync_at
        if last_error is not UNSET:
            field_dict["lastError"] = last_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        provider = d.pop("provider")

        service_type = d.pop("serviceType")

        status = d.pop("status")

        display_name = d.pop("displayName")

        username = d.pop("username")

        external_account_id = d.pop("externalAccountId")

        created_at = d.pop("createdAt")

        def _parse_last_sync_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_sync_at = _parse_last_sync_at(d.pop("lastSyncAt", UNSET))


        def _parse_last_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))


        integration_connection = cls(
            id=id,
            provider=provider,
            service_type=service_type,
            status=status,
            display_name=display_name,
            username=username,
            external_account_id=external_account_id,
            created_at=created_at,
            last_sync_at=last_sync_at,
            last_error=last_error,
        )


        integration_connection.additional_properties = d
        return integration_connection

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
