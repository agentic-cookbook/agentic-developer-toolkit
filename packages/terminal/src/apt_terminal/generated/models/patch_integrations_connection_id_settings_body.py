from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="PatchIntegrationsConnectionIdSettingsBody")



@_attrs_define
class PatchIntegrationsConnectionIdSettingsBody:
    """ 
        Attributes:
            gmail_label_ids (Union[Unset, list[str]]): Gmail label ids to sync (default INBOX).
            gmail_window_days (Union[Unset, int]): Days of history to sync (default 30, max 366).
            reddit_subreddits (Union[Unset, list[str]]): Subreddits to watch (name or r/name; max 50).
            reddit_keywords (Union[Unset, list[str]]): Keywords to match within watched subreddits (max 50).
     """

    gmail_label_ids: Union[Unset, list[str]] = UNSET
    gmail_window_days: Union[Unset, int] = UNSET
    reddit_subreddits: Union[Unset, list[str]] = UNSET
    reddit_keywords: Union[Unset, list[str]] = UNSET





    def to_dict(self) -> dict[str, Any]:
        gmail_label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.gmail_label_ids, Unset):
            gmail_label_ids = self.gmail_label_ids



        gmail_window_days = self.gmail_window_days

        reddit_subreddits: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reddit_subreddits, Unset):
            reddit_subreddits = self.reddit_subreddits



        reddit_keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reddit_keywords, Unset):
            reddit_keywords = self.reddit_keywords




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if gmail_label_ids is not UNSET:
            field_dict["gmailLabelIds"] = gmail_label_ids
        if gmail_window_days is not UNSET:
            field_dict["gmailWindowDays"] = gmail_window_days
        if reddit_subreddits is not UNSET:
            field_dict["redditSubreddits"] = reddit_subreddits
        if reddit_keywords is not UNSET:
            field_dict["redditKeywords"] = reddit_keywords

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gmail_label_ids = cast(list[str], d.pop("gmailLabelIds", UNSET))


        gmail_window_days = d.pop("gmailWindowDays", UNSET)

        reddit_subreddits = cast(list[str], d.pop("redditSubreddits", UNSET))


        reddit_keywords = cast(list[str], d.pop("redditKeywords", UNSET))


        patch_integrations_connection_id_settings_body = cls(
            gmail_label_ids=gmail_label_ids,
            gmail_window_days=gmail_window_days,
            reddit_subreddits=reddit_subreddits,
            reddit_keywords=reddit_keywords,
        )

        return patch_integrations_connection_id_settings_body

