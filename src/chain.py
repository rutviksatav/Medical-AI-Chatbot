from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import RetrievalQA
import logging
import re
def create_rag_chain(retriever, llm, prompt, query):
    """
    Creates a Retrieval-Augmented Generation (RAG) chain for question answering,
    invokes it with a given query, and prints the answer.

    Args:
        retriever: The retriever object used to fetch relevant documents.
        llm: The language model to be used for generating answers.
        prompt: The prompt template for formatting the input to the language model.
        query: The question input to invoke the RAG chain.

    Returns:
        rag_chain: The initialized RAG chain for question answering.
    """

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    answer = rag_chain.invoke({"input": query})
    translated_text = re.sub(r'<think>.*?</think>\n\n', '', answer['answer'], flags=re.DOTALL)
    # logging.info(f"Context: {answer['context']}")
    logging.info(f"Answer: {translated_text}")
    return translated_text

# Example usage
# rag_chain = create_rag_chain(retriever, llm, prompt, "What is the definition of Acetaminophen?")
