from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document(doc, chunk_size=500, chunk_overlap=20):
    """
    Splits a document into smaller chunks using the RecursiveCharacterTextSplitter.

    Args:
        doc (list): A list of document objects to be split.
        chunk_size (int): The size of each chunk. Default is 500.
        chunk_overlap (int): The overlap size between chunks. Default is 20.

    Returns:
        list: A list of split document chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    # Split the document into chunks
    splitted_doc = text_splitter.split_documents(doc)
    
    return splitted_doc


