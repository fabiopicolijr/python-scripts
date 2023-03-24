import json
from json_stream.dump import JSONStreamEncoder

from marketplace.behave.config import PATH, FILE, INTERPOLATION_SCHEMA
from marketplace.behave.classes.api import Api


def interpolate_template(api: Api, template_file):
    file = template_file.split('/')[-1]

    new_file = interpolate_filename(file, api)
    output_file = f"{PATH['output']}/{new_file}"

    with open(template_file, 'r') as stream, open(output_file, 'w') as stream_write:
        content = stream.read()
        new_content = interpolate_content(content, api)
        new_content_indented = json.dumps(json.loads(new_content), indent=2)

        stream_write.write(new_content_indented)


def interpolate_filename(filename, api):
    new_file = filename \
        .replace(INTERPOLATION_SCHEMA.url_main_path, api.url_main_path) \
        .replace(INTERPOLATION_SCHEMA.method, api.method)

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
