# TODO: change TASKS to CONFIGS, like:
#  id: 1, 'automation_marketplace_headers'
#  id: 2, 'automation_marketplace_body_and_output'
#  id: 3, 'progress_headers'
#  id: 4, 'progress_body_and_output'
#  each id will be an folder inside templates

ALPHA_TASKS = ['headers', 'body_and_output']

# Required fields
alpha_task = ALPHA_TASKS[1]

api_name = 'Pay Data Inputs'
api_service = 'Pay Data Input'
api_method = 'POST'
api_version = 'V1'
api_url_service = 'PAYROLL'

# Optional fields
api_operation = 'Add'
api_prefix = ''

PARAMETERS = {
    'task': alpha_task,
    'api_name': api_name,
    'api_prefix': api_prefix,
    'api_service': api_service,
    'api_version': api_version,
    'api_operation': api_operation,
    'api_method': api_method,
    'api_url_service': api_url_service
}

