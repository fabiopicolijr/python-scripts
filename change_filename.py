import os

print('\n**** WELCOME TO "fabiopicolijr" PYTHON SCRIPTS ****\n')

path = 'C:/Users/fabio.picoli/Documents/adp/tasks/marketplace/_models/post/headers/'
old_name = 'change_body'
new_name = 'add_body'

files_count = 0
files_renamed_count = 0

print(f'=> Objective: Change "{old_name}" to "{new_name}" of all files into folder "{path}"\n')
print('processing...')


for filename in os.listdir(path):

    files_count += 1

    if filename.find(old_name) >= 0:
        file = path + filename
        new_file = path + filename.replace(old_name, new_name)
        os.rename(file, new_file)
        files_renamed_count += 1
else:
    print(f'Changed "{files_renamed_count}" of "{files_count}" files.')


