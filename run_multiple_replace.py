from utils.multiple_replace import MultipleReplace

projects = "C:/Users/fabio.picoli/projects"

# path = f'{projects}/adp/automation/ala.marketplace/marketplace/features/files/br/inputs/400/pay_data_inputs/replace'
# path = f"{projects}/fabiopicolijr/python-scripts/marketplace/behave/files/rule_3/templates"
path = f"{projects}/fabiopicolijr/python-scripts/marketplace/behave/output"

search_replace = [
    {
        "old": '"effectiveDateTime": "2023-01-20T15:15:00Z"',
        "new": '"effectiveDateTime": "2014-01-01T00:00:00Z"',
    },
]

if __name__ == "__main__":
    print("Processing...")

    mr = MultipleReplace(search_replace, path)

    try:
        mr.process_files()
        print(f'\nProcess finished: Replaced "{mr.replaced_count}" times')
    except Exception as e:
        print(e)
