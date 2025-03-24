from typing import List

from service import UserService
from commands.base_command import Command
from commands.command_response import CommandResponse


class RegisterCommand(Command):
    """Command to register a new user."""
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        
    def execute(self, args: List[str]) -> CommandResponse:
        if len(args) != 1:
            return CommandResponse(False, "Error - invalid arguments")
        
        success, message = self.user_service.register_user(args[0])
        return CommandResponse(success, message)