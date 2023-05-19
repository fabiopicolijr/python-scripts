import os

API = "worker_leave_return_request"
projects = "C:/Users/fabio.picoli/projects"
marketplace = "adp/automation/ala.marketplace/marketplace/features/data/br"

path = f"{projects}/{marketplace}/{API}/v1/post/200/inputs"
# path = f"{projects}/fabiopicolijr/python-scripts/marketplace/behave/output"


search_replace = [
    # {
    #     "old": 'worker_leave',
    #     "new": 'wl_cancel'
    # }
    {"old": "wl_return_request_v1_v1", "new": "wl_return_request_v1"}
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
