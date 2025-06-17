from bs4 import BeautifulSoup
from colorama import Fore, Style

from src.config import Config
from src.errors import BoundError


def main() -> None:
    config = get_config()

    print(config)


def get_config() -> Config:
    print(f"\n{Fore.YELLOW}> Enter a destination directory{Style.RESET_ALL}")
    print(
        f"{Fore.LIGHTWHITE_EX}  Leave empty to use the current directory\n{Style.RESET_ALL}"
    )
    dest: str = input("destination: ") or "."

    print(f"\n{Fore.YELLOW}> Enter a prefix for the saved filenames{Style.RESET_ALL}")
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
    url = input("url: ")

    print(
        f"\n{Fore.YELLOW}> Enter the selector for the images to download{Style.RESET_ALL}"
    )
    print(
        f"{Fore.LIGHTWHITE_EX}  Use your browser's dev tools to find \
a selector matching the images\n{Style.RESET_ALL}"
    )
    selector = input("selector: ")

    while True:
        try:
            print(
                f"\n{Fore.YELLOW}> Enter the first chapter to download{Style.RESET_ALL}"
            )
            start = int(input("from chapter: "))
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
            end = int(input("to chapter: "))
            if start > end:
                raise BoundError("Start chapter can't be higher than the end chapter")

            break
        except BoundError as e:
            print(f"\n{Fore.RED}  Value error. {str(e)}{Style.RESET_ALL}")

        except Exception:
            print(
                f"\n{Fore.RED}  Value error. Please enter a valid chapter number{Style.RESET_ALL}"
            )

    return Config(dest, prefix, url, selector, start, end)


if __name__ == "__main__":
    main()
