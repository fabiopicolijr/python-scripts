import os

template_path = 'C:/Users/fabio.picoli/Documents/adp/templates/ala_marketplace/post/transform'
output_path = 'C:/Users/fabio.picoli/Documents/adp/output'
old_text = 'worker.birth-date.change'
new_text = 'worker.pay-distribution.change'

files_count = 0
files_replaced_count = 0

print(f'=> Objective: Change "{old_text}" to "{new_text}" from files inside folder "{template_path}"\n')
print('processing...')

for filename in os.listdir(template_path):

    if filename.endswith(".json"):
        files_count += 1

        template_file = f'{template_path}/{filename}'
        output_file = f'{output_path}/{filename}'

        with open(template_file, 'r') as stream, open(output_file, 'w') as stream_write:
            file_data = stream.read()

            new_file_data = file_data.replace(old_text, new_text)
            stream_write.write(new_file_data)

            files_replaced_count += 1


print(f'Changed "{files_replaced_count}" of "{files_count}" files.')
