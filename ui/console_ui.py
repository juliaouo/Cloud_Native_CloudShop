import sys
from typing import TextIO

from factories import CommandFactory
from ui.parser import Parser


class ConsoleUI:
    """User interface for the console application."""
    def __init__(self, command_factory: CommandFactory):
        self.command_factory = command_factory
        self.parser = Parser()
    
    def process_command(self, line: str) -> str:
        """Process a command line and return the result."""
        command_name, args = self.parser.parse_line(line)
        if not command_name:
            return ""
        
        command = self.command_factory.get_command(command_name)
        if not command:
            return ""
        
        result = command.execute(args)
        return result.message
    
    def run(self, input_stream: TextIO = sys.stdin, output_stream: TextIO = sys.stdout):
        """
        Run the application with support for both interactive and non-interactive modes.
        
        In interactive mode, the application will display a prompt before each command.
        In non-interactive mode (e.g., when piping input from a file), no prompt is shown.
        
        Args:
            input_stream: Source of input (default: sys.stdin)
            output_stream: Destination for output (default: sys.stdout)
        """
        # Determine if we're in interactive mode (terminal) or non-interactive mode (pipe/file)
        is_interactive = input_stream.isatty()
        
        try:
            while True:
                # Display prompt only in interactive mode
                if is_interactive:
                    output_stream.write("# ")
                    output_stream.flush()
                
                # Read a line of input
                line = input_stream.readline()
                
                # Check for EOF
                if not line:
                    break
                
                # Process the command
                line = line.strip()
                if line:
                    result = self.process_command(line)
                    if result:
                        print(result, file=output_stream)
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            sys.exit(0)
        except EOFError:
            # Handle EOF gracefully
            sys.exit(0)