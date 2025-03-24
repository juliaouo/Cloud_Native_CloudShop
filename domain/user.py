from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class User:
    username: str
    display_name: str = None
    
    def __post_init__(self):
        if self.display_name is None:
            self.display_name = self.username
        self.username = self.username.lower()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "username": self.username,
            "display_name": self.display_name
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        return cls(
            username=data["username"],
            display_name=data.get("display_name")
        )