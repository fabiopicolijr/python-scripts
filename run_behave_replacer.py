import os
from utils.file_manager import fileManager
from utils.settings import BASE_DIR, LOG, RULES, TASKS
from utils.print_color import print_colored

# Behave Replacer settings
RULE = RULES[0]  # 0 regular rule
TASK = TASKS[2]  # 0 headers, 1 save, 2 validate

# General settings
API_VERSION = "v1"

# Filename Settings
FILENAME_BEGIN = "wl_absence"
FILENAME_API_NAME = "leave_absence_request"
FILENAME_API_METHOD = "change"
FILENAME_API_VERSION = API_VERSION

# Content Settings

# JSON Settings
JSON_SERVICE_SHORTNAME = "HR"
JSON_EVENT_SHORTNAME = "worker.leaves"
JSON_EVENT_TITLE = "Worker Leaves"


def show_script_finished_message(fm: fileManager) -> None:
    print_colored(
        f"\nBehave Replacer Process Finished in '{fm.counter_files}' files:",
        color="green",
    )
    print_colored(
        f"- Files injected count: {fm.counter_replace_injector}",
        color="green",
    )
    print_colored(
        f"- Filename replaced count: {fm.counter_replace_filename}",
        color="green",
    )

    print_colored(
        f"- Files content replaced count: {fm.counter_replace_content}",
        color="green",
    )

    # print_colored(f'- total files "{mr.replaced_count}"', color="green")
    # print_colored(f'- replace count "{mr.replaced_count}"', color="green")
    # print_colored(f'- injector count "{injector.counter}"', color="green")


def main():
    project_folder = os.path.join(BASE_DIR, "behave_replacer")
    out_folder = f"{project_folder}/output"
    rule_folder = f"{project_folder}/templates/{RULE}"
    overlap_folder = f"{rule_folder}/overlap/{TASK}"
    injector_folder = f"{rule_folder}/injector"

    content_tags = {
        "[[SERVICE_SHORTNAME]]": JSON_SERVICE_SHORTNAME,
        "[[EVENT_SHORTNAME]]": JSON_EVENT_SHORTNAME,
        "[[EVENT_TITLE]]": JSON_EVENT_TITLE,
        "[[FILENAME_BEGIN]]": FILENAME_BEGIN,
        "[[API_METHOD]]": FILENAME_API_METHOD,
    }

    filename_tags = {
        "[[FILENAME_BEGIN]]": FILENAME_BEGIN,
        "[[API_METHOD]]": FILENAME_API_METHOD,
    }

    injector_tags = {
        "[[TRANSFORM]]": f"{injector_folder}/transform.json",
        "[[OUTPUT]]": f"{injector_folder}/output.json",
    }

    if LOG:
        print_colored("Processing...", color="blue")

    try:
        # clear output files
        fm_output = fileManager(out_folder)
        fm_output.erase_files()

        # move overlap files to the output folder
        fm_templates = fileManager(overlap_folder)
        fm_templates.move_files(out_folder)

        # process files recursively
        for folder, _, files in os.walk(out_folder):
            for filename in files:
                file_path = os.path.join(folder, filename)

                if os.path.isfile(file_path):
                    # inject file content inside files
                    fm_output.replace_inject_file(file_path, injector_tags)
                    # replace file content
                    fm_output.replace_content(file_path, content_tags)
                    # replace filenames
                    fm_output.replace_filename(file_path, filename_tags)

        show_script_finished_message(fm_output)

    except Exception as e:
        print_colored("Error: ", str(e), color="red")


if __name__ == "__main__":
    main()
