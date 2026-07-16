from enum import Enum

class PatchProjectProjectsIdStatusesStatusIdBodyCategory(str, Enum):
    DONE = "done"
    IN_PROGRESS = "in_progress"
    TODO = "todo"

    def __str__(self) -> str:
        return str(self.value)
