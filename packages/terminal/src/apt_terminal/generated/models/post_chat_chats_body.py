from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostChatChatsBody")



@_attrs_define
class PostChatChatsBody:
    """ 
        Attributes:
            owner_user_id (str):
            ecosystem_id (Union[Unset, str]):
            type_ (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            header_image (Union[Unset, str]):
            header_background_image (Union[Unset, str]):
            background_image (Union[Unset, str]):
            state (Union[Unset, str]):
            security (Union[Unset, str]):
            model (Union[Unset, str]):
            persona_slug (Union[None, Unset, str]):
            deleted_at (Union[None, Unset, str]):
     """

    owner_user_id: str
    ecosystem_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    header_image: Union[Unset, str] = UNSET
    header_background_image: Union[Unset, str] = UNSET
    background_image: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    security: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    persona_slug: Union[None, Unset, str] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET





    def to_dict(self) -> dict[str, Any]:
        owner_user_id = self.owner_user_id

        ecosystem_id = self.ecosystem_id

        type_ = self.type_

        name = self.name

        description = self.description

        header_image = self.header_image

        header_background_image = self.header_background_image

        background_image = self.background_image

        state = self.state

        security = self.security

        model = self.model

        persona_slug: Union[None, Unset, str]
        if isinstance(self.persona_slug, Unset):
            persona_slug = UNSET
        else:
            persona_slug = self.persona_slug

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ownerUserId": owner_user_id,
        })
        if ecosystem_id is not UNSET:
            field_dict["ecosystemId"] = ecosystem_id
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
        owner_user_id = d.pop("ownerUserId")

        ecosystem_id = d.pop("ecosystemId", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        header_image = d.pop("headerImage", UNSET)

        header_background_image = d.pop("headerBackgroundImage", UNSET)

        background_image = d.pop("backgroundImage", UNSET)

        state = d.pop("state", UNSET)

        security = d.pop("security", UNSET)

        model = d.pop("model", UNSET)

        def _parse_persona_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        persona_slug = _parse_persona_slug(d.pop("personaSlug", UNSET))


        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt", UNSET))


        post_chat_chats_body = cls(
            owner_user_id=owner_user_id,
            ecosystem_id=ecosystem_id,
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

        return post_chat_chats_body

