import shutil
import os
from .settings import LOG
from .print_color import print_colored


def copy_files(source_folder, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        files = os.listdir(source_folder)

        for file in files:
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)
            shutil.copy2(source_file, destination_file)

        if LOG:
            print_colored(
                f"Files copied successfully to {destination_folder}!", color="blue"
            )

        return True

    except Exception as e:
        print("An error occurred while copying files:", str(e))
        return False


def erase_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))
