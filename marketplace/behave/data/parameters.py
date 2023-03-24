from marketplace.behave.config import JIRA_TASKS

# Required fields

# Optional fields
filename_begin = 'pay_data_inputs'  # optional, used to modify the filename pattern

PARAMETERS = {
    'version': 'V1',
    'service': 'PAYROLL',
    'prefix': '',
    'name': 'Pay Data Input',
    'filename_begin': filename_begin,
    'method': 'Add',
    'request_method': 'post',
    'task': JIRA_TASKS[1]
}

