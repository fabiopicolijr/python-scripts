from utils.multiple_replace import MultipleReplace
from utils.settings import MARKETPLACE, PROJECTS

API = "worker_leave_return_request"
SEARCH_REPLACE = {
    "10565022-": "10565022X",
}

if __name__ == "__main__":
    print("Processing...")

    path = f"{MARKETPLACE}/{API}"
    # path = f"{PROJECTS}/fabiopicolijr/python-scripts/marketplace/behave/files/rule_3/templates"
    # path = f"{PROJECTS}/fabiopicolijr/python-scripts/marketplace/behave/output"
    mr = MultipleReplace(SEARCH_REPLACE, path)

    try:
        mr.process_files()
        print(f'\nProcess finished: Replaced "{mr.replaced_count}" times')
    except Exception as e:
        print(e)
