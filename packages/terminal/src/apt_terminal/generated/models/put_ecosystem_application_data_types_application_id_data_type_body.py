from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PutEcosystemApplicationDataTypesApplicationIdDataTypeBody")



@_attrs_define
class PutEcosystemApplicationDataTypesApplicationIdDataTypeBody:
    """ 
        Attributes:
            application_id (str | Unset):
            data_type (str | Unset):
     """

    application_id: str | Unset = UNSET
    data_type: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        data_type = self.data_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if data_type is not UNSET:
            field_dict["dataType"] = data_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_id = d.pop("applicationId", UNSET)

        data_type = d.pop("dataType", UNSET)

        put_ecosystem_application_data_types_application_id_data_type_body = cls(
            application_id=application_id,
            data_type=data_type,
        )

        return put_ecosystem_application_data_types_application_id_data_type_body

