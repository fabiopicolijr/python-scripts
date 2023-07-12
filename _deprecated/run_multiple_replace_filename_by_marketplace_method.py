import os

# TEMP VARIABLES
method = "modify"
error_code_folder = "400"
io_folder = "inputs"

# CONST VARIABLES

TEMPLATES_PATH = (
    f"C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace/marketplace/features/files/br/"
    f"{io_folder}/{error_code_folder}/pay_data_inputs/{method}"
)

REPLACE_TAGS = [{"old": "_add_", "new": f"_{method}_"}]

files_count = 0
files_renamed_count = 0

print("processing...")

for filename in os.listdir(TEMPLATES_PATH):
    files_count += 1

    for replace_tag in REPLACE_TAGS:
        if filename.find(replace_tag["old"]) >= 0:
            file = f"{TEMPLATES_PATH}/{filename}"
            new_file = f'{TEMPLATES_PATH}/{filename.replace(replace_tag["old"], replace_tag["new"])}'
            os.rename(file, new_file)

            files_renamed_count += 1
else:
    print(f'Replaced "{files_renamed_count}" of "{files_count}" files.')
