from dataclasses import dataclass, field

from marketplace.behave.classes.api_body import ApiBody


@dataclass()
class Api:
    version: str
    service: str
    prefix: str
    name: str
    method: str
    title: str = field(init=False, repr=True)
    url_main_path: str = field(init=False, repr=True)
    body: ApiBody = field(init=False, repr=True)

    def __post_init__(self):
        self.title = f'{self.prefix} {self.name}'.title()
        self.url_main_path = f"{'_'.join(self.title.split()).lower()}"
        self.method = self.method.lower()
        self.body = ApiBody(
            service_category_code=self.service,
            event_title=f'{self.prefix.lower()}.{"-".join(self.name.split()).lower()}.{self.method}',
            event_name_code=f'{self.title} {self.method.capitalize()}'
        )
