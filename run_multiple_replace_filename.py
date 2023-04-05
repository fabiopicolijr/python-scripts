import os

path = f"C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace/marketplace/features/files/br/inputs/400/pay_data_inputs/replace"
search_replace = [
    {
        "old": '_add_',
        "new": f'_replace_'
    }
]

files_count = 0
files_renamed_count = 0

print('processing...')

for filename in os.listdir(path):

    files_count += 1

    for replace_tag in search_replace:
        if filename.find(replace_tag['old']) >= 0:
            file = f'{path}/{filename}'
            new_file = f'{path}/{filename.replace(replace_tag["old"], replace_tag["new"])}'
            os.rename(file, new_file)

            files_renamed_count += 1
else:
    print(f'Replaced "{files_renamed_count}" of "{files_count}" files.')


