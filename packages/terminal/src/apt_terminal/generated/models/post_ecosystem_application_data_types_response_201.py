from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostEcosystemApplicationDataTypesResponse201")



@_attrs_define
class PostEcosystemApplicationDataTypesResponse201:
    """ 
        Attributes:
            application_id (str):
            data_type (str):
     """

    application_id: str
    data_type: str





    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        data_type = self.data_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "applicationId": application_id,
            "dataType": data_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_id = d.pop("applicationId")

        data_type = d.pop("dataType")

        post_ecosystem_application_data_types_response_201 = cls(
            application_id=application_id,
            data_type=data_type,
        )

        return post_ecosystem_application_data_types_response_201

