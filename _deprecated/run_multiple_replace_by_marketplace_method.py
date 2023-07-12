from utils.multiple_replace import MultipleReplace

# TEMP VARIABLES
old_method = "add"
new_method = "modify"

# CONST VARIABLES
in_folder = f"C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace/ \
    marketplace/features/files/br/inputs/400/pay_data_inputs/{new_method}"

search_replace = [
    {
        "old": f"pay-data-input.{old_method.lower()}",
        "new": f"pay-data-input.{new_method.lower()}",
    },
    {
        "old": f"Pay Data Input {old_method.capitalize()}",
        "new": f"Pay Data Input {new_method.capitalize()}",
    },
]

if __name__ == "__main__":
    print("Processing...")

    processor = MultipleReplace(search_replace, in_folder)

    try:
        processor.process_files()
        print(f'\nProcess finished: Replaced "{processor.replaced_count}"')
    except Exception as e:
        print(e)
