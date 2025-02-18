import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def create_retriever(splitted_doc, api_key_env_var="GOOGLE_API_KEY", embedding_model="models/embedding-001", search_type="similarity", k=10):
    """
    Sets up a Chroma vector store and retriever.

    Args:
        splitted_doc (list): A list of document objects to be used for vectorization.
        api_key_env_var (str): The environment variable name for the API key. Default is 'GOOGLE_API_KEY'.
        embedding_model (str): The embedding model to use. Default is 'models/embedding-001'.
        search_type (str): The type of search to use in retriever. Default is 'similarity'.
        k (int): The number of top results to retrieve. Default is 10.

    Returns:
        retriever: Initialized Chroma retriever.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Fetch API key from environment variables
    api_key = os.getenv(api_key_env_var)
    if not api_key:
        raise ValueError(f"API key not found. Make sure {api_key_env_var} is set in your environment or .env file.")

    # Set the Google API key environment variable
    os.environ["GOOGLE_API_KEY"] = api_key

    # Initialize embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model=embedding_model)

    # Chroma DB path
    persist_directory = "data"
    collection_name = "chroma_collection"

    # Load or create the Chroma vector store
    chroma_db = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name=collection_name
    )

    # Check if the Chroma database has any existing vectors
    if not chroma_db._collection or not chroma_db._collection.count():
        print("Chroma database is empty. Creating a new one...")

        # Create and persist the Chroma database
        chroma_db = Chroma.from_documents(
            documents=splitted_doc,
            embedding=embeddings,
            persist_directory=persist_directory,
            collection_name=collection_name
        )
        print("Chroma is in persist mode.")
        chroma_db.persist()

    # Set up the retriever with specified search type and parameters
    retriever = chroma_db.as_retriever(search_type=search_type, search_kwargs={"k": k})
    return retriever
