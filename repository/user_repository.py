from abc import ABC, abstractmethod
from typing import Optional

from domain.user import User


class UserRepository(ABC):
    """Interface for User repositories."""
    @abstractmethod
    def add(self, username: str, user: User) -> None:
        """Add a user to the repository."""
        pass

    @abstractmethod
    def get(self, username: str) -> Optional[User]:
        """Get a user by username."""
        pass

    @abstractmethod
    def delete(self, username: str) -> bool:
        """Delete a user by username."""
        pass

    @abstractmethod
    def exists(self, username: str) -> bool:
        """Check if a user exists."""
        pass
    
    @abstractmethod
    def save(self) -> None:
        """Save data to persistent storage."""
        pass
    
    @abstractmethod
    def load(self) -> None:
        """Load data from persistent storage."""
        pass