from abc import ABC, abstractmethod
from typing import List

from commands.command_response import CommandResponse


class Command(ABC):
    """Abstract base class for commands."""
    @abstractmethod
    def execute(self, args: List[str]) -> CommandResponse:
        pass