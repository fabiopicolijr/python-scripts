from dataclasses import dataclass, field

from marketplace.behave.classes.api_body import ApiBody


@dataclass()
class Api:
    name: str
    prefix: str
    service: str
    version: str
    operation: str
    method: str
    url_service: str
    body: ApiBody = field(init=False, repr=True)

    def __post_init__(self):
        event_title = f'{"-".join(self.name.split())}.{self.operation}'.lower()
        event_name_code = f'{self.name} {self.operation}'

        if self.prefix:
            event_title = f'{self.prefix}.{event_title}'.lower()

        if self.prefix:
            event_name_code = f'{self.prefix} {event_name_code}'

        if self.method == 'POST' and self.operation:
            self.service = f'{self.service} {self.operation}'

        self.body = ApiBody(
            service_category_code=self.url_service,
            event_title=event_title,
            event_name_code=event_name_code
        )
