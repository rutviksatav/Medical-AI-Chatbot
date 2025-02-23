import streamlit as st
from main import main  # Import the main function

# Streamlit UI Config
st.set_page_config(page_title="Medical AI Chatbot", layout="wide", page_icon="🩺")

# Custom Styling
st.markdown(
    """
    <style>
        .main {background-color: #f9f9f9;}
        .stChatMessage {border-radius: 10px; padding: 10px; margin-bottom: 5px;}
        .stChatMessageUser {background-color: #e6f7ff;}
        .stChatMessageAssistant {background-color: #f4f4f4;}
        .stChatMessage span {font-size: 16px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("🩺 Medical AI Assistant")
st.write("Ask me anything related to medicine. I'll provide accurate answers based on the **Gale Encyclopedia of Medicine**.")

# Sidebar Section
with st.sidebar:
    st.title("💡 Quick Questions")
    st.write("Try one of these suggested questions:")

    starter_questions = [
        "What is Acetaminophen?",
        "What are the symptoms of diabetes?",
        "How is hypertension treated?",
        "What are the causes of migraines?",
        "Tell me about the side effects of Ibuprofen."
    ]

    selected_question = st.radio("Click to ask:", starter_questions, index=None)

    if selected_question:
        st.session_state["query"] = selected_question
        st.rerun()

    # Collapsible FAQ Section
    with st.expander("ℹ️ How It Works"):
        st.write(
            """
            - This chatbot provides medical information using the **Gale Encyclopedia of Medicine**.
            - Type a question in the chat or select a predefined question.
            - The AI will fetch and generate an accurate response.
            - Please consult a doctor for any medical concerns.
            """
        )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Function to display chat
def display_chat():
    for message in st.session_state["messages"]:
        role = message["role"]
        css_class = "stChatMessageUser" if role == "user" else "stChatMessageAssistant"
        with st.chat_message(role):
            st.markdown(f'<div class="{css_class}"><span>{message["content"]}</span></div>', unsafe_allow_html=True)

# Display chat history
display_chat()

# User Input
query = st.chat_input("Type your medical question and press Enter:")

if query or "query" in st.session_state:
    if not query:
        query = st.session_state.pop("query")

    # Store user query in chat history
    st.session_state["messages"].append({"role": "user", "content": query})

    # Display query instantly
    with st.chat_message("user"):
        st.write(query)

    # Fetch and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = main(query)  # Call the main function
            except Exception as e:
                answer = f"⚠️ An error occurred: {e}"
            st.write(answer)

    # Store assistant response in chat history
    st.session_state["messages"].append({"role": "assistant", "content": answer})

    # Refresh chat display
    st.rerun()
