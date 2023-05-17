import os

from marketplace.behave.classes.interpolation_schema import InterpolationSchema

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

FILE = {
    "body_transform_tag": f"{ROOT_PATH}/files/injectors/body_transform_tag.json",
    "body_output_tag": f"{ROOT_PATH}/files/injectors/body_output_tag.json",
}

PATH = {"files": f"{ROOT_PATH}/files", "output": f"{ROOT_PATH}/output"}

INTERPOLATION_SCHEMA = InterpolationSchema()
