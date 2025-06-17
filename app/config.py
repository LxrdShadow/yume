from colorama import Fore, Style

from app.errors import BoundError


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

    @staticmethod
    def get_config():
        print(f"\n{Fore.YELLOW}> Enter a destination directory{Style.RESET_ALL}")
        print(
            f"{Fore.LIGHTWHITE_EX}  Leave empty to use the current directory\n{Style.RESET_ALL}"
        )
        dest: str = input("destination: ") or "kaiju"

        print(
            f"\n{Fore.YELLOW}> Enter a prefix for the saved filenames{Style.RESET_ALL}"
        )
        print(f'{Fore.LIGHTWHITE_EX}  Leave empty to use "Ch-" prefix{Style.RESET_ALL}')
        print(
            f'{Fore.LIGHTWHITE_EX}  Ex: For the prefix "parasite-" generates:{Style.RESET_ALL}'
        )
        print(f"{Fore.LIGHTWHITE_EX}    > parasite-1.pdf \n{Style.RESET_ALL}")
        prefix: str = input("prefix: ") or "Ch-"

        print(f"\n{Fore.YELLOW}> Enter the url{Style.RESET_ALL}")
        print(
            f'{Fore.MAGENTA}  Put "{{ch}}" at where the Chapter number should be{Style.RESET_ALL}\n'
        )
        print(
            f"{Fore.LIGHTWHITE_EX}\
        Ex: https://example.com/manga/parasite-chapter-{{ch}}/view?chapter={{ch}}\n\
          > https://example.com/manga/parasite-chapter-1/view?chapter=1 \
            {Style.RESET_ALL}\n"
        )
        url = input("url: ") or "https://kaijumanga.co/manga/chapter-{ch}/"

        print(
            f"\n{Fore.YELLOW}> Enter the selector for the images to download{Style.RESET_ALL}"
        )
        print(
            f"{Fore.LIGHTWHITE_EX}  Use your browser's dev tools to find \
    a selector matching the images\n{Style.RESET_ALL}"
        )
        selector = input("selector: ") or ".manga-image"

        while True:
            try:
                print(
                    f"\n{Fore.YELLOW}> Enter the first chapter to download{Style.RESET_ALL}"
                )
                start = int(input("from chapter: ")) or 1
                break
            except Exception:
                print(
                    f"\n{Fore.RED}  Value error. Please enter a valid chapter number{Style.RESET_ALL}"
                )

        while True:
            try:
                print(
                    f"\n{Fore.YELLOW}> Enter the last chapter to download{Style.RESET_ALL}"
                )
                end = int(input("to chapter: ")) or 1
                if start > end:
                    raise BoundError(
                        "Start chapter can't be higher than the end chapter"
                    )

                break
            except BoundError as e:
                print(f"\n{Fore.RED}  Value error. {str(e)}{Style.RESET_ALL}")

            except Exception:
                print(
                    f"\n{Fore.RED}  Value error. Please enter a valid chapter number{Style.RESET_ALL}"
                )

        return Config(dest, prefix, url, selector, start, end)
