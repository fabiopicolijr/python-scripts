import os

version = 'v1'
prefix = 'Worker'
name = 'Pay Distribution'
type_ = 'Change'
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_files_behave = f'{dir_path}\\behave\\files'
dir_files_progress = f'{dir_path}\\progress\\files'

shortname = f'{prefix.lower()}.{"-".join(name.split()).lower()}'
procedure_name = f'{prefix.lower()}-{"-".join(name.split()).lower()}'
schema_name = f'{prefix.lower()}_{"-".join(name.split()).lower()}.{type_.lower()}'

context = {
    'version': version.lower(),
    'name': name.capitalize(),
    'shortname': shortname,
    'eventTitle': f'{prefix.capitalize()} {name.capitalize()} {type_.capitalize()}',
    'procedureName': procedure_name,
    'schemaName': schema_name,
    'paths': {
        'inputs': {
            'json_body': f'{dir_files_progress}\\inputs\\body\\{shortname}.json'
        },
        'templates': {
            'procedure_read_change_json': f'{dir_files_progress}\\templates\\read_change_json.txt'
        },
        'schemas': {
            'post': f'{dir_files_progress}\\schemas\\post\\{schema_name}.json'
        },
        'outputs': {
            'procedure_read_change_json': f'{dir_files_progress}\\outputs\\progress\\procedure_read_change_json.p'
        }
    }
}
