class Config:
    def __init__(self, dest: str, prefix: str, url: str, selector: str) -> None:
        self.dest = dest
        self.prefix = prefix
        self.url = url
        self.selector = selector

    def __repr__(self) -> str:
        return f'Config(dest: "{self.dest}", prefix: "{self.prefix}", url: "{self.url}", selector: "{self.selector}")'
