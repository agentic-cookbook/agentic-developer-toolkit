from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast, Union






T = TypeVar("T", bound="PutChatChatsIdResponse200")



@_attrs_define
class PutChatChatsIdResponse200:
    """ 
        Attributes:
            id (str):
            owner_user_id (str):
            ecosystem_id (str):
            type_ (str):
            name (str):
            description (str):
            header_image (str):
            header_background_image (str):
            background_image (str):
            state (str):
            security (str):
            model (str):
            persona_slug (Union[None, str]):
            created_at (str):
            updated_at (str):
            deleted_at (Union[None, str]):
     """

    id: str
    owner_user_id: str
    ecosystem_id: str
    type_: str
    name: str
    description: str
    header_image: str
    header_background_image: str
    background_image: str
    state: str
    security: str
    model: str
    persona_slug: Union[None, str]
    created_at: str
    updated_at: str
    deleted_at: Union[None, str]





    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        persona_slug: Union[None, str]
        persona_slug = self.persona_slug

        created_at = self.created_at

        updated_at = self.updated_at

        deleted_at: Union[None, str]
        deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "ownerUserId": owner_user_id,
            "ecosystemId": ecosystem_id,
            "type": type_,
            "name": name,
            "description": description,
            "headerImage": header_image,
            "headerBackgroundImage": header_background_image,
            "backgroundImage": background_image,
            "state": state,
            "security": security,
            "model": model,
            "personaSlug": persona_slug,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "deletedAt": deleted_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        owner_user_id = d.pop("ownerUserId")

        ecosystem_id = d.pop("ecosystemId")

        type_ = d.pop("type")

        name = d.pop("name")

        description = d.pop("description")

        header_image = d.pop("headerImage")

        header_background_image = d.pop("headerBackgroundImage")

        background_image = d.pop("backgroundImage")

        state = d.pop("state")

        security = d.pop("security")

        model = d.pop("model")

        def _parse_persona_slug(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        persona_slug = _parse_persona_slug(d.pop("personaSlug"))


        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_deleted_at(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        deleted_at = _parse_deleted_at(d.pop("deletedAt"))


        put_chat_chats_id_response_200 = cls(
            id=id,
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
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        return put_chat_chats_id_response_200

