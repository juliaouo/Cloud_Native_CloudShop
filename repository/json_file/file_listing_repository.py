import os
import json
from collections import defaultdict
from typing import Dict, List, Optional

from domain import Listing
from repository.listing_repository import ListingRepository


class FileListingRepository(ListingRepository):
    """File-based implementation of ListingRepository."""
    def __init__(self, file_path: str = "listings.json"):
        self.file_path = file_path
        self.listings: Dict[int, Listing] = {}
        self.user_listings: Dict[str, List[int]] = defaultdict(list)
        self.load()

    def add(self, listing: Listing) -> None:
        self.listings[listing.id] = listing
        self.user_listings[listing.username].append(listing.id)
        self.save()

    def get(self, listing_id: int) -> Optional[Listing]:
        return self.listings.get(listing_id)

    def delete(self, listing_id: int) -> bool:
        if listing_id in self.listings:
            listing = self.listings[listing_id]
            self.user_listings[listing.username].remove(listing_id)
            del self.listings[listing_id]
            self.save()
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
        """Get all listings."""
        return list(self.listings.values())
    
    def save(self) -> None:
        """Save listings to JSON file."""
        # Prepare data for serialization
        data = {
            "listings": {str(id): listing.to_dict() for id, listing in self.listings.items()},
            "user_listings": {username: listing_ids for username, listing_ids in self.user_listings.items() if listing_ids}
        }
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path) or '.', exist_ok=True)
        
        # Save to file
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load(self) -> None:
        """Load listings from JSON file if it exists."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    
                    # Restore listings
                    self.listings = {int(id): Listing.from_dict(listing_data) 
                                    for id, listing_data in data.get("listings", {}).items()}
                    
                    # Restore user_listings mapping
                    self.user_listings = defaultdict(list)
                    for username, listing_ids in data.get("user_listings", {}).items():
                        self.user_listings[username] = listing_ids
                    
                    # Update next_id to be greater than any existing listing ID
                    if self.listings:
                        Listing.next_id = max(int(id) for id in self.listings.keys()) + 1
            except (json.JSONDecodeError, FileNotFoundError):
                # If the file is corrupted or missing, start with empty data structures
                self.listings = {}
                self.user_listings = defaultdict(list)
