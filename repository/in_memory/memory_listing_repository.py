from collections import defaultdict
from typing import Dict, List, Optional

from domain import Listing
from repository.listing_repository import ListingRepository


class MemoryListingRepository(ListingRepository):
    """Repository for Listing entities using in-memory storage."""
    def __init__(self):
        self.listings: Dict[int, Listing] = {}
        self.user_listings: Dict[str, List[int]] = defaultdict(list)
        self.next_id = 100001

    def add(self, listing: Listing) -> None:
        self.listings[listing.id] = listing
        self.user_listings[listing.username].append(listing.id)

    def get(self, listing_id: int) -> Optional[Listing]:
        return self.listings.get(listing_id)

    def delete(self, listing_id: int) -> bool:
        if listing_id in self.listings:
            listing = self.listings[listing_id]
            self.user_listings[listing.username].remove(listing_id)
            del self.listings[listing_id]
            return True
        return False

    def exists(self, listing_id: int) -> bool:
        return listing_id in self.listings
    
    def is_owner(self, username: str, listing_id: int) -> bool:
        """Check if a user is the owner of a listing."""
        if listing_id not in self.listings:
            return False
        return self.listings[listing_id].username == username.lower()
    
    def get_all(self) -> List[Listing]:
        return list(self.listings.values())
    
    def save(self):
        return super().save()
        
    def load(self):
        return super().load()