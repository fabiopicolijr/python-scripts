from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROJECTS = "C:/Users/fabio.picoli/projects"
MARKETPLACE = f"{PROJECTS}/adp/automation/ala.marketplace/marketplace/features/data/br"

LOG = True

# Behave rules:
# - rule_1: created 19.05.2023.
RULES = ["rule_1"]

# Behave tasks related to the alpha team:
TASKS = ["headers", "save", "validate"]
