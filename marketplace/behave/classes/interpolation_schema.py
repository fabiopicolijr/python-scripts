from dataclasses import dataclass


@dataclass(frozen=True)
class InterpolationSchema:
    url_main_path: str = '[[API_NAME]]'
    method: str = '[[API_METHOD]]'
    service_category_code: str = '[[SERVICE_SHORTNAME]]'
    event_name_code: str = '[[EVENT_SHORTNAME]]'
    event_title: str = '[[EVENT_TITLE]]'
    transform: str = '[[TRANSFORM]]'
    output: str = '[[OUTPUT]]'
