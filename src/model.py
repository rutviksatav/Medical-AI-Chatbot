import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def llm() -> ChatGoogleGenerativeAI:
    """
    Initializes the ChatGoogleGenerativeAI model with the specified parameters.

    Returns:
        ChatGoogleGenerativeAI: An instance of the ChatGoogleGenerativeAI model.

    Raises:
        ValueError: If the GOOGLE_API_KEY is not set in the environment variables.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve Google API key from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")

    if not google_api_key:
        raise ValueError("Missing Google API key. Please set the GOOGLE_API_KEY in your .env file.")

    # Initialize the Google Generative AI model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.5,
        max_tokens=None,  # Consider setting a default value for max_tokens
        timeout=None,     # Consider setting a default value for timeout
        max_retries=2,
    )
    
    print("ChatGoogleGenerativeAI initialized successfully.")
    return llm
