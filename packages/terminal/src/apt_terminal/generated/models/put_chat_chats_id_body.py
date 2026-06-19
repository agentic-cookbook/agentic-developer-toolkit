from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PutChatChatsIdBody")



@_attrs_define
class PutChatChatsIdBody:
    """ 
        Attributes:
            owner_user_id (str | Unset):
            owner_id (str | Unset):
            type_ (str | Unset):
            name (str | Unset):
            description (str | Unset):
            header_image (str | Unset):
            header_background_image (str | Unset):
            background_image (str | Unset):
            state (str | Unset):
            security (str | Unset):
            model (str | Unset):
            persona_slug (None | str | Unset):
            deleted_at (None | str | Unset):
     """

    owner_user_id: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    header_image: str | Unset = UNSET
    header_background_image: str | Unset = UNSET
    background_image: str | Unset = UNSET
    state: str | Unset = UNSET
    security: str | Unset = UNSET
    model: str | Unset = UNSET
    persona_slug: None | str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_user_id = self.owner_user_id

        owner_id = self.owner_id

        type_ = self.type_

        name = self.name

        description = self.description

        header_image = self.header_image

        header_background_image = self.header_background_image

        background_image = self.background_image

        state = self.state

        security = self.security

        model = self.model

        persona_slug: None | str | Unset
        if isinstance(self.persona_slug, Unset):
            persona_slug = UNSET
        else:
            persona_slug = self.persona_slug

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if owner_user_id is not UNSET:
            field_dict["ownerUserId"] = owner_user_id
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if header_image is not UNSET:
            field_dict["headerImage"] = header_image
        if header_background_image is not UNSET:
            field_dict["headerBackgroundImage"] = header_background_image
        if background_image is not UNSET:
            field_dict["backgroundImage"] = background_image
        if state is not UNSET:
            field_dict["state"] = state
        if security is not UNSET:
            field_dict["security"] = security
        if model is not UNSET:
            field_dict["model"] = model
        if persona_slug is not UNSET:
            field_dict["personaSlug"] = persona_slug
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_user_id = d.pop("ownerUserId", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        header_image = d.pop("headerImage", UNSET)

        header_background_image = d.pop("headerBackgroundImage", UNSET)

        background_image = d.pop("backgroundImage", UNSET)

        state = d.pop("state", UNSET)

        security = d.pop("security", UNSET)

        model = d.pop("model", UNSET)

        def _parse_persona_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        persona_slug = _parse_persona_slug(d.pop("personaSlug", UNSET))


        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        put_chat_chats_id_body = cls(
            owner_user_id=owner_user_id,
            owner_id=owner_id,
            type_=type_,
            name=name,
            description=description,
            header_image=header_image,
            header_background_image=header_background_image,
            background_image=background_image,
            state=state,
            security=security,
            model=model,
            persona_slug=persona_slug,
            deleted_at=deleted_at,
        )

        return put_chat_chats_id_body

