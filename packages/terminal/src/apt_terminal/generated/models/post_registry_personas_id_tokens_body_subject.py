from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_registry_personas_id_tokens_body_subject_kind import PostRegistryPersonasIdTokensBodySubjectKind
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PostRegistryPersonasIdTokensBodySubject")



@_attrs_define
class PostRegistryPersonasIdTokensBodySubject:
    """ 
        Attributes:
            kind (PostRegistryPersonasIdTokensBodySubjectKind): `self` (owner-gated) or `user` (the caller lets the persona
                act AS themselves, gated on the persona’s `may_act user` opt-in) or `team` (owner-gated; the persona acts AS the
                team `id` in the target `ecosystemId`, gated on `may_act team` + persona team-membership + the team’s reach into
                that ecosystem). `org` → 400 (not yet supported).
            id (Union[Unset, str]): The team id for a `team` subject (required for `team`). Ignored for `self` (derived from
                the persona) and `user` (always the authenticated caller, never a param).
            ecosystem_id (Union[Unset, str]): The TARGET ecosystem a `team` subject acts in (required for `team`); ignored
                for the other kinds.
     """

    kind: PostRegistryPersonasIdTokensBodySubjectKind
    id: Union[Unset, str] = UNSET
    ecosystem_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        id = self.id

        ecosystem_id = self.ecosystem_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = PostRegistryPersonasIdTokensBodySubjectKind(d.pop("kind"))




        id = d.pop("id", UNSET)

        ecosystem_id = d.pop("ecosystemId", UNSET)

        post_registry_personas_id_tokens_body_subject = cls(
            kind=kind,
            id=id,
            ecosystem_id=ecosystem_id,
        )


        post_registry_personas_id_tokens_body_subject.additional_properties = d
        return post_registry_personas_id_tokens_body_subject

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
