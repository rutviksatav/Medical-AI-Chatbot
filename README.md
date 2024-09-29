# Medical AI Chatbot

This project aims to develop a Generative AI-based chatbot that provides medical information sourced from the **Gale Encyclopedia of Medicine (Vol. 1, 2nd Edition)**. The chatbot will serve as an assistant to answer general medical questions, offering helpful information based on the encyclopedia data.

## Features

- **Natural Language Understanding**: The chatbot will use advanced NLP techniques to understand and respond to user queries in conversational language.
- **Medical Knowledge Base**: Powered by the extensive data from the **Gale Encyclopedia of Medicine**, the chatbot will provide accurate and reliable medical information.
- **Generative Responses**: Using state-of-the-art generative AI models, the chatbot will offer informative responses based on user queries.
- **Conversational Interface**: A user-friendly, conversational experience for asking medical questions, symptoms, treatments, and definitions.
- **Contextual Understanding**: The bot retains context, enabling follow-up questions and more in-depth conversations.

## Data Source

The main data source for the chatbot is the **Gale Encyclopedia of Medicine (Vol. 1, 2nd Edition)**, which contains information on diseases, disorders, treatments, procedures, and medical terminology.

## Project Structure

- `data/`: Contains the medical data extracted from the **Gale Encyclopedia of Medicine**.
- `model/`: Includes the Generative AI model (e.g., GPT-based model) for generating responses.
- `src/`: Contains the source code for processing user queries, interfacing with the AI model, and generating responses.
- `app.py`: The main file to run the chatbot application.
- `requirements.txt`: List of dependencies and Python libraries required to run the project.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/medical-ai-chatbot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd medical-ai-chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Load the medical data from the **Gale Encyclopedia of Medicine**:
    - Ensure the relevant files are in the `data/` directory.

5. Run the chatbot:
    ```bash
    python app.py
    ```

## Usage

After starting the chatbot, you can ask medical-related questions such as:

- What is hypertension?
- What are the symptoms of diabetes?
- How is asthma treated?
- Define pneumonia.

The chatbot will respond with detailed medical information sourced from the encyclopedia.

## Model

This chatbot leverages a **Generative Pre-trained Transformer (GPT)** model for creating conversational, human-like responses. The model is fine-tuned on medical text extracted from the **Gale Encyclopedia of Medicine** to ensure that responses are relevant and accurate in the medical domain.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).
