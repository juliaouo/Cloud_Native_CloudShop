from typing import List

from service import ListingService
from commands.base_command import Command
from commands.command_response import CommandResponse


class GetTopCategoryCommand(Command):
    """Command to get the category with the most listings."""
    def __init__(self, listing_service: ListingService):
        self.listing_service = listing_service
        
    def execute(self, args: List[str]) -> CommandResponse:
        if len(args) != 1:
            return CommandResponse(False, "Error - invalid arguments")
        
        username = args[0]
        success, message = self.listing_service.get_top_category(username)
        return CommandResponse(success, message)