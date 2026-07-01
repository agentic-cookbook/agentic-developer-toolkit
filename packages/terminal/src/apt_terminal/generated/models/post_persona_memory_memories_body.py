from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="PostPersonaMemoryMemoriesBody")



@_attrs_define
class PostPersonaMemoryMemoriesBody:
    """ 
        Attributes:
            persona_id (UUID):
            slug (str):
            memory_type (str):
            description (str):
            body (str):
            owner_id (Union[Unset, str]):
            deleted_at (Union[None, Unset, str]):
            scope (Union[Unset, str]):
            subject_table (Union[None, Unset, str]):
            subject_id (Union[None, Unset, str]):
            status (Union[Unset, str]):
            supersedes_id (Union[None, Unset, str]):
            source (Union[Unset, str]):
            confidence (Union[Unset, int]):
            tags (Union[Unset, list[str]]):
            valid_from (Union[None, Unset, str]):
            valid_to (Union[None, Unset, str]):
     """

    persona_id: UUID
    slug: str
    memory_type: str
    description: str
    body: str
    owner_id: Union[Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    subject_table: Union[None, Unset, str] = UNSET
    subject_id: Union[None, Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    supersedes_id: Union[None, Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    confidence: Union[Unset, int] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    valid_from: Union[None, Unset, str] = UNSET
    valid_to: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        persona_id = str(self.persona_id)

        slug = self.slug

        memory_type = self.memory_type

        description = self.description

        body = self.body

        owner_id = self.owner_id

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        scope = self.scope

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

        status = self.status

        supersedes_id: Union[None, Unset, str]
        if isinstance(self.supersedes_id, Unset):
            supersedes_id = UNSET
        else:
            supersedes_id = self.supersedes_id

        source = self.source

        confidence = self.confidence

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags



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


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "personaId": persona_id,
            "slug": slug,
            "memoryType": memory_type,
            "description": description,
            "body": body,
        })
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if scope is not UNSET:
            field_dict["scope"] = scope
        if subject_table is not UNSET:
            field_dict["subjectTable"] = subject_table
        if subject_id is not UNSET:
            field_dict["subjectId"] = subject_id
        if status is not UNSET:
            field_dict["status"] = status
        if supersedes_id is not UNSET:
            field_dict["supersedesId"] = supersedes_id
        if source is not UNSET:
            field_dict["source"] = source
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if tags is not UNSET:
            field_dict["tags"] = tags
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persona_id = UUID(d.pop("personaId"))




        slug = d.pop("slug")

        memory_type = d.pop("memoryType")

        description = d.pop("description")

        body = d.pop("body")

        owner_id = d.pop("ownerId", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        scope = d.pop("scope", UNSET)

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


        status = d.pop("status", UNSET)

        def _parse_supersedes_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        supersedes_id = _parse_supersedes_id(d.pop("supersedesId", UNSET))


        source = d.pop("source", UNSET)

        confidence = d.pop("confidence", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))


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


        post_persona_memory_memories_body = cls(
            persona_id=persona_id,
            slug=slug,
            memory_type=memory_type,
            description=description,
            body=body,
            owner_id=owner_id,
            deleted_at=deleted_at,
            scope=scope,
            subject_table=subject_table,
            subject_id=subject_id,
            status=status,
            supersedes_id=supersedes_id,
            source=source,
            confidence=confidence,
            tags=tags,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        return post_persona_memory_memories_body

