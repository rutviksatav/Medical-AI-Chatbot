from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

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
    # Create a question-answering chain using the provided LLM and prompt
    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    # Create the retrieval chain using the retriever and question-answering chain
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Invoke the RAG chain with the provided query
    result = rag_chain.invoke({"input": query})

    # Print the answer from the result
    answer = result['answer']

    return answer

# Example usage
# rag_chain = create_rag_chain(retriever, llm, prompt, "What is the definition of Acetaminophen?")
