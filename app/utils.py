import os
from io import BytesIO

from PIL.Image import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

PAGE_WIDTH, PAGE_HEIGHT = A4


def fit_image_to_page(img: Image, max_width: int, max_height: int) -> Image:
    original_width, original_height = img.size
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    print("return fitted image")
    return img.resize((new_width, new_height))


def add_image_to_pdf(img: Image, canvas: Canvas) -> None:
    print("fit image")
    fitted_img = fit_image_to_page(img, PAGE_WIDTH, PAGE_HEIGHT)

    x = (PAGE_WIDTH - fitted_img.width) / 2
    y = (PAGE_HEIGHT - fitted_img.height) / 2

    img_stream = BytesIO()
    fitted_img.save(img_stream, format="JPEG", optimize=True)
    img_stream.seek(0)

    print("draw image")
    canvas.drawImage(
        ImageReader(fitted_img), x, y, width=fitted_img.width, height=fitted_img.height
    )
    print("show page")
    canvas.showPage()


def create_directory_if_not_exists(dirname: str) -> None:
    if not os.path.exists(dirname):
        os.mkdir(dirname)
