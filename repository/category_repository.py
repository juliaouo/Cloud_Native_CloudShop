from abc import ABC, abstractmethod
from typing import List, Optional

from domain.listing import Listing


class CategoryRepository(ABC):
    """Interface for category-related operations."""
    @abstractmethod
    def add(self, category: str, listing_id: int) -> None:
        """Add a listing to a category."""
        pass

    @abstractmethod
    def get(self, category: str) -> List[int]:
        """Get all listing IDs in a category."""
        pass

    @abstractmethod
    def delete(self, category: str, listing_id: int) -> bool:
        """Delete a listing from a category."""
        pass

    @abstractmethod
    def exists(self, category: str) -> bool:
        """Check if a category exists."""
        pass
    
    @abstractmethod
    def get_listings_by_category(self, category: str) -> List[Listing]:
        """Get all listings in a category sorted by creation time (descending)."""
        pass
    
    @abstractmethod
    def get_top_category_name(self) -> Optional[list]:
        """Get the category with the most listings."""
        pass
    
    @abstractmethod
    def save(self) -> None:
        """Save data to persistent storage."""
        pass
    
    @abstractmethod
    def load(self) -> None:
        """Load data from persistent storage."""
        pass