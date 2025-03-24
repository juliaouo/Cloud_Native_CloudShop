from collections import defaultdict
from typing import Dict, List, Optional, TypeVar

from repository.listing_repository import ListingRepository
from repository.category_repository import CategoryRepository
from domain import Listing


class MemoryCategoryRepository(CategoryRepository):
    """Repository for categories using in-memory storage."""
    def __init__(self, listing_repository: ListingRepository):
        self.listing_repository = listing_repository
        self.category_listings: Dict[str, List[int]] = defaultdict(list)
        self.category_count: Dict[str, int] = defaultdict(int)

    def add(self, category: str, listing_id: int) -> None:
        self.category_listings[category].append(listing_id)
        self.category_count[category] += 1

    def get(self, category: str) -> List[int]:
        return self.category_listings.get(category, [])

    def delete(self, category: str, listing_id: int) -> bool:
        if category in self.category_listings and listing_id in self.category_listings[category]:
            self.category_listings[category].remove(listing_id)
            self.category_count[category] -= 1
            
            # Clean up empty categories
            if self.category_count[category] == 0:
                del self.category_count[category]
                del self.category_listings[category]
            
            return True
        return False

    def exists(self, category: str) -> bool:
        return category in self.category_listings

    def get_listings_by_category(self, category: str) -> List[Listing]:
        """Get all listings in a category sorted by creation time (descending)."""
        if category not in self.category_listings:
            return []
    
        listings = []
        insertion_order = 0
        for listing_id in self.category_listings[category]:
            listing = self.listing_repository.get(listing_id)
            if listing:
                listing.insertion_order = insertion_order
                listings.append(listing)
                insertion_order += 1
        
        return sorted(listings, key=lambda x: (x.created_time, x.insertion_order), reverse=True)

    def get_top_category_name(self) -> Optional[list]:
        """Get the category with the most listings."""
        if not self.category_count:
            return None

        max_value = max(self.category_count.values())
        top_categories = [key for key, value in self.category_count.items() if value == max_value]
        
        return sorted(top_categories)  
    
    def save(self):
        return super().save()
    
    def load(self):
        return super().load()