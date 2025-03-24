import os
from dataclasses import dataclass
from typing import Optional, Dict, Any
import json

from repository import RepositoryType

@dataclass
class DatabaseConfig:
    data_dir: str = "data"
    db_type: RepositoryType = RepositoryType.FILE  # Options: RepositoryType.MEMORY, RepositoryType.FILE, can extend to "sqlite", "mysql", etc.
    db_connection: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.db_type == RepositoryType.FILE:
            self.ensure_data_dir_exists()
    
    def ensure_data_dir_exists(self) -> None:
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def get_user_db_path(self) -> str:
        return os.path.join(self.data_dir, "users.json")
    
    def get_listing_db_path(self) -> str:
        return os.path.join(self.data_dir, "listings.json")
    
    def get_category_db_path(self) -> str:
        return os.path.join(self.data_dir, "categories.json")
    
    @classmethod
    def from_config_file(cls, config_path: str) -> 'DatabaseConfig':
        try:
            with open(config_path, 'r') as f:
                config_data = json.load(f)
            return cls(**config_data)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default config if file doesn't exist or is invalid
            return cls()