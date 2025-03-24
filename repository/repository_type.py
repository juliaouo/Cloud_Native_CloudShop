from enum import Enum

class RepositoryType(Enum):
    """Type of repository."""
    MEMORY = "memory"
    FILE = "file"