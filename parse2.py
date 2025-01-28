import pathlib
import pdfplumber

def parse_pdf(pdf_path):
    """
    Parse the PDF and return the content of the first page as text.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Text content of the first page, or None if the PDF is empty.
    """
    with pdfplumber.open(pdf_path) as pdf:
        if len(pdf.pages) == 0:
            print("The PDF is empty.")
            return None
        # Extract text from the first page
        first_page = pdf.pages[0]
        return first_page.extract_text()
