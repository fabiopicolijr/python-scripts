from dataclasses import dataclass


@dataclass(frozen=True)
class InterpolationSchema:
    api_name_underlined: str = '[[API_NAME_UNDERLINED]]'
    filename_begin: str = '[[FILENAME_BEGIN]]'
    method: str = '[[API_METHOD]]'
    service_category_code: str = '[[SERVICE_SHORTNAME]]'
    event_name_code: str = '[[EVENT_SHORTNAME]]'
    event_title: str = '[[EVENT_TITLE]]'
    transform: str = '[[TRANSFORM]]'
    output: str = '[[OUTPUT]]'
