import os

# path = 'C:/Users/fabio.picoli/projects/fabiopicolijr/python-scripts/marketplace/behave/files/templates/post
# /body_and_output'
path = 'C:/Users/fabio.picoli/projects/fabiopicolijr/python-scripts/marketplace/behave/files/output'


old_piece = 'worker_pay_distribution'
new_piece = 'worker_pay_distributions'

files_count = 0
files_renamed_count = 0

print(f'=> Objective: Change "{old_piece}" to "{new_piece}" of all files into folder "{path}"\n')
print('processing...')

for filename in os.listdir(path):

    files_count += 1

    if filename.find(old_piece) >= 0:
        file = f'{path}/{filename}'
        new_file = f'{path}/{filename.replace(old_piece, new_piece)}'
        os.rename(file, new_file)

        files_renamed_count += 1
else:
    print(f'Changed "{files_renamed_count}" of "{files_count}" files.')


