from typing import List, Tuple


class Parser:
    """Utility to parse input strings into commands and arguments."""
    @staticmethod
    def parse_line(line: str) -> Tuple[str, List[str]]:
        """Parse a command line into command and arguments, handling quoted strings."""
        parts = []
        current_part = ""
        in_quotes = False
        quote_char = None
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char in ["'", '"'] and (i == 0 or line[i-1] != "\\"):
                if not in_quotes:
                    in_quotes = True
                    quote_char = char
                elif char == quote_char:
                    in_quotes = False
                    quote_char = None
                    parts.append(current_part)
                    current_part = ""
            elif char.isspace() and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char
            
            i += 1
        
        if current_part:
            parts.append(current_part)
        
        if not parts:
            return "", []

        return parts[0], parts[1:]