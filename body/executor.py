# ==========================================
# Ai.personal - File & Task Executor
# ==========================================

import os
import subprocess
from config.settings import WORKSPACE_DIR

class Executor:
    def __init__(self):
        self.workspace = WORKSPACE_DIR

    def write_production_file(self, filename: str, content: str):
        file_path = os.path.join(self.workspace, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"✅ Production-ready file successfully created at: {file_path}"
        except Exception as e:
            return f"❌ Error writing file: {e}"

    def run_script(self, filename: str):
        file_path = os.path.join(self.workspace, filename)
        if not os.path.exists(file_path):
            return f"❌ File not found in workspace: {filename}"
        
        try:
            result = subprocess.run(
                ["python", file_path],
                capture_output=True,
                text=True,
                timeout=10
            )
            return f"Output:\n{result.stdout}\nErrors:\n{result.stderr}"
        except Exception as e:
            return f"❌ Execution failed: {e}"
