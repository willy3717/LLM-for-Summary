from parse_script import parse_pdf
from rag import call_rag
import json

def main():
    # Path to the PDF file
    pdf_path = "path_to_your_pdf.pdf"  # Replace with your actual PDF file path

    # Parse the PDF
    print("Parsing the PDF...")
    first_page_text = parse_pdf(pdf_path)

    if not first_page_text:
        print("No content extracted from the PDF.")
        return

    # Prepare the question and prompt
    question = "What is the main topic of the document?"
    prompt = f"""
    Can you answer the following question based on this context?

    CONTEXT:
    {first_page_text}

    QUESTION:
    {question}

    If the answer is not available in the context, return that the information is not available and do not invent things.
    """

    # Call the LLM using call_rag
    try:
        print("Sending request to the LLM...")
        response = call_rag(prompt, llm_name="mistral-large-2407")  # Replace with your model name

        # Extract and tidy the response
        print("\nTidy Response:")
        choices = response.get("choices", [])
        if choices:
            content = choices[0]["message"]["content"]
            print(f"Content: {content.strip()}")

        # Extract token usage (optional)
        usage = response.get("usage", {})
        if usage:
            print("\nToken Usage:")
            print(f"- Completion Tokens: {usage.get('completion_tokens')}")
            print(f"- Prompt Tokens: {usage.get('prompt_tokens')}")
            print(f"- Total Tokens: {usage.get('total_tokens')}")

        # Extract system warnings (optional)
        system = response.get("system", {})
        warnings = system.get("warnings", [])
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
