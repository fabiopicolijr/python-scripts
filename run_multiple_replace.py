from utils.multiple_replace import MultipleReplace
from utils.settings import MARKETPLACE, PROJECTS

API_FOLDER = "worker_assignment_terminate"
SEARCH_REPLACE = {
    "workerDates": "workAssignment",
}

if __name__ == "__main__":
    print("Processing...")

    path = f"{MARKETPLACE}/{API_FOLDER}"
    # path = f"{PROJECTS}/fabiopicolijr/python-scripts/marketplace/behave/files/rule_3/templates"
    # path = f"{PROJECTS}/fabiopicolijr/python-scripts/marketplace/behave/output"
    # path = f"{PROJECTS}/fabiopicolijr/python-scripts/behave_replacer/templates/rule_1/overlap"

    mr = MultipleReplace(SEARCH_REPLACE, path)

    try:
        mr.process_files()
        print(f'\nProcess finished: Replaced "{mr.replaced_count}" times')
    except Exception as e:
        print(e)
