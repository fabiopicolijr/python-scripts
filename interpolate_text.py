import os

print('\n**** WELCOME TO "fabiopicolijr" PYTHON SCRIPTS ****\n')

template_path = 'C:/Users/fabio.picoli/Documents/adp/templates/ala_marketplace/post/body_and_output'
old_text = 'Worker Birth Date Change'
new_text = '[[EVENT_TITLE]]'

files_count = 0
files_replaced_count = 0

print(f'=> Objective: Change "{old_text}" to "{new_text}" from files inside folder "{template_path}"\n')
print('processing...')

for filename in os.listdir(template_path):

    if not filename.endswith(".json"):
        continue

    files_count += 1

    template_file = f'{template_path}/{filename}'

    print(template_file)

    with open(template_file, 'r+') as stream:
        file_data = stream.read()
        file_data = file_data.replace(old_text, new_text)

        stream.truncate(0)
        stream.seek(0)

        stream.write(file_data)

        files_replaced_count += 1


print(f'Changed "{files_replaced_count}" of "{files_count}" files.')
