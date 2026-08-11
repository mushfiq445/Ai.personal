# ==========================================
# Ai.personal - Command Parser
# ==========================================

class CommandParser:
    def __init__(self):
        pass

    def parse(self, raw_input: str):
        # Clean and sanitize the user input
        cleaned_input = raw_input.strip()
        
        # Check for system commands or direct instructions
        return {
            "raw": raw_input,
            "cleaned": cleaned_input,
            "is_empty": len(cleaned_input) == 0
        }
