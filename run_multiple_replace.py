from utils.multiple_replace import MultipleReplace

in_folder = f'C:/Users/fabio.picoli/projects/adp/automation/ala.marketplace/marketplace/features/files/br/inputs/400/pay_data_inputs/replace'
# in_folder = f'C:/Users/fabio.picoli/projects/fabiopicolijr/python-scripts/temp/files'
search_replace = [
    {
        "old": f"pay-data-input.add",
        "new": f"pay-data-input.replace",
    },
    {
        "old": f"Pay Data Input Add",
        "new": f"Pay Data Input Replace",
    },
]

if __name__ == '__main__':
    print(f'Processing...')

    mr = MultipleReplace(search_replace, in_folder)

    try:
        mr.process_files()
        print(f'\nProcess finished: Replaced "{mr.replaced_count}" times')
    except Exception as e:
        print(e)
