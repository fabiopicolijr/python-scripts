import os


version = 'v1'
prefix = 'Worker'
name = 'Deposit Account'
type_ = 'Add'
dir_path = os.path.dirname(os.path.realpath(__file__))

context = {
    'version': version.lower(),
    'name': name.capitalize(),
    'shortname': f'{prefix.lower()}.{"-".join(name.split()).lower()}',
    'eventTitle': f'{prefix.capitalize()} {name.capitalize()} {type_.capitalize()}',
    'paths': {
        'templates': {
            'post': {
                'headers': {
                    'inputs': f'{dir_path}\\files\\templates\\post\\headers\\inputs'
                }
            }
        }

    }
}