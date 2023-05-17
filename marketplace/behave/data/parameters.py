# Parameters config


def get_dict_key_index_by_value(_dict: dict, value: str):
    dict_keys = list(_dict.keys())
    dict_values = list(_dict.values())

    return dict_keys[dict_values.index(value)]


rules = {
    1: "marketplace_api_headers",
    2: "marketplace_api_body_and_output",
    3: "marketplace_api_body_and_output_without_worker",
}

# Required parameters
rule = "marketplace_api_body_and_output_without_worker"
api_name = "Worker Leave"
api_service = "cancel worker leave"
api_method = "POST"
api_version = "V1"
api_url_service = "HR"

# Optional parameters
api_operation = "Cancel"
api_prefix = ""

PARAMETERS = {
    "rule_code": get_dict_key_index_by_value(rules, rule),
    "api_name": api_name,
    "api_prefix": api_prefix,
    "api_service": api_service,
    "api_version": api_version,
    "api_operation": api_operation,
    "api_method": api_method,
    "api_url_service": api_url_service,
}
