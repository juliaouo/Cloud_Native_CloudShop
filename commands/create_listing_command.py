from typing import List

from service import ListingService
from commands.base_command import Command
from commands.command_response import CommandResponse


class CreateListingCommand(Command):
    """Command to create a new listing."""
    def __init__(self, listing_service: ListingService):
        self.listing_service = listing_service
        
    def execute(self, args: List[str]) -> CommandResponse:
        if len(args) != 5:
            return CommandResponse(False, "Error - invalid arguments")
        
        username, title, description, price, category = args        
        success, message = self.listing_service.create_listing(
            username, title, description, price, category)
        return CommandResponse(success, message)