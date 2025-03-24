class CommandResponse:
    """Object to hold the response of a command execution."""
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message