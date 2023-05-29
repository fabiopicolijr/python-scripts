import os
from utils.file_manager import fileManager
from utils.settings import BASE_DIR, LOG, RULES, TASKS
from utils.print_color import print_colored

# Behave Replacer settings
RULE = RULES[0]  # 0=1_TRANSFORM_TAG
TASK = TASKS[2]  # 0=HEADERS, 1=SAVE, 2=VALIDATE


# br_environment
API_SERVICE_GROUP = "leaves"
API_SERVICE = "change worker leave"

# General settings
API_VERSION = "v1"
API_OPERATION = "change"  # add, change, remove
API_TITLE = "Worker Leave Change"

API_TITLE_LOWER = API_TITLE.lower()
API_TITLE_UNDERLINED = API_TITLE_LOWER.replace(" ", "_")


# Filename Settings
FILENAME_API_NAME = API_TITLE_UNDERLINED
# Filename json Settings
FILENAME_BEGIN = f"wl_change_{API_VERSION}"

# Content Settings
JSON_SERVICE_SHORTNAME = "HR"
JSON_EVENT_SHORTNAME = "worker.leave.change"
JSON_EVENT_TITLE = API_TITLE

# Feature and step Settings
FEATURE_TITLE_ARTICLE = "o"  # Eu quero acessar ...
FEATURE_TITLE_ARTICLE_COMPLEMENT = "lo"  # De modo que eu possa gerenciá-...

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
    for folder, _, files in os.walk(fm_output.folder):
        for filename in files:
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path):
                # Inject file content inside files
                fm_output.replace_inject_file(file_path, injector_tags)
                # Replace file content
                fm_output.replace_content(file_path, content_tags)
                # Replace filenames
                fm_output.replace_filename(file_path, filename_tags)


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
        process_files(fm_output, injector_tags, content_tags, filename_tags)

        show_script_finished_message(fm_output)

    except Exception as e:
        print_colored("Error: ", str(e), color="red")


if __name__ == "__main__":
    main()
