import pathlib
import pdfplumber
from typing import List

class Granularity:
    PAGE = "PAGE"

class Content:
    def __init__(self, text, page_number, granularity, item_number, vector, parser):
        self.text = text
        self.page_number = page_number
        self.granularity = granularity
        self.item_number = item_number
        self.vector = vector
        self.parser = parser

def parse_page_v2(path: pathlib.Path, granularity: Granularity) -> List[Content]:
    """
    Parsing a PDF file by page.

    Args:
        path (pathlib.Path): Path to the PDF file.
        granularity (Granularity): The granularity setting (e.g. PAGE).
    Returns:
        List[Content]: A list of Content objects, one for each page in the PDF.
    """
    contents: List[Content] = []
    with pdfplumber.open(str(path)) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            contents.append(
                Content(
                    text=page_text,
                    page_number=page_number,
                    granularity=granularity,
                    item_number=page_number,
                    vector=None,
                    parser="parse_page_v2"
                )
            )
    return contents
