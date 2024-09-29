import os
import logging
from dotenv import load_dotenv
from loader import load_document
from splitter import split_document
from vectorestore import create_retriever
from prompt import create_chat_prompt
from chain import create_rag_chain
from model import llm

# Import logging configuration
import log_config  # Use the new filename

FILEPATH = r"/Users/rutvik/Developer/DS/Medical-AI-Chatbot/data/Gale Encyclopedia of Medicine. Vol. 1. 2nd Edition ( PDFDrive ).pdf"
query = "what is Definition of Acetaminophen?"

def main():
    logging.info("Application started.")
    try:
        # Load environment variables
        load_dotenv()
        logging.info("Environment variables loaded.")

        # Load document
        docs = load_document(FILEPATH)
        docs = docs[:50]
        logging.info(f"Document loaded from {FILEPATH}.")

        # Split document
        split_doc = split_document(docs)
        logging.info("Document split into sections.")

        # Create retriever
        retriever = create_retriever(splitted_doc=split_doc)
        logging.info("Retriever created.")

        # Create chat prompt
        prompt = create_chat_prompt()
        logging.info("Chat prompt created.")

        # Initialize model
        model = llm()
        logging.info("Language model initialized.")

        # Create answer using the RAG chain
        answer = create_rag_chain(retriever=retriever, llm=model, prompt=prompt, query=query)
        logging.info("Answer generated.")

        # Print the answer
        print(answer)  # Add this line to print the generated answer

        return answer
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Application finished.")

if __name__ == "__main__":
    main()
