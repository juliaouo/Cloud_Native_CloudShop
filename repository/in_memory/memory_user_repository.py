from typing import Dict, Optional

from domain import User
from repository.user_repository import UserRepository


class MemoryUserRepository(UserRepository):
    """Repository for User entities using in-memory storage."""
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add(self, username: str, user: User) -> None:
        self.users[username.lower()] = user

    def get(self, username: str) -> Optional[User]:
        return self.users.get(username.lower())

    def delete(self, username: str) -> bool:
        if username.lower() in self.users:
            del self.users[username.lower()]
            return True
        return False

    def exists(self, username: str) -> bool:
        return username.lower() in self.users
    
    def save(self):
        return super().save()
    
    def load(self):
        return super().load()