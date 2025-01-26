import requests

# Replace with your actual LLM API endpoint and token
LLM_AAS_ENDPOINT = "https://your_actual_endpoint_here"  # Replace with your actual endpoint
LLM_AAS_TOKEN = "your_actual_token_here"  # Replace with your actual token

def call_llm(prompt: str, model_name: str = "your_llm_model_name"):
    """
    Send a prompt to the LLM API and return the response.

    Args:
        prompt (str): The prompt to send to the LLM.
        model_name (str): The LLM model to use.

    Returns:
        dict: The response from the LLM API.
    """
    headers = {"X-Api-Key": LLM_AAS_TOKEN}
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    response = requests.post(f"{LLM_AAS_ENDPOINT}/v1/chat/completions", json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def ask_question(context: str, question: str):
    """
    Construct a prompt and send it to the LLM.

    Args:
        context (str): The context to include in the prompt.
        question (str): The question to ask the LLM.

    Returns:
        dict: The response from the LLM API.
    """
    prompt = f"""
    Can you answer the following question based on this context?

    CONTEXT:
    {context}

    QUESTION:
    {question}

    If the answer is not available in the context, return that the information is not available and do not invent things.
    """
    return call_llm(prompt)
