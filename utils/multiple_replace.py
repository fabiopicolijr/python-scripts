import os
from .config import LOG


# TODO: non-recursive call
# TODO: output folder to put new files there

class MultipleReplace:

    def __init__(self, search_replace: list, in_folder: str, out_folder: str = None):
        self.search_replace_list = search_replace
        self.in_folder = in_folder
        self.out_folder = out_folder
        self.files_count = 0
        self.replaced_count = 0

    def process_files(self):

        for folder, _, files in os.walk(self.in_folder):
            for filename in files:
                self.process_file(folder, filename)

    def process_file(self, folder: str, filename: str):

        try:
            if not filename.endswith(".json"):
                raise Exception(f'file "{filename}" not allowed to change.')

            template_file = f'{folder}/{filename}'

            with open(template_file, 'r+') as stream:
                try:
                    file_data = stream.read()
                except Exception as err:
                    # raise Exception(f'{template_file} {err}')
                    raise Exception(f'{filename} {err}')

                for search_replace in self.search_replace_list:
                    if file_data.find(search_replace['old']) > 0:

                        file_data = file_data.replace(search_replace['old'], search_replace['new'])
                        self.replaced_count += 1

                        if LOG:
                            print(f"\tReplaced: {template_file}")

                stream.truncate(0)
                stream.seek(0)
                stream.write(file_data)

        except Exception as err:
            print(f'\twarning: {err}')
