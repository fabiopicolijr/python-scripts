import os


def erase_path(path):
    for filename in os.listdir(path):

        if not filename.endswith(".json") and not filename.endswith(".feature"):
            continue

        output_file = f"{path}/{filename}"
        os.remove(output_file)
