from typing import List

from service import ListingService
from commands.base_command import Command
from commands.command_response import CommandResponse


class DeleteListingCommand(Command):
    """Command to delete a listing."""
    def __init__(self, listing_service: ListingService):
        self.listing_service = listing_service
        
    def execute(self, args: List[str]) -> CommandResponse:
        if len(args) != 2:
            return CommandResponse(False, "Error - invalid arguments")
        
        username, listing_id = args
        try:
            listing_id_int = int(listing_id)
        except ValueError:
            return CommandResponse(False, "Error - invalid listing ID")
        
        success, message = self.listing_service.delete_listing(username, listing_id_int)
        return CommandResponse(success, message)