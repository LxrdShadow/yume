import os
from typing import List

from PIL import Image as PILImage
from PIL.Image import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 20

# You can tweak this for the height of the image to save
# eg: 1.5, 1.7, 2.5...
# Lower value mean taller image when splitting vertically
SPLIT_HEIGHT_FACTOR = 2

SLICE_OVERLAP = 50  # Pixels of overlap between slices (prevents awkward cuts)


def fit_image_to_page(img: Image, max_width: int, max_height: int) -> Image:
    """Resize the image for it to fit right in a page.

    img: PIL.Image
    """
    original_width, original_height = img.size
    ratio = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    return img.resize((new_width, new_height), PILImage.LANCZOS)


def split_image_vertically(
    img: Image, max_height: int, overlap: int = 0
) -> List[Image]:
    """Split a tall image into vertical chunks with optional overlap.

    img: PIL.Image
    """
    width, height = img.size
    slices = []
    y = 0

    while y < height:
        bottom = min(y + max_height, height)
        slices.append(img.crop((0, y, width, bottom)))
        y += max_height - overlap  # shift down with overlap

    return slices


def add_image_to_pdf(img: Image, canvas: Canvas) -> None:
    """Add an image to the pdf.

    img: PIL.Image
    canvas: reportlab.pdfgen.canvas.Canvas
    """
    # Convert to RGB if needed
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    max_display_width = int(PAGE_WIDTH - 2 * MARGIN)
    max_display_height = int(PAGE_HEIGHT - 2 * MARGIN)
    split_height = int(PAGE_HEIGHT * SPLIT_HEIGHT_FACTOR)

    if img.height > split_height:
        # If it's tall then split into parts
        slices = split_image_vertically(img, split_height, overlap=SLICE_OVERLAP)
        for chunk in slices:
            fitted_chunk = fit_image_to_page(
                chunk, max_display_width, max_display_height
            )
            x = (PAGE_WIDTH - fitted_chunk.width) / 2
            y = (PAGE_HEIGHT - fitted_chunk.height) / 2
            canvas.drawImage(
                ImageReader(fitted_chunk),
                x,
                y,
                width=fitted_chunk.width,
                height=fitted_chunk.height,
            )
            canvas.showPage()
    else:
        # Fits as is
        fitted_img = fit_image_to_page(img, max_display_width, max_display_height)
        x = (PAGE_WIDTH - fitted_img.width) / 2
        y = (PAGE_HEIGHT - fitted_img.height) / 2
        canvas.drawImage(
            ImageReader(fitted_img),
            x,
            y,
            width=fitted_img.width,
            height=fitted_img.height,
        )
        canvas.showPage()


def create_directory_if_not_exists(dirname: str) -> None:
    """Create a directory if it does not exist"""
    if not os.path.exists(dirname):
        os.mkdir(dirname)
