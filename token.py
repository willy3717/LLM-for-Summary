def parse_pdf_by_tokens(pdf_path, max_tokens=1000):
    """
    Parses a PDF file and returns text chunks of approximately `max_tokens` tokens.

    Args:
        pdf_path (str): Path to the PDF file.
        max_tokens (int): Maximum number of tokens per chunk.

    Returns:
        list[str]: A list of text chunks, each with up to `max_tokens` tokens.
    """
    def tokenize_text(text):
        """
        Tokenizes text using a basic word-based approximation.
        Ideally, replace this with an LLM-compatible tokenizer if needed.

        Args:
            text (str): The text to tokenize.

        Returns:
            list[str]: A list of tokens.
        """
        return re.findall(r'\S+', text)  # Splits text into words as token approximation

    with pdfplumber.open(pdf_path) as pdf:
        full_text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    tokens = tokenize_text(full_text)
    chunks = []
    current_chunk = []

    for token in tokens:
        current_chunk.append(token)
        if len(current_chunk) >= max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    # Add any remaining tokens as the last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
