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
    for ch in range(config.start, config.end + 1):
        print(f"{Fore.CYAN}\tDownloading chapter {ch}{Style.RESET_ALL}")
        create_directory_if_not_exists(config.dest)

        filename = f"{config.prefix}{ch}.pdf"
        canvas = Canvas(os.path.join(config.dest, filename), pagesize=A4)

        images = []
        try:
            url = config.url.format(ch=ch)
            page_req = requests.get(url)
            soup = BeautifulSoup(page_req.content, "html.parser")
            images = soup.select(config.selector)
        except Exception as e:
            print(f"{Fore.RED}  Failed to process {url}:{Style.RESET_ALL}")
            print({str(e)})

        for item in images:
            try:
                response = requests.get(item["src"], timeout=10)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content)).convert("RGB")

                add_image_to_pdf(img, canvas)
            except Exception as e:
                print(
                    f"{Fore.RED}  Failed to process {item['src']}:{str(e)}{Style.RESET_ALL}"
                )
                print(e)

        canvas.save()


if __name__ == "__main__":
    main()
