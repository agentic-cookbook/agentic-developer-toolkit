from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.put_content_key_value_pairs_id_body_value_type_1 import PutContentKeyValuePairsIdBodyValueType1





T = TypeVar("T", bound="PutContentKeyValuePairsIdBody")



@_attrs_define
class PutContentKeyValuePairsIdBody:
    """ 
        Attributes:
            owner_id (str | Unset):
            deleted_at (None | str | Unset):
            key (str | Unset):
            value (bool | float | list[Any] | None | PutContentKeyValuePairsIdBodyValueType1 | str | Unset):
     """

    owner_id: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    key: str | Unset = UNSET
    value: bool | float | list[Any] | None | PutContentKeyValuePairsIdBodyValueType1 | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.put_content_key_value_pairs_id_body_value_type_1 import PutContentKeyValuePairsIdBodyValueType1
        owner_id = self.owner_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        key = self.key

        value: bool | dict[str, Any] | float | list[Any] | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PutContentKeyValuePairsIdBodyValueType1):
            value = self.value.to_dict()
        elif isinstance(self.value, list):
            value = self.value


        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.put_content_key_value_pairs_id_body_value_type_1 import PutContentKeyValuePairsIdBodyValueType1
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        key = d.pop("key", UNSET)

        def _parse_value(data: object) -> bool | float | list[Any] | None | PutContentKeyValuePairsIdBodyValueType1 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_1 = PutContentKeyValuePairsIdBodyValueType1.from_dict(data)



                return value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_2 = cast(list[Any], data)

                return value_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | list[Any] | None | PutContentKeyValuePairsIdBodyValueType1 | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))


        put_content_key_value_pairs_id_body = cls(
            owner_id=owner_id,
            deleted_at=deleted_at,
            key=key,
            value=value,
        )

        return put_content_key_value_pairs_id_body

