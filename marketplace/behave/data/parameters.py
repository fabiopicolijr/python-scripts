# Parameters config

def get_dict_key_index_by_value(_dict: dict, value: str):
    dict_keys = list(_dict.keys())
    dict_values = list(_dict.values())

    return dict_keys[dict_values.index(value)]


rules = {
    1: 'marketplace_api_headers',
    2: 'marketplace_api_body_and_output',
}

# Required parameters
rule = 'marketplace_api_body_and_output'
api_name = 'Pay Data Inputs'
api_service = 'Pay Data Input'
api_method = 'POST'
api_version = 'V1'
api_url_service = 'PAYROLL'

# Optional parameters
api_operation = 'Add'
api_prefix = ''

PARAMETERS = {
    'rule_code': get_dict_key_index_by_value(rules, rule),
    'api_name': api_name,
    'api_prefix': api_prefix,
    'api_service': api_service,
    'api_version': api_version,
    'api_operation': api_operation,
    'api_method': api_method,
    'api_url_service': api_url_service
}
