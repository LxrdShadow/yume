import os
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas

from app.config import Config
from app.utils import add_image_to_pdf, create_directory_if_not_exists


def main() -> None:
    config = Config.get_config()

    print(config)
    print()
    for ch in range(config.start, config.end + 1):
        print(f"{Fore.CYAN}\tDownloading chapter {ch}{Style.RESET_ALL}")
        create_directory_if_not_exists(config.dest)

        filename = f"{config.prefix}{ch}.pdf"
        filepath = os.path.join(config.dest, filename)
        canvas = Canvas(filepath, pagesize=A4)

        image_tags = []
        try:
            url = config.url.format(ch=ch)
            page_req = requests.get(url)
            soup = BeautifulSoup(page_req.content, "html.parser")
            image_tags = soup.select(config.selector)
        except Exception as e:
            print(f"{Fore.RED}  Failed to process {url}:{Style.RESET_ALL}")
            print(str(e))

        for item in image_tags:
            try:
                print(f"Downloading: {item['src']}", end="\t")
                response = requests.get(item["src"], timeout=10)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content)).convert("RGB")

                add_image_to_pdf(img, canvas)
                print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[FAILED]{Style.RESET_ALL}")
                print(
                    f"{Fore.RED}  Failed to process {item['src']}:{str(e)}{Style.RESET_ALL}"
                )
                print(str(e))

        canvas.save()

    print(f"{Fore.GREEN}\tDownload finished{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
