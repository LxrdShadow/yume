from colorama import Fore, Style

from src.config import Config


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

    return Config(dest, prefix, url, selector)


if __name__ == "__main__":
    main()
