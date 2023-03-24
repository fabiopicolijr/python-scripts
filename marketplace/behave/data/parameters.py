from marketplace.behave.config import JIRA_TASKS

PARAMETERS = {
    'version': 'V1',
    'service': 'PAYROLL',
    'prefix': 'Worker',
    'name': 'Pay Data Inputs',
    'method': 'Add',
    'request_method': 'post',
    'task': JIRA_TASKS[1]
}

