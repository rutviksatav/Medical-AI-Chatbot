from langchain_core.prompts import ChatPromptTemplate

def create_chat_prompt(context_placeholder="{context}", input_placeholder="{input}"):
    """
    Creates a ChatPromptTemplate for question-answering tasks.

    Args:
        context_placeholder (str): Placeholder for the context to be injected into the prompt. Default is '{context}'.
        input_placeholder (str): Placeholder for the user's input. Default is '{input}'.

    Returns:
        ChatPromptTemplate: Initialized ChatPromptTemplate for Q&A tasks.
    """
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        f"{context_placeholder}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", input_placeholder),
        ]
    )

    return prompt


