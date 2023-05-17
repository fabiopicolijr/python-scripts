import json

from marketplace.behave.config import PATH, INTERPOLATION_SCHEMA
from marketplace.behave.classes.api import Api


def interpolate_file(api: Api, template_file: str):
    file = template_file.split("/")[-1]

    new_file = interpolate_filename(file, api)
    output_file = f"{PATH['output']}/{new_file}"

    print(file)

    with open(template_file, "r") as stream, open(output_file, "w") as stream_write:
        content = stream.read()
        new_content = interpolate_content(content, api)

        if template_file.endswith("json"):
            new_content = json.dumps(json.loads(new_content), indent=2)

        stream_write.write(new_content)


def interpolate_filename(filename, api):
    filepiece_api_operation = api.operation.lower()
    api_name_underlined = f'{"_".join(api.name.split())}_{api.version}'.lower()

    if api.prefix:
        api_name_underlined = f"{api.prefix}.{api_name_underlined}".lower()

    new_file = filename.replace(
        INTERPOLATION_SCHEMA.filename_begin, api_name_underlined
    ).replace(INTERPOLATION_SCHEMA.method, filepiece_api_operation)

    return new_file


def interpolate_content(content, api):
    content = (
        content.replace(INTERPOLATION_SCHEMA.event_name_code, api.body.event_name_code)
        .replace(INTERPOLATION_SCHEMA.event_title, api.body.event_title)
        .replace(
            INTERPOLATION_SCHEMA.service_category_code, api.body.service_category_code
        )
    )

    tag_transform_file = (
        f"{PATH['files']}/rule_{api.rule_code}/injectors/body_transform_tag.json"
    )

    with open(tag_transform_file, "r") as stream:
        file_content = stream.read()
        content = content.replace(INTERPOLATION_SCHEMA.transform, file_content)

    tag_output_file = (
        f"{PATH['files']}/rule_{api.rule_code}/injectors/body_output_tag.json"
    )

    with open(tag_output_file, "r") as stream:
        file_content = stream.read()
        content = content.replace(INTERPOLATION_SCHEMA.output, file_content)

    return content
