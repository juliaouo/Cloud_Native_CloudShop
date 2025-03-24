
import os
import json
from typing import Dict, Optional

from domain import User
from repository.user_repository import UserRepository


class FileUserRepository(UserRepository):
    """File-based implementation of UserRepository."""
    def __init__(self, file_path: str = "users.json"):
        self.file_path = file_path
        self.users: Dict[str, User] = {}
        self.load()

    def add(self, username: str, user: User) -> None:
        self.users[username.lower()] = user
        self.save()

    def get(self, username: str) -> Optional[User]:
        return self.users.get(username.lower())

    def delete(self, username: str) -> bool:
        if username.lower() in self.users:
            del self.users[username.lower()]
            self.save()
            return True
        return False

    def exists(self, username: str) -> bool:
        return username.lower() in self.users
    
    def save(self) -> None:
        """Save users to JSON file."""
        users_data = {username: user.to_dict() for username, user in self.users.items()}
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path) or '.', exist_ok=True)
        
        with open(self.file_path, 'w') as f:
            json.dump(users_data, f, indent=2)
    
    def load(self) -> None:
        """Load users from JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    users_data = json.load(f)
                    self.users = {username: User.from_dict(data) for username, data in users_data.items()}
            except (json.JSONDecodeError, FileNotFoundError):
                # If the file is corrupted or missing, start with an empty dictionary
                self.users = {}