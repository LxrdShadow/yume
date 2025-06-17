class Config:
    def __init__(
        self, dest: str, prefix: str, url: str, selector: str, start: int, end: int
    ) -> None:
        self.dest: str = dest
        self.prefix: str = prefix
        self.url: str = url
        self.selector: str = selector
        self.start: int = start
        self.end: int = end

    def __repr__(self) -> str:
        return f'Config(dest: "{self.dest}", \
prefix: "{self.prefix}", \
url: "{self.url}", \
selector: "{self.selector}", \
start: {self.start}, \
end: {self.end})'
