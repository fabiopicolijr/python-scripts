import os

from config import PATH
from data.parameters import PARAMETERS
from util.file_handling import erase_path
from util.error_handling import show_error_message
from marketplace.behave.classes.api import Api
from marketplace.behave.interpolating.file_interpolator import interpolate_file


def process_files(api: Api, path: str, accept_only=None):
    for filename in os.listdir(path):
        if accept_only and not filename.endswith(accept_only):
            continue

        file = f'{path}/{filename}'
        process_file(api, file)


def process_file(api: Api, file):
    try:
        interpolate_file(api, file)
    except Exception as e:
        show_error_message(e, process_file.__name__)


def main():
    try:
        api = Api(
            name=PARAMETERS['api_name'],
            prefix=PARAMETERS['api_prefix'],
            service=PARAMETERS['api_service'],
            version=PARAMETERS['api_version'],
            operation=PARAMETERS['api_operation'],
            method=PARAMETERS['api_method'],
            url_service=PARAMETERS['api_url_service']
        )

        json_files_path = f"{PATH['templates']}/{api.method}/{PARAMETERS['task']}"
        behave_files_path = f"{PATH['templates']}/automation/{PARAMETERS['task']}"

        erase_path(PATH['output'])
        process_files(api, json_files_path, accept_only='json')
        process_files(api, behave_files_path)

        # TODO: process_filenames
    except Exception as e:
        show_error_message(e)
    else:
        print('Process finished with success!')


if __name__ == '__main__':
    main()
