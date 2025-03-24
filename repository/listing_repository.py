from abc import ABC, abstractmethod
from typing import Optional, List

from domain.listing import Listing


class ListingRepository(ABC):
    """Interface for Listing repositories."""
    @abstractmethod
    def add(self, listing: Listing) -> None:
        """Add a listing to the repository."""
        pass

    @abstractmethod
    def get(self, listing_id: int) -> Optional[Listing]:
        """Get a listing by ID."""
        pass

    @abstractmethod
    def delete(self, listing_id: int) -> bool:
        """Delete a listing by ID."""
        pass

    @abstractmethod
    def exists(self, listing_id: int) -> bool:
        """Check if a listing exists."""
        pass
    
    @abstractmethod
    def is_owner(self, username: str, listing_id: int) -> bool:
        """Check if a user is the owner of a listing."""
        pass
    
    @abstractmethod
    def get_all(self) -> List[Listing]:
        """Get all listings."""
        pass
    
    @abstractmethod
    def save(self) -> None:
        """Save data to persistent storage."""
        pass
    
    @abstractmethod
    def load(self) -> None:
        """Load data from persistent storage."""
        pass