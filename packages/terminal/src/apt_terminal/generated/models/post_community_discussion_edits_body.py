from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostCommunityDiscussionEditsBody")



@_attrs_define
class PostCommunityDiscussionEditsBody:
    """ 
        Attributes:
            entity_type (str):
            entity_id (str):
            previous_body (str):
            editor_id (str):
            edited_at (str):
            ecosystem_id (str | Unset):
     """

    entity_type: str
    entity_id: str
    previous_body: str
    editor_id: str
    edited_at: str
    ecosystem_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type

        entity_id = self.entity_id

        previous_body = self.previous_body

        editor_id = self.editor_id

        edited_at = self.edited_at

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "entityType": entity_type,
            "entityId": entity_id,
            "previousBody": previous_body,
            "editorId": editor_id,
            "editedAt": edited_at,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = d.pop("entityType")

        entity_id = d.pop("entityId")

        previous_body = d.pop("previousBody")

        editor_id = d.pop("editorId")

        edited_at = d.pop("editedAt")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_community_discussion_edits_body = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            previous_body=previous_body,
            editor_id=editor_id,
            edited_at=edited_at,
            ecosystem_id=ecosystem_id,
        )

        return post_community_discussion_edits_body

