import os

from config import PATH
from data.parameters import PARAMETERS
from util.file_handling import erase_path
from util.error_handling import show_error_message
from marketplace.behave.classes.api import Api
from marketplace.behave.interpolating.file_interpolator import interpolate_file


def process_templates(api: Api, path: str, accept_only=None):
    for filename in os.listdir(path):
        if accept_only and not filename.endswith(accept_only):
            continue

        file = f"{path}/{filename}"
        process_template(api, file)


def process_template(api: Api, file):
    try:
        interpolate_file(api, file)
    except Exception as e:
        show_error_message(e, process_template.__name__)


def main():
    try:
        api = Api(
            rule_code=PARAMETERS["rule_code"],
            name=PARAMETERS["api_name"],
            prefix=PARAMETERS["api_prefix"],
            service=PARAMETERS["api_service"],
            version=PARAMETERS["api_version"],
            operation=PARAMETERS["api_operation"],
            method=PARAMETERS["api_method"],
            url_service=PARAMETERS["api_url_service"],
        )

        templates_path = f"{PATH['files']}/rule_{api.rule_code}/templates"

        erase_path(PATH["output"])
        process_templates(api, templates_path)
    except Exception as e:
        show_error_message(e)
    else:
        print(f"Process finished with success!\nFind your files at: {PATH['output']}")


if __name__ == "__main__":
    main()
