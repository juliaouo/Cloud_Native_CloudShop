from typing import TypeVar, Tuple, Optional

from domain import User
from repository import UserRepository


class UserService:
    """Service for user-related operations."""
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def register_user(self, username: str) -> Tuple[bool, str]:
        """Register a new user and return result with message."""
        if self.user_repository.exists(username):
            return False, "Error - user already existing"
        
        user = User(username)
        self.user_repository.add(username, user)
        return True, "Success"
    
    def get_user(self, username: str) -> Optional[User]:
        """Get a user by username."""
        return self.user_repository.get(username)
    
    def user_exists(self, username: str) -> bool:
        """Check if a user exists."""
        return self.user_repository.exists(username)