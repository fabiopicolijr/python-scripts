import os
from config import context

print(f'=> Objective: Generate Marketplace HEADERS"\n')

path = context['paths']['templates']['post']['headers']['inputs'] + '\\'

# JSON TEXT PARAMETERS
old_shortname = 'worker.pay-distributions.change'
old_event_title = 'Worker Pay Distributions Change'

new_shortname = 'worker.deposit-account.add'
new_event_title = 'Worker Deposit Account Add'

# FEATURE TEXT PARAMETERS
# old_feature_name # STOPPED HERE



json_files_count = 0
JSON_FILES_REPLACED_COUNT = 0


def change_json_file(json_file):
    file_path = path + json_file

    with open(file_path, 'r') as stream:
        file_data = stream.read()
        new_file_data = file_data.replace(old_shortname, new_shortname).replace(old_event_title, new_event_title)

        with open(file_path, 'w') as stream_write:
            stream_write.write(new_file_data)


def change_feature_file(feature_file):
    file_path = path + feature_file

    with open(file_path, 'r') as stream:
        file_data = stream.read()
        new_file_data = file_data.replace(old_shortname, new_shortname).replace(old_event_title, new_event_title)

        with open(file_path, 'w') as stream_write:
            stream_write.write(new_file_data)


for filename in os.listdir(path):

    if filename.endswith('.json'):
        change_json_file(filename)

    # if filename.endswith('.feature'):
    #     change_feature_file(filename)

# print(f'Changed "{json_files_replaced_count}" of "{json_files_count}" files.')
print('=> EOF')
