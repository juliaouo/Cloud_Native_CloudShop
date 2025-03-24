import datetime
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Listing:
    title: str
    description: str
    price: int
    category: str
    username: str
    display_name: str
    id: int = None
    created_time: str = None
    
    next_id = 100001
    
    def __post_init__(self):
        self.id = Listing.next_id
        Listing.next_id += 1
        self.created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_string(self) -> str:
        return f"{self.title}|{self.description}|{self.price}|{self.created_time}|{self.category}|{self.display_name}"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "username": self.username,
            "display_name": self.display_name,
            "created_time": self.created_time
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Listing':
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            price=data["price"],
            category=data["category"],
            username=data["username"],
            display_name=data["display_name"],
            created_time=data["created_time"]
        )