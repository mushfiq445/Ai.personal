import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
WORKSPACE_DIR = os.path.join(BASE_DIR, "workspace")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(WORKSPACE_DIR, exist_ok=True)

MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")

SYSTEM_RULES = {
    "strict_obedience": True,
    "no_pushback": True,
    "production_ready_code": True
}
