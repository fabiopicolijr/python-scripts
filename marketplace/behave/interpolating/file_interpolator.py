import json

from marketplace.behave.config import PATH, FILE, INTERPOLATION_SCHEMA
from marketplace.behave.classes.api import Api


def interpolate_file(api: Api, template_file):
    file = template_file.split('/')[-1]

    new_file = interpolate_filename(file, api)
    output_file = f"{PATH['output']}/{new_file}"

    with open(template_file, 'r') as stream, open(output_file, 'w') as stream_write:
        content = stream.read()
        new_content = interpolate_content(content, api)

        if template_file.endswith('json'):
            new_content = json.dumps(json.loads(new_content), indent=2)

        stream_write.write(new_content)


def interpolate_filename(filename, api):
    filepiece_api_operation = api.operation.lower()
    filepiece_api_name = f'{"_".join(api.name.split())}'.lower()

    if api.prefix:
        filepiece_api_name = f'{api.prefix}.{filepiece_api_name}'.lower()

    new_file = filename \
        .replace(INTERPOLATION_SCHEMA.filename_begin, filepiece_api_name) \
        .replace(INTERPOLATION_SCHEMA.method, filepiece_api_operation)

    return new_file


def interpolate_content(content, api):
    content = content \
        .replace(INTERPOLATION_SCHEMA.event_name_code, api.body.event_name_code) \
        .replace(INTERPOLATION_SCHEMA.event_title, api.body.event_title) \
        .replace(INTERPOLATION_SCHEMA.service_category_code, api.body.service_category_code)

    with open(FILE['body_transform_tag'], 'r') as stream:
        file_content = stream.read()
        content = content.replace(INTERPOLATION_SCHEMA.transform, file_content)

    with open(FILE['body_output_tag'], 'r') as stream:
        file_content = stream.read()
        content = content.replace(INTERPOLATION_SCHEMA.output, file_content)

    return content
