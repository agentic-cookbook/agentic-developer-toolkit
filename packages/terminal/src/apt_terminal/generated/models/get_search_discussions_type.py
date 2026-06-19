from enum import Enum

class GetSearchDiscussionsType(str, Enum):
    REPLIES = "replies"
    THREADS = "threads"

    def __str__(self) -> str:
        return str(self.value)
