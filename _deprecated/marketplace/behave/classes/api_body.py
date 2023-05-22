from dataclasses import dataclass


@dataclass()
class ApiBody:
    service_category_code: str
    event_name_code: str
    event_title: str
