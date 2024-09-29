from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document(doc, chunk_size=500, chunk_overlap=20):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    splitted_doc = text_splitter.split_documents(doc)
    return splitted_doc


