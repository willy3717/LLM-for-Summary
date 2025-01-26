from parse_script import parse_page_v2, Granularity
from ask_llm import ask_question
import pathlib

def main():
    # Path to your PDF
    pdf_path = pathlib.Path("path_to_your_pdf.pdf")  # Replace with your actual PDF file path

    # Parse the PDF
    print("Parsing the PDF...")
    contents = parse_page_v2(pdf_path, Granularity.PAGE)

    # Ensure the PDF was parsed successfully
    if not contents:
        print("No content found in the PDF.")
        return

    # Get the first page's content
    first_page_text = contents[0].text

    # Ask the LLM a question using the first page's content as context
    question = "What is the main topic of the document?"
    print("Asking the LLM...")
    try:
        response = ask_question(first_page_text, question)
        print("LLM Response:")
        print(response["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
