from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="PostPersonaMemoryFactsBody")



@_attrs_define
class PostPersonaMemoryFactsBody:
    """ 
        Attributes:
            persona_id (UUID):
            predicate (str):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            scope (Union[Unset, str]):
            memory_id (Union[None, Unset, str]):
            subject_table (Union[None, Unset, str]):
            subject_id (Union[None, Unset, str]):
            object_table (Union[None, Unset, str]):
            object_id (Union[None, Unset, str]):
            object_value (Union[None, Unset, str]):
            source (Union[Unset, str]):
            confidence (Union[Unset, int]):
            valid_from (Union[None, Unset, str]):
            valid_to (Union[None, Unset, str]):
            status (Union[Unset, str]):
            supersedes_id (Union[None, Unset, str]):
     """

    persona_id: UUID
    predicate: str
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    memory_id: Union[None, Unset, str] = UNSET
    subject_table: Union[None, Unset, str] = UNSET
    subject_id: Union[None, Unset, str] = UNSET
    object_table: Union[None, Unset, str] = UNSET
    object_id: Union[None, Unset, str] = UNSET
    object_value: Union[None, Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    confidence: Union[Unset, int] = UNSET
    valid_from: Union[None, Unset, str] = UNSET
    valid_to: Union[None, Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    supersedes_id: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        persona_id = str(self.persona_id)

        predicate = self.predicate

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        scope = self.scope

        memory_id: Union[None, Unset, str]
        if isinstance(self.memory_id, Unset):
            memory_id = UNSET
        else:
            memory_id = self.memory_id

        subject_table: Union[None, Unset, str]
        if isinstance(self.subject_table, Unset):
            subject_table = UNSET
        else:
            subject_table = self.subject_table

        subject_id: Union[None, Unset, str]
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        else:
            subject_id = self.subject_id

        object_table: Union[None, Unset, str]
        if isinstance(self.object_table, Unset):
            object_table = UNSET
        else:
            object_table = self.object_table

        object_id: Union[None, Unset, str]
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        object_value: Union[None, Unset, str]
        if isinstance(self.object_value, Unset):
            object_value = UNSET
        else:
            object_value = self.object_value

        source = self.source

        confidence = self.confidence

        valid_from: Union[None, Unset, str]
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = self.valid_from

        valid_to: Union[None, Unset, str]
        if isinstance(self.valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = self.valid_to

        status = self.status

        supersedes_id: Union[None, Unset, str]
        if isinstance(self.supersedes_id, Unset):
            supersedes_id = UNSET
        else:
            supersedes_id = self.supersedes_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "personaId": persona_id,
            "predicate": predicate,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if memory_id is not UNSET:
            field_dict["memoryId"] = memory_id
        if subject_table is not UNSET:
            field_dict["subjectTable"] = subject_table
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if object_table is not UNSET:
            field_dict["objectTable"] = object_table
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_value is not UNSET:
            field_dict["objectValue"] = object_value
        if source is not UNSET:
            field_dict["source"] = source
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if status is not UNSET:
            field_dict["status"] = status
        if supersedes_id is not UNSET:
            field_dict["supersedesId"] = supersedes_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persona_id = UUID(d.pop("personaId"))




        predicate = d.pop("predicate")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        scope = d.pop("scope", UNSET)

        def _parse_memory_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        memory_id = _parse_memory_id(d.pop("memoryId", UNSET))


        def _parse_subject_table(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_table = _parse_subject_table(d.pop("subjectTable", UNSET))


        def _parse_subject_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject_id = _parse_subject_id(d.pop("subjectId", UNSET))


        def _parse_object_table(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_table = _parse_object_table(d.pop("objectTable", UNSET))


        def _parse_object_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_id = _parse_object_id(d.pop("objectId", UNSET))


        def _parse_object_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_value = _parse_object_value(d.pop("objectValue", UNSET))


        source = d.pop("source", UNSET)

        confidence = d.pop("confidence", UNSET)

        def _parse_valid_from(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        valid_from = _parse_valid_from(d.pop("validFrom", UNSET))


        def _parse_valid_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        valid_to = _parse_valid_to(d.pop("validTo", UNSET))


        status = d.pop("status", UNSET)

        def _parse_supersedes_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supersedes_id = _parse_supersedes_id(d.pop("supersedesId", UNSET))


        post_persona_memory_facts_body = cls(
            persona_id=persona_id,
            predicate=predicate,
            owner_id=owner_id,
            deleted_at=deleted_at,
            scope=scope,
            memory_id=memory_id,
            subject_table=subject_table,
            subject_id=subject_id,
            object_table=object_table,
            object_id=object_id,
            object_value=object_value,
            source=source,
            confidence=confidence,
            valid_from=valid_from,
            valid_to=valid_to,
            status=status,
            supersedes_id=supersedes_id,
        )

        return post_persona_memory_facts_body

