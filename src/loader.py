from langchain_community.document_loaders import PyPDFLoader
FILEPATH = "/workspaces/Medical-AI-Chatbot/data/Gale Encyclopedia of Medicine. Vol. 1. 2nd Edition ( PDFDrive ).pdf"
def document_loader(PATH):
    loader = PyPDFLoader(FILEPATH)
    document = loader.load()
    return document

doc = document_loader(PATH=FILEPATH)
print(doc[1].page_content)
        
        