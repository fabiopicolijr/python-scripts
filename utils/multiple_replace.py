import os
from .settings import LOG
from .file_manager import fileManager
from .print_color import print_colored


class MultipleReplace:
    def __init__(
        self,
        search_replace: list,
        in_folder: str,
        out_folder: str = None,
        replace_filename: bool = False,
    ):
        self.search_replace_list = search_replace
        self.in_folder = in_folder
        self.out_folder = out_folder
        self.replace_filename = replace_filename
        self.files_count = 0
        self.replaced_count = 0
        self.process_folder = self.set_process_folder()

    def set_process_folder(self):
        if not self.out_folder:
            return self.in_folder
        else:
            fm = fileManager(self.in_folder)
            fm.copy_files(self.out_folder)

            return self.out_folder

    def process_files(self):
        """Process all files"""

        for folder, _, files in os.walk(self.process_folder):
            for filename in files:
                self.process_file(folder, filename)

    def process_file(self, folder: str, filename: str):
        file = os.path.join(folder, filename)

        try:
            if not filename.endswith(".json"):
                raise Exception(f'file "{filename}" not allowed to change.')

            if self.replace_filename:
                new_filename = self.replace_file_name(filename)
                file = self.change_filename(file, new_filename)

            self.replace_content(file)

        except Exception as err:
            print_colored(f"Error: {err}", color="red")

    def replace_file_name(self, file):
        for tag_str, new_str in self.search_replace_list.items():
            file = file.replace(tag_str, new_str)
        return file

    def change_filename(self, file_path, new_name):
        directory = os.path.dirname(file_path)
        new_path = os.path.join(directory, new_name)

        try:
            os.rename(file_path, new_path)
            print_colored(f"File renamed successfully to {new_name}", color="blue")
            return new_path
        except OSError as e:
            print_colored(f"Error renaming file: {e}", color="red")

    def replace_content(self, replace_file):
        with open(replace_file, "r+") as stream:
            try:
                content = stream.read()
            except Exception as err:
                raise Exception(f"{replace_file} {err}")

            for tag_str, new_str in self.search_replace_list.items():
                if content.find(tag_str) > 0:
                    content = content.replace(tag_str, new_str)
                    self.replaced_count += 1

                    if LOG:
                        filename = replace_file.split("/")[-1]
                        print_colored(
                            f"FILE: {filename}\tOLD: {tag_str}\tNEW: {new_str}",
                            color="blue",
                        )
            stream.truncate(0)
            stream.seek(0)
            stream.write(content)
