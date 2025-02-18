from langchain_core.prompts import ChatPromptTemplate

def create_chat_prompt(context_placeholder="{context}", input_placeholder="{input}"):
    """
    Creates a ChatPromptTemplate for a Medical AI assistant that strictly answers only from the provided data.

    Args:
        context_placeholder (str): Placeholder for the retrieved context. Default is '{context}'.
        input_placeholder (str): Placeholder for the user's input. Default is '{input}'.

    Returns:
        ChatPromptTemplate: Configured ChatPromptTemplate for medical Q&A tasks.
    """
    system_prompt = (
        "You are a specialized AI assistant designed for medical question-answering. "
        "You must strictly answer ONLY using the retrieved medical context provided to you. "
        "DO NOT use any outside knowledge or make assumptions. If the retrieved context "
        "does not contain enough information to answer the question, respond with:\n\n"
        "'I'm sorry, but I couldn't find relevant information in the available data. "
        "Please consult a medical professional for accurate advice.'\n\n"
        f"{context_placeholder}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", input_placeholder),
        ]
    )

    return prompt
