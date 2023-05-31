import os
from utils.file_manager import fileManager
from utils.settings import BASE_DIR, LOG, RULES, TASKS
from utils.print_color import print_colored

# Constants and Settings
RULE = RULES[0]
TASK = TASKS[2]

API_SERVICE_GROUP = "leaves"
API_SERVICE = "change worker leave"

API_VERSION = "v1"
API_OPERATION = "change"
API_TITLE = "Worker Leave Change"

API_TITLE_LOWER = API_TITLE.lower()
API_TITLE_UNDERLINED = API_TITLE_LOWER.replace(" ", "_")

FILENAME_API_NAME = API_TITLE_UNDERLINED
FILENAME_BEGIN = f"wl_change_{API_VERSION}"

JSON_SERVICE_SHORTNAME = "HR"
JSON_EVENT_SHORTNAME = "worker.leave.change"
JSON_EVENT_TITLE = API_TITLE

FEATURE_TITLE_ARTICLE = "o"
FEATURE_TITLE_ARTICLE_COMPLEMENT = "lo"

match API_OPERATION:
    case "add":
        API_OPERATION_BR = "cadastrar"
    case "change":
        API_OPERATION_BR = "alterar"
    case "remove":
        API_OPERATION_BR = "excluir"
    case _:
        API_OPERATION_BR = "API_OPERATION_BR"

API_OPERATION_CAPITALIZED_BR = API_OPERATION_BR.capitalize()


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


def process_files(fm_output, injector_tags, content_tags, filename_tags):
    for folder, _, files in os.walk(fm_output.source):
        for filename in files:
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path):
                # inject file content inside files
                fm_output.replace_inject_file(file_path, injector_tags)
                # replace file content
                fm_output.replace_content(file_path, content_tags)
                # replace filenames
                fm_output.replace_filename(file_path, filename_tags)


def main():
    project_folder = os.path.join(BASE_DIR, "behave_replacer")
    out_folder = os.path.join(project_folder, "output")
    rule_folder = os.path.join(project_folder, "templates", RULE)
    overlap_folder = os.path.join(rule_folder, "overlap", TASK)
    injector_folder = os.path.join(rule_folder, "injector")

    content_tags = {
        "[[SERVICE_SHORTNAME]]": JSON_SERVICE_SHORTNAME,
        "[[EVENT_SHORTNAME]]": JSON_EVENT_SHORTNAME,
        "[[EVENT_TITLE]]": JSON_EVENT_TITLE,
        "[[FILENAME_BEGIN]]": FILENAME_BEGIN,
        "[[API_TITLE]]": API_TITLE,
        "[[API_TITLE_LOWER]]": API_TITLE_LOWER,
        "[[API_TITLE_UNDERLINED]]": API_TITLE_UNDERLINED,
        "[[API_VERSION]]": API_VERSION,
        "[[API_OPERATION]]": API_OPERATION,
        "[[API_OPERATION_BR]]": API_OPERATION_BR,
        "[[API_OPERATION_CAPITALIZED_BR]]": API_OPERATION_CAPITALIZED_BR,
        "[[API_SERVICE]]": API_SERVICE,
        "[[API_SERVICE_GROUP]]": API_SERVICE_GROUP,
        "[[FEATURE_TITLE_ARTICLE]]": FEATURE_TITLE_ARTICLE,
        "[[FEATURE_TITLE_ARTICLE_COMPLEMENT]]": FEATURE_TITLE_ARTICLE_COMPLEMENT,
    }

    filename_tags = {
        "[[FILENAME_BEGIN]]": FILENAME_BEGIN,
        "[[API_OPERATION]]": API_OPERATION,
        "[[FILENAME_API_NAME]]": FILENAME_API_NAME,
        "[[FILENAME_API_VERSION]]": API_VERSION,
    }

    injector_tags = {
        "[[TRANSFORM]]": os.path.join(injector_folder, "transform.json"),
        "[[OUTPUT]]": os.path.join(injector_folder, "output.json"),
    }

    if LOG:
        print_colored("Processing...", color="blue")

    try:
        # clear output files
        fm_output = fileManager(out_folder)
        fm_output.erase_files()

        # move overlap files to the output folder
        fm_templates = fileManager(overlap_folder)
        fm_templates.move_files(fm_output.source)

        # process files recursively
        process_files(fm_output, injector_tags, content_tags, filename_tags)

        show_script_finished_message(fm_output)

    except Exception as e:
        print_colored("Error: ", str(e), color="red")


if __name__ == "__main__":
    main()
