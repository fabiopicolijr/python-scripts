import os

print('\n**** WELCOME TO "fabiopicolijr" PYTHON SCRIPTS ****\n')

path = 'C:/Users/fabio.picoli/Documents/adp/tasks/marketplace/_models/post/headers/'
old_text = 'worker.pay-distributions.change'
new_text = 'worker.deposit-account.add'

files_count = 0
files_replaced_count = 0

print(f'=> Objective: Change "{old_text}" to "{new_text}" from files inside folder "{path}"\n')
print('processing...')

for filename in os.listdir(path):

    if filename.endswith(".json"):
        files_count += 1
        file_path = path + filename

        with open(file_path, 'r') as stream:
            file_data = stream.read()
            new_file_data = file_data.replace(old_text, new_text)

            with open(file_path, 'w') as stream_write:
                stream_write.write(new_file_data)
                files_replaced_count += 1


print(f'Changed "{files_replaced_count}" of "{files_count}" files.')
