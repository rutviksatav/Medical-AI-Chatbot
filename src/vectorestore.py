import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def create_retriver(splitted_doc, api_key_env_var="GOOGLE_API_KEY", embedding_model="models/embedding-001", search_type="similarity", k=10):
    """
    Sets up a Chroma vector store and retriever.

    Args:
        splitted_doc (list): A list of document objects to be used for vectorization.
        api_key_env_var (str): The environment variable name for the API key. Default is 'GOOGLE_API_KEY'.
        embedding_model (str): The embedding model to use. Default is 'models/embedding-001'.
        search_type (str): The type of search to use in retriever. Default is 'similarity'.
        k (int): The number of top results to retrieve. Default is 10.

    Returns:
        vectorstore, retriever: Initialized Chroma vectorstore and retriever.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Fetch API key from environment variables
    api_key = os.getenv(api_key_env_var)
    if api_key is None:
        raise ValueError(f"API key not found. Make sure {api_key_env_var} is set in your environment or .env file.")
    
    # Set the Google API key environment variable
    os.environ["GOOGLE_API_KEY"] = api_key

    # Initialize embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)

    # Set up the Chroma vector store with the provided documents and embeddings
    vectorstore = Chroma.from_documents(documents=splitted_doc, embedding=embeddings)

    # Set up the retriever with specified search type and parameters
    retriever = vectorstore.as_retriever(search_type=search_type, search_kwargs={"k": k})

    return retriever

