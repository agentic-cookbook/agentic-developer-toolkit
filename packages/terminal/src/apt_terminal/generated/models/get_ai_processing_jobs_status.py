from enum import Enum

class GetAiProcessingJobsStatus(str, Enum):
    CLAIMED = "claimed"
    DEAD = "dead"
    QUEUED = "queued"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
