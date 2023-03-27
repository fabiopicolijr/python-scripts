import json
from _deprecated.tree_manager import TreeManager


def json_to_dict(file: str) -> dict:
    try:
        # Opening JSON file
        f = open(file)

        # returns JSON object as a dictionary
        try:
            data = json.load(f)
        except ValueError as ve:
            raise Exception(f"Invalid JSON file {file} : {ve}")

        # Closing file
        f.close()
    except ValueError as ve:
        raise Exception(f"json_to_dict(): {ve}")

    return data


def json_to_tree(api_schema_file: str) -> TreeManager:
    """
    Convert a json file into a tree
    :return TreeManager
    """

    api_schema_data = json_to_dict(api_schema_file)
    api_schema_tree = TreeManager()
    api_schema_tree.dict_to_tree(api_schema_data)

    # api_schema_tree.show()
    print('Funtions -> json_to_tree -> Tree converted!')

    return api_schema_tree
