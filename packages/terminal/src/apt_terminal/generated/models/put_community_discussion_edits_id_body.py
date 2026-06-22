from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PutCommunityDiscussionEditsIdBody")



@_attrs_define
class PutCommunityDiscussionEditsIdBody:
    """ 
        Attributes:
            ecosystem_id (Union[Unset, str]):
            entity_type (Union[Unset, str]):
            entity_id (Union[Unset, str]):
            previous_body (Union[Unset, str]):
            editor_id (Union[Unset, str]):
            edited_at (Union[Unset, str]):
     """

    ecosystem_id: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    previous_body: Union[Unset, str] = UNSET
    editor_id: Union[Unset, str] = UNSET
    edited_at: Union[Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        ecosystem_id = self.ecosystem_id

        entity_type = self.entity_type

        entity_id = self.entity_id

        previous_body = self.previous_body

        editor_id = self.editor_id

        edited_at = self.edited_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if previous_body is not UNSET:
            field_dict["previousBody"] = previous_body
        if editor_id is not UNSET:
            field_dict["editorId"] = editor_id
        if edited_at is not UNSET:
            field_dict["editedAt"] = edited_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ecosystem_id = d.pop("ecosystemId", UNSET)

        entity_type = d.pop("entityType", UNSET)

        entity_id = d.pop("entityId", UNSET)

        previous_body = d.pop("previousBody", UNSET)

        editor_id = d.pop("editorId", UNSET)

        edited_at = d.pop("editedAt", UNSET)

        put_community_discussion_edits_id_body = cls(
            ecosystem_id=ecosystem_id,
            entity_type=entity_type,
            entity_id=entity_id,
            previous_body=previous_body,
            editor_id=editor_id,
            edited_at=edited_at,
        )

        return put_community_discussion_edits_id_body

