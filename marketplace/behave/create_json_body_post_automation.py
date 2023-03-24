import os

from config import PATH
from data.parameters import PARAMETERS
from util.file_handling import erase_path
from util.error_handling import show_error_message
from marketplace.behave.classes.api import Api
from marketplace.behave.interpolating.template_interpolator import interpolate_template


def process_templates(api: Api, path):

    for filename in os.listdir(path):
        if not filename.endswith(".json"):
            continue

        file = f'{path}/{filename}'
        process_template(api, file)


def process_template(api: Api, file):
    try:
        interpolate_template(api, file)
    except Exception as e:
        show_error_message(e, process_template.__name__)


def main():
    try:
        api = Api(PARAMETERS['version'], PARAMETERS['service'], PARAMETERS['prefix'], PARAMETERS['name'], PARAMETERS['method'], PARAMETERS['filename_begin'])
        template_path = f"{PATH['templates']}/{PARAMETERS['request_method']}/{PARAMETERS['task']}"

        erase_path(PATH['output'])
        process_templates(api, template_path)
        # TODO: process_filenames
    except Exception as e:
        show_error_message(e)
    else:
        print('Process finished with success!')


if __name__ == '__main__':
    main()
