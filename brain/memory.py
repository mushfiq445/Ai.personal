# ==========================================
# Ai.personal - Local Memory Management
# ==========================================

import json
import os
from config.settings import MEMORY_FILE

class LocalMemory:
    def __init__(self):
        self.memory_file = MEMORY_FILE
        self.history = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_memory(self):
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving memory: {e}")

    def add_interaction(self, user_input: str, response: str):
        self.history.append({
            "user": user_input,
            "assistant": response
        })
        self.save_memory()
