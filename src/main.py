import os
import logging
from dotenv import load_dotenv
from loader import load_document
from splitter import split_document
from vectorestore import create_retriever
from prompt import create_chat_prompt
from chain import create_rag_chain
from model import llm
import log_config  # Import logging configuration

# Load environment variables once
load_dotenv()
# Load and preprocess document once
FILEPATH = r"/Users/rutvik/Developer/DS/Medical-AI-Chatbot/data/Gale Encyclopedia of Medicine. Vol. 1. 2nd Edition ( PDFDrive ).pdf"
docs = load_document(FILEPATH)
# docs = docs[:200]  # Limit document size if needed
split_doc = split_document(docs)
retriever = create_retriever(splitted_doc=split_doc)
prompt = create_chat_prompt()
model = llm()

logging.info("All components initialized.")

def main(query):
    """Handles user query and returns an answer."""
    logging.info(f"User Query: {query}")
    try:
        # Use preloaded components
        answer = create_rag_chain(retriever=retriever, llm=model, prompt=prompt, query=query)
        logging.info(f"Answer: {answer}")
        return answer
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Query processing finished.")

if __name__ == "__main__":
    # query = "What is the definition of Acetaminophen?"
    # print(main(query))  # Example query'
    main()
