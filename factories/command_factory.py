from typing import Optional

from service import *
from commands import *


class CommandFactory:
    """Factory to create appropriate Command objects."""
    def __init__(self, user_service: UserService, listing_service: ListingService):
        self.commands = {
            "REGISTER": RegisterCommand(user_service),
            "CREATE_LISTING": CreateListingCommand(listing_service),
            "DELETE_LISTING": DeleteListingCommand(listing_service),
            "GET_LISTING": GetListingCommand(listing_service),
            "GET_CATEGORY": GetCategoryCommand(listing_service),
            "GET_TOP_CATEGORY": GetTopCategoryCommand(listing_service)
        }
    
    def get_command(self, command_name: str) -> Optional[Command]:
        """Get a command by name."""
        return self.commands.get(command_name)