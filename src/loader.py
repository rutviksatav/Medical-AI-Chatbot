from langchain_community.document_loaders import PyPDFLoader
from typing import List

def load_document(file_path):
    """
    Loads a PDF document and returns its content.

    Parameters:
        file_path (str): The path to the PDF file.

    Returns:
        List[dict]: A list of dictionaries containing the document's content.
    """
    try:
        loader = PyPDFLoader(file_path)
        document = loader.load()
        return document
    except Exception as e:
        print(f"Error loading document from {file_path}: {e}")
        return []
