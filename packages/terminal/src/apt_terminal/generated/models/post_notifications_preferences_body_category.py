from enum import Enum

class PostNotificationsPreferencesBodyCategory(str, Enum):
    ACCOUNT = "account"
    ADMIN_ANNOUNCEMENT = "admin_announcement"
    COMMUNITY_MENTION = "community_mention"
    COMMUNITY_REPLY = "community_reply"
    DIRECT_MESSAGE = "direct_message"

    def __str__(self) -> str:
        return str(self.value)
