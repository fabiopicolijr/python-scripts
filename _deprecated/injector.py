class Injector:
    """Inject content into files"""

    def __init__(
        self,
        in_folder: str,
        out_folder: str = None,
    ):
        self.in_folder = in_folder
        self.out_folder = out_folder
        self.counter = 0
