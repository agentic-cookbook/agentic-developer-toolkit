from enum import Enum

class GetCommunityLeaderboardPeriod(str, Enum):
    ALL = "all"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
