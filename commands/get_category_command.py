from typing import List

from service import ListingService
from commands.base_command import Command
from commands.command_response import CommandResponse


class GetCategoryCommand(Command):
    """Command to get listings in a specific category."""
    def __init__(self, listing_service: ListingService):
        self.listing_service = listing_service
        
    def execute(self, args: List[str]) -> CommandResponse:
        if len(args) != 2:
            return CommandResponse(False, "Error - invalid arguments")
        
        username, category = args
        success, message = self.listing_service.get_category_listings(username, category)
        return CommandResponse(success, message)