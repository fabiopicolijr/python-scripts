import os

# TEMP VARIABLES
new_method = "replace"
new_event_name_code_method = new_method.lower()
new_event_title_method = new_method.capitalize()

# CONST VARIABLES
TEMPLATES_PATH = f'C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace/marketplace/features/files/br/inputs/400/pay_data_inputs/{new_method}'
# TEMPLATES_PATH = 'C:/Users/fabio.picoli/projects/fabiopicolijr/python-scripts/marketplace/behave/output'

REPLACE_TAGS = [
    {
        "old": f"pay-data-input.add",
        "new": f"pay-data-input.{new_event_name_code_method}",
    },
    {
        "old": f"Pay Data Input Add",
        "new": f"Pay Data Input {new_event_title_method}",
    },
]


FILES_REPLACES_COUNT = 0
FILES_COUNT = 0


def process_templates():
    for template_path, _, files in os.walk(TEMPLATES_PATH):
        for filename in files:
            process_template(template_path, filename)


def process_template(template_path: str, filename: str):
    global FILES_COUNT
    global FILES_REPLACES_COUNT

    try:
        if not filename.endswith(".json"):
            raise Exception(f'file "{filename}" not allowed to change.')

        FILES_COUNT += 1
        template_file = f'{template_path}/{filename}'

        with open(template_file, 'r+') as stream:
            try:
                file_data = stream.read()
            except Exception as err:
                # raise Exception(f'{template_file} {err}')
                raise Exception(f'{filename} {err}')

            for replace_tag in REPLACE_TAGS:
                if file_data.find(replace_tag['old']) > 0:
                    # print(f'Found: {template_file})
                    file_data = file_data.replace(replace_tag['old'], replace_tag['new'])
                    FILES_REPLACES_COUNT += 1

            stream.truncate(0)
            stream.seek(0)

            stream.write(file_data)

    except Exception as err:
        print(f'\twarning: {err}')


if __name__ == '__main__':
    print('Processing...')

    try:
        process_templates()
        print(f'\nProcess finished: Replaced "{FILES_REPLACES_COUNT}" times in "{FILES_COUNT}" files.')
    except Exception as e:
        print(e)
