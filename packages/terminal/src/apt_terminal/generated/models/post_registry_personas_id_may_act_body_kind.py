from enum import Enum

class PostRegistryPersonasIdMayActBodyKind(str, Enum):
    ORG = "org"
    TEAM = "team"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
