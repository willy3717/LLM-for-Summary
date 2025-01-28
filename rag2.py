import requests

# LLM API credentials
LLM_AAS_ENDPOINT = "https://your_llm_endpoint_here"  # Replace with your endpoint
LLM_AAS_TOKEN = "your_llm_token_here"  # Replace with your token

def call_rag(llm_prompt: str, llm_name: str):
    """
    Perform a call to the RAG endpoint with pre-authentication via HEAD request.

    Args:
        llm_prompt (str): The prompt to send to the LLM.
        llm_name (str): The name of the LLM model.

    Returns:
        dict: The JSON response from the LLM API.
    """
    # Step 1: Authenticate and resolve the URL
    try:
        head_response = requests.head(
            LLM_AAS_ENDPOINT,
            allow_redirects=True,
            verify=False,  # Disable SSL verification if needed
            timeout=30
        )
        resolved_url = head_response.url
    except Exception as e:
        raise ConnectionError(f"HEAD request failed: {e}")

    # Step 2: Prepare and send the actual request
    headers = {"X-Api-Key": LLM_AAS_TOKEN}
    payload = {
        "model": llm_name,
        "messages": [{"role": "user", "content": llm_prompt}],
        "temperature": 0
    }

    try:
        post_response = requests.post(
            f"{resolved_url}/v1/chat/completions",
            json=payload,
            headers=headers,
            verify=False,  # Disable SSL verification if needed
            timeout=120
        )
        if post_response.status_code == 200:
            return post_response.json()
        else:
            raise ConnectionError(
                f"Error [{post_response.status_code}]: {post_response.text}"
            )
    except Exception as e:
        raise ConnectionError(f"POST request failed: {e}")
