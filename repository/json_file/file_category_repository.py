import os
import json
from collections import defaultdict
from typing import Dict, List, Optional

from domain import Listing
from repository.listing_repository import ListingRepository
from repository.category_repository import CategoryRepository


class FileCategoryRepository(CategoryRepository):
    """File-based implementation of CategoryRepository."""
    def __init__(self, listing_repository: ListingRepository, file_path: str = "categories.json"):
        self.listing_repository = listing_repository
        self.file_path = file_path
        self.category_listings: Dict[str, List[int]] = defaultdict(list)
        self.category_count: Dict[str, int] = defaultdict(int)
        self.load()

    def add(self, category: str, listing_id: int) -> None:
        """Add a listing to a category."""
        self.category_listings[category].append(listing_id)
        self.category_count[category] += 1
        self.save()

    def get(self, category: str) -> List[int]:
        """Get all listing IDs in a category."""
        return self.category_listings.get(category, [])

    def delete(self, category: str, listing_id: int) -> bool:
        """Remove a listing from a category."""
        if category in self.category_listings and listing_id in self.category_listings[category]:
            self.category_listings[category].remove(listing_id)
            self.category_count[category] -= 1
            
            # Clean up empty categories
            if self.category_count[category] == 0:
                del self.category_count[category]
                del self.category_listings[category]
            
            self.save()
            return True
        return False

    def exists(self, category: str) -> bool:
        """Check if a category exists."""
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

    def get_top_category_name(self) -> Optional[List]:
        """Get the category with the most listings."""
        if not self.category_count:
            return None

        max_value = max(self.category_count.values())
        top_categories = [key for key, value in self.category_count.items() if value == max_value]
        
        return sorted(top_categories) 
    
    def save(self) -> None:
        """Save category data to JSON file."""
        # Prepare data for serialization
        data = {
            "category_listings": {category: listing_ids for category, listing_ids in self.category_listings.items()},
            "category_count": dict(self.category_count)
        }
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path) or '.', exist_ok=True)
        
        # Save to file
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Load category data from JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    
                    # Restore category_listings
                    self.category_listings = defaultdict(list)
                    for category, listing_ids in data.get("category_listings", {}).items():
                        self.category_listings[category] = listing_ids
                    
                    # Restore category_count
                    self.category_count = defaultdict(int)
                    for category, count in data.get("category_count", {}).items():
                        self.category_count[category] = count
            except (json.JSONDecodeError, FileNotFoundError):
                # If the file is corrupted or missing, start with empty data structures
                self.category_listings = defaultdict(list)
                self.category_count = defaultdict(int)