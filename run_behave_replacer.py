import os
from utils.files import erase_files
from utils.injector import Injector
from utils.multiple_replace import MultipleReplace
from utils.settings import BASE_DIR, LOG, RULES, TASKS
from utils.print_color import print_colored

# API = "worker_leave_return_request"

JSON_SERVICE_SHORTNAME = "HR"
JSON_EVENT_SHORTNAME = "worker.leaves"
JSON_EVENT_TITLE = "Worker Leaves"

FILENAME_BEGIN = "wl_absence"
FILENAME_API_METHOD = "change"


if __name__ == "__main__":
    search_replace = {
        "[[SERVICE_SHORTNAME]]": JSON_SERVICE_SHORTNAME,
        "[[EVENT_SHORTNAME]]": JSON_EVENT_SHORTNAME,
        "[[EVENT_TITLE]]": JSON_EVENT_TITLE,
        "[[FILENAME_BEGIN]]": FILENAME_BEGIN,
        "[[API_METHOD]]": FILENAME_API_METHOD,
    }

    project_folder = os.path.join(BASE_DIR, "behave_replacer")
    out_folder = f"{project_folder}/output"
    rule_folder = f"{project_folder}/templates/{RULES[0]}"
    task_folder = f"{rule_folder}/overlap/{TASKS[2]}"
    injector_folder = f"{rule_folder}/injector"

    if LOG:
        print_colored("Processing...", color="blue")

    try:
        erase_files(out_folder)
        mr = MultipleReplace(search_replace, task_folder, out_folder, True)
        mr.process_files()

        injector = Injector(injector_folder, out_folder)

        print_colored("\nBehave Replacer Process Finished:", color="green")
        print_colored(f'- total files "{mr.replaced_count}"', color="green")
        print_colored(f'- replace count "{mr.replaced_count}"', color="green")
        print_colored(f'- injector count "{injector.counter}"', color="green")

    except Exception as e:
        print_colored("Error: ", str(e), color="red")
