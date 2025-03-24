from typing import Tuple, TypeVar

from domain import Listing
from repository import UserRepository
from service import UserService


class ListingService:
    """Service for listing-related operations."""
    def __init__(self, listing_repository: UserRepository, category_repository: UserRepository, user_service: UserService):
        self.listing_repository = listing_repository
        self.category_repository = category_repository
        self.user_service = user_service
    
    def create_listing(self, username: str, title: str, description: str, 
                       price: float, category: str) -> Tuple[bool, str]:
        """Create a new listing and return result with message or ID."""
        if not self.user_service.user_exists(username):
            return False, "Error - unknown user"
        
        user = self.user_service.get_user(username)
        listing = Listing(title, description, price, category, 
                         username.lower(), user.display_name)
        
        self.listing_repository.add(listing)
        self.category_repository.add(category, listing.id)
        return True, str(listing.id)
    
    def delete_listing(self, username: str, listing_id: int) -> Tuple[bool, str]:
        """Delete a listing and return result with message."""
        if not self.user_service.user_exists(username):
            return False, "Error - unknown user"
        
        if not self.listing_repository.exists(listing_id):
            return False, "Error - listing does not exist"
        
        if not self.listing_repository.is_owner(username, listing_id):
            return False, "Error - listing owner mismatch"
        
        listing = self.listing_repository.get(listing_id)
        
        if listing:
            self.category_repository.delete(listing.category, listing_id)

        self.listing_repository.delete(listing_id)
        return True, "Success"
    
    def get_listing(self, username: str, listing_id: int) -> Tuple[bool, str]:
        """Get a listing by ID and return result with listing details or error message."""
        if not self.user_service.user_exists(username):
            return False, "Error - unknown user"
        
        listing = self.listing_repository.get(listing_id)
        if not listing:
            return False, "Error - not found"
        
        return True, listing.to_string()
    
    def get_category_listings(self, username: str, category: str) -> Tuple[bool, str]:
        """Get listings by category and return result with listing details or error message."""
        if not self.user_service.user_exists(username):
            return False, "Error - unknown user"
        
        listings = self.category_repository.get_listings_by_category(category)
        if not listings:
            return False, "Error - category not found"
        
        result = []
        for listing in listings:
            result.append(f"{listing.title}|{listing.description}|{listing.price}|{listing.created_time}")
        
        return True, "\n".join(result)
    
    def get_top_category(self, username: str) -> Tuple[bool, str]:
        """Get the category with the most listings and return result with category name or error message."""
        if not self.user_service.user_exists(username):
            return False, "Error - unknown user"
        
        top_category = self.category_repository.get_top_category_name()
        if not top_category:
            return True, "No categories found"
        
        return True, "\n".join(top_category)