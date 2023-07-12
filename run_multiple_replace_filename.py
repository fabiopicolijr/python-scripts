import os

API_FOLDER = "worker_assignment_terminate"
projects = "C:/Users/fabio.picoli/projects"
marketplace = "adp/automation/ala.marketplace/marketplace/features/data/br"

path = f"{projects}/{marketplace}/{API_FOLDER}/v1/post/404/inputs"
# path = (
#     f"{projects}/fabiopicolijr/python-scripts/behave_replacer/templates/"
#     "rule_1/overlap/headers/data/200/inputs"
# )


search_replace = [
    {"old": "worker_terminate", "new": "worker_assignment_terminate"}
    # {"old": "[[API_METHOD]]", "new": "[[API_OPERATION]]"}
]

files_count = 0
files_renamed_count = 0

print("processing...")

for filename in os.listdir(path):
    files_count += 1

    for replace_tag in search_replace:
        if filename.find(replace_tag["old"]) >= 0:
            file = f"{path}/{filename}"
            new_file = (
                f'{path}/{filename.replace(replace_tag["old"], replace_tag["new"])}'
            )
            os.rename(file, new_file)

            files_renamed_count += 1
else:
    print(f'Replaced "{files_renamed_count}" of "{files_count}" files.')
