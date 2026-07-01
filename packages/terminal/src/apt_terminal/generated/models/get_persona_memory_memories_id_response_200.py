from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import cast, Union
from uuid import UUID






T = TypeVar("T", bound="GetPersonaMemoryMemoriesIdResponse200")



@_attrs_define
class GetPersonaMemoryMemoriesIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_id (str):
            customer_id (str):
            deleted_at (Union[None, str]):
            persona_id (UUID):
            scope (str):
            slug (str):
            memory_type (str):
            description (str):
            body (str):
            subject_table (Union[None, str]):
            subject_id (Union[None, str]):
            status (str):
            supersedes_id (Union[None, str]):
            source (str):
            confidence (int):
            tags (list[str]):
            valid_from (Union[None, str]):
            valid_to (Union[None, str]):
            recall_count (int):
            last_recalled_at (Union[None, str]):
            embedding (Union[None, list[float]]):
            embedding_model (Union[None, str]):
            created_at (str):
            updated_at (str):
     """

    id: str
    owner_id: str
    customer_id: str
    deleted_at: Union[None, str]
    persona_id: UUID
    scope: str
    slug: str
    memory_type: str
    description: str
    body: str
    subject_table: Union[None, str]
    subject_id: Union[None, str]
    status: str
    supersedes_id: Union[None, str]
    source: str
    confidence: int
    tags: list[str]
    valid_from: Union[None, str]
    valid_to: Union[None, str]
    recall_count: int
    last_recalled_at: Union[None, str]
    embedding: Union[None, list[float]]
    embedding_model: Union[None, str]
    created_at: str
    updated_at: str





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owner_id = self.owner_id

        customer_id = self.customer_id

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at

        persona_id = str(self.persona_id)

        scope = self.scope

        slug = self.slug

        memory_type = self.memory_type

        description = self.description

        body = self.body

        subject_table: Union[None, str]
        subject_table = self.subject_table

        subject_id: Union[None, str]
        subject_id = self.subject_id

        status = self.status

        supersedes_id: Union[None, str]
        supersedes_id = self.supersedes_id

        source = self.source

        confidence = self.confidence

        tags = self.tags



        valid_from: Union[None, str]
        valid_from = self.valid_from

        valid_to: Union[None, str]
        valid_to = self.valid_to

        recall_count = self.recall_count

        last_recalled_at: Union[None, str]
        last_recalled_at = self.last_recalled_at

        embedding: Union[None, list[float]]
        if isinstance(self.embedding, list):
            embedding = self.embedding


        else:
            embedding = self.embedding

        embedding_model: Union[None, str]
        embedding_model = self.embedding_model

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerId": owner_id,
            "customerId": customer_id,
            "deletedAt": deleted_at,
            "personaId": persona_id,
            "scope": scope,
            "slug": slug,
            "memoryType": memory_type,
            "description": description,
            "body": body,
            "subjectTable": subject_table,
            "subjectId": subject_id,
            "status": status,
            "supersedesId": supersedes_id,
            "source": source,
            "confidence": confidence,
            "tags": tags,
            "validFrom": valid_from,
            "validTo": valid_to,
            "recallCount": recall_count,
            "lastRecalledAt": last_recalled_at,
            "embedding": embedding,
            "embeddingModel": embedding_model,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_id = d.pop("ownerId")

        customer_id = d.pop("customerId")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        persona_id = UUID(d.pop("personaId"))




        scope = d.pop("scope")

        slug = d.pop("slug")

        memory_type = d.pop("memoryType")

        description = d.pop("description")

        body = d.pop("body")

        def _parse_subject_table(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_table = _parse_subject_table(d.pop("subjectTable"))


        def _parse_subject_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subject_id = _parse_subject_id(d.pop("subjectId"))


        status = d.pop("status")

        def _parse_supersedes_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        supersedes_id = _parse_supersedes_id(d.pop("supersedesId"))


        source = d.pop("source")

        confidence = d.pop("confidence")

        tags = cast(list[str], d.pop("tags"))


        def _parse_valid_from(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        valid_from = _parse_valid_from(d.pop("validFrom"))


        def _parse_valid_to(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        valid_to = _parse_valid_to(d.pop("validTo"))


        recall_count = d.pop("recallCount")

        def _parse_last_recalled_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_recalled_at = _parse_last_recalled_at(d.pop("lastRecalledAt"))


        def _parse_embedding(data: object) -> Union[None, list[float]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_type_0 = cast(list[float], data)

                return embedding_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, list[float]], data)

        embedding = _parse_embedding(d.pop("embedding"))


        def _parse_embedding_model(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        embedding_model = _parse_embedding_model(d.pop("embeddingModel"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_persona_memory_memories_id_response_200 = cls(
            id=id,
            owner_id=owner_id,
            customer_id=customer_id,
            deleted_at=deleted_at,
            persona_id=persona_id,
            scope=scope,
            slug=slug,
            memory_type=memory_type,
            description=description,
            body=body,
            subject_table=subject_table,
            subject_id=subject_id,
            status=status,
            supersedes_id=supersedes_id,
            source=source,
            confidence=confidence,
            tags=tags,
            valid_from=valid_from,
            valid_to=valid_to,
            recall_count=recall_count,
            last_recalled_at=last_recalled_at,
            embedding=embedding,
            embedding_model=embedding_model,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_persona_memory_memories_id_response_200

