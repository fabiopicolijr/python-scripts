import json
import shutil
import os
from .settings import LOG
from .print_color import print_colored


class fileManager:
    """
    This class manages files and directories
    """

    def __init__(self, source: str) -> None:
        self.source = source
        self.counter_files = 0
        self.counter_replace_injector = 0
        self.counter_replace_filename = 0
        self.counter_replace_content = 0

        self._count_files_recursively()

    def erase_files(self) -> None:
        for filename in os.listdir(self.source):
            file_path = os.path.join(self.source, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    if filename != ".gitkeep":
                        os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))

        if LOG:
            erased_folder = os.path.basename(self.source)
            print_colored(f"Files in '{erased_folder}' were erased.", color="blue")

    def move_files(self, destination: str) -> None:
        try:
            # Create the destination directory if it doesn't exist
            if not os.path.exists(destination):
                os.makedirs(destination)

            # Iterate over the items in the source directory
            for item in os.listdir(self.source):
                source_path = os.path.join(self.source, item)
                destination_path = os.path.join(destination, item)

                # Check if the item is a file or a directory
                if os.path.isfile(source_path):
                    shutil.copy2(source_path, destination_path)  # Copy the file
                elif os.path.isdir(source_path):
                    shutil.copytree(
                        source_path, destination_path
                    )  # Copy the directory recursively

            if LOG:
                print_colored(
                    f"Files moved from '{self.source}' to '{destination}'.",
                    color="blue",
                )

        except Exception as e:
            print_colored(
                f"An error occurred while MOVING files: {str(e)}", color="red"
            )

    def replace_inject_file(self, file_path, replacements: dict) -> None:
        try:
            filename = os.path.basename(file_path)

            with open(file_path, "r") as file:
                original_content = file.read()

            updated_content = original_content
            for tag, replacement_file in replacements.items():
                with open(replacement_file, "r") as replacement:
                    replacement_content = replacement.read()

                updated_content = updated_content.replace(tag, replacement_content)

                if filename.endswith("json"):
                    updated_content = self._format_json(updated_content, 2)

            with open(file_path, "w") as file:
                file.write(updated_content)

            self.counter_replace_injector += 1

            if LOG:
                print_colored(f"INJECTOR: File {filename} was injected.", color="blue")

        except Exception as e:
            print_colored(
                f"An error occurred while injecting file {filename}:",
                str(e),
                color="red",
            )

    def replace_filename(self, file_path: str, replacements: dict) -> None:
        directory = os.path.dirname(file_path)
        old_filename = os.path.basename(file_path)
        new_filename = old_filename

        for tag, content in replacements.items():
            if new_filename.find(tag) > 0:
                self.counter_replace_filename += 1
            new_filename = new_filename.replace(tag, content)

        new_file_path = os.path.join(directory, new_filename)

        try:
            os.rename(file_path, new_file_path)
            if LOG:
                print_colored(f"FILENAME: renamed to: {new_filename}", color="blue")
        except OSError:
            print_colored(
                f"FILENAME: Failed to rename the file {old_filename}.", color="red"
            )
            return None

    def replace_content(self, file_path: str, replacements: dict) -> None:
        with open(file_path, "r+") as stream:
            try:
                data = stream.read()
            except Exception as err:
                raise Exception(f"{file_path} {err}")

            for tag, content in replacements.items():
                if data.find(tag) > 0:
                    data = data.replace(tag, content)
                    self.counter_replace_content += 1

                    if LOG:
                        filename = os.path.basename(file_path)
                        print_colored(
                            f"CONTENT: {filename}\tOLD: {tag} NEW: {content}",
                            color="blue",
                        )
            stream.truncate(0)
            stream.seek(0)
            stream.write(data)

    def _format_json(self, content: str, spaces: int) -> str:
        return json.dumps(json.loads(content), indent=spaces)

    def _count_files_recursively(self) -> None:
        for root, dirs, files in os.walk(self.source):
            self.counter_files += len(files)
