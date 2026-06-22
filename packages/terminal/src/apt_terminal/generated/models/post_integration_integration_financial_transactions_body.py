from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostIntegrationIntegrationFinancialTransactionsBody")



@_attrs_define
class PostIntegrationIntegrationFinancialTransactionsBody:
    """ 
        Attributes:
            connection_id (str):
            external_id (str):
            account_id (str):
            amount (str):
            name (str):
            transaction_date (str):
            deleted_at (Union[None, Unset, str]):
            owner_id (Union[Unset, str]):
            account_name (Union[None, Unset, str]):
            institution_name (Union[None, Unset, str]):
            currency (Union[Unset, str]):
            merchant_name (Union[None, Unset, str]):
            category (Union[None, Unset, str]):
            category_detailed (Union[None, Unset, str]):
            authorized_date (Union[None, Unset, str]):
            pending (Union[Unset, bool]):
            logo_url (Union[None, Unset, str]):
            is_deleted (Union[Unset, bool]):
     """

    connection_id: str
    external_id: str
    account_id: str
    amount: str
    name: str
    transaction_date: str
    deleted_at: Union[None, Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    account_name: Union[None, Unset, str] = UNSET
    institution_name: Union[None, Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    merchant_name: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    category_detailed: Union[None, Unset, str] = UNSET
    authorized_date: Union[None, Unset, str] = UNSET
    pending: Union[Unset, bool] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET





    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        external_id = self.external_id

        account_id = self.account_id

        amount = self.amount

        name = self.name

        transaction_date = self.transaction_date

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        owner_id = self.owner_id

        account_name: Union[None, Unset, str]
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        institution_name: Union[None, Unset, str]
        if isinstance(self.institution_name, Unset):
            institution_name = UNSET
        else:
            institution_name = self.institution_name

        currency = self.currency

        merchant_name: Union[None, Unset, str]
        if isinstance(self.merchant_name, Unset):
            merchant_name = UNSET
        else:
            merchant_name = self.merchant_name

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        category_detailed: Union[None, Unset, str]
        if isinstance(self.category_detailed, Unset):
            category_detailed = UNSET
        else:
            category_detailed = self.category_detailed

        authorized_date: Union[None, Unset, str]
        if isinstance(self.authorized_date, Unset):
            authorized_date = UNSET
        else:
            authorized_date = self.authorized_date

        pending = self.pending

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connectionId": connection_id,
            "externalId": external_id,
            "accountId": account_id,
            "amount": amount,
            "name": name,
            "transactionDate": transaction_date,
        })
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if institution_name is not UNSET:
            field_dict["institutionName"] = institution_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if merchant_name is not UNSET:
            field_dict["merchantName"] = merchant_name
        if category is not UNSET:
            field_dict["category"] = category
        if category_detailed is not UNSET:
            field_dict["categoryDetailed"] = category_detailed
        if authorized_date is not UNSET:
            field_dict["authorizedDate"] = authorized_date
        if pending is not UNSET:
            field_dict["pending"] = pending
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connectionId")

        external_id = d.pop("externalId")

        account_id = d.pop("accountId")

        amount = d.pop("amount")

        name = d.pop("name")

        transaction_date = d.pop("transactionDate")

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        owner_id = d.pop("ownerId", UNSET)

        def _parse_account_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        def _parse_institution_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        institution_name = _parse_institution_name(d.pop("institutionName", UNSET))


        currency = d.pop("currency", UNSET)

        def _parse_merchant_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        merchant_name = _parse_merchant_name(d.pop("merchantName", UNSET))


        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))


        def _parse_category_detailed(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_detailed = _parse_category_detailed(d.pop("categoryDetailed", UNSET))


        def _parse_authorized_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authorized_date = _parse_authorized_date(d.pop("authorizedDate", UNSET))


        pending = d.pop("pending", UNSET)

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))


        is_deleted = d.pop("isDeleted", UNSET)

        post_integration_integration_financial_transactions_body = cls(
            connection_id=connection_id,
            external_id=external_id,
            account_id=account_id,
            amount=amount,
            name=name,
            transaction_date=transaction_date,
            deleted_at=deleted_at,
            owner_id=owner_id,
            account_name=account_name,
            institution_name=institution_name,
            currency=currency,
            merchant_name=merchant_name,
            category=category,
            category_detailed=category_detailed,
            authorized_date=authorized_date,
            pending=pending,
            logo_url=logo_url,
            is_deleted=is_deleted,
        )

        return post_integration_integration_financial_transactions_body

