import streamlit as st
from main import main  # Import the main function

# Streamlit UI
st.set_page_config(page_title="Medical AI Chatbot", layout="wide")
st.title("🩺 Medical AI Assistant")
st.write("Ask me anything related to medicine. I will provide answers based on the **Gale Encyclopedia of Medicine**.")

# Starter templates
starter_questions = [
    "What is Acetaminophen?",
    "What are the symptoms of diabetes?",
    "How is hypertension treated?",
    "What are the causes of migraines?",
    "Tell me about the side effects of Ibuprofen."
]

st.sidebar.title("💡 Try These Questions")
for question in starter_questions:
    if st.sidebar.button(question):
        st.session_state["query"] = question
        st.rerun()

# Initialize chat history if not present
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat interface
def display_chat():
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

display_chat()

# User Input
query = st.chat_input("Type your question and press Enter:")
if query or "query" in st.session_state:
    if not query:
        query = st.session_state.pop("query")

    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": query})

    with st.chat_message("assistant"):
        with st.spinner("Fetching answer..."):
            try:
                answer = main(query)  # Call the main function from main.py
            except Exception as e:
                answer = f"An error occurred: {e}"
            st.write(answer)

    # Add assistant response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": answer})

    # Refresh chat display
    st.rerun()
