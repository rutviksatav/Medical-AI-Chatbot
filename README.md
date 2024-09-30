
# GenAI Medical AI Chatbot

Welcome to the **GenAI-based Medical AI Chatbot**! This project is designed as a Retrieval-Augmented Generation (RAG) application that leverages the power of the Google Gemini 1.5 Pro model. The chatbot provides intelligent and context-aware responses to medical inquiries, enhancing user experience with accurate and reliable information.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description

The GenAI Medical AI Chatbot uses advanced Generative AI techniques to assist users with their medical queries. By implementing the Google Gemini 1.5 Pro model, this application enables dynamic interactions and provides evidence-based answers. Its architecture follows a RAG approach, where the chatbot retrieves relevant information from a database and generates coherent responses, thereby improving the quality of interactions.

## Features

- Interactive chatbot capable of answering medical questions.
- Utilizes Google Gemini 1.5 Pro model for enhanced response generation.
- Provides relevant medical information based on user queries.
- Implements a RAG architecture for efficient information retrieval.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/genai-medical-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd genai-medical-chatbot/src
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the chatbot, run the following command:
```bash
python main.py
```

You can then interact with the chatbot in your terminal or via the designated interface.

## File Structure

```
genai-medical-chatbot/
├── data/
│   └── datafile              # Contains relevant data files for the chatbot
├── src/
│   ├── __pycache__/
│   ├── app.log               # Log file for recording events and errors
│   ├── chain.py              # Handles user interactions and conversation flow
│   ├── loader.py             # Loads models and data required by the chatbot
│   ├── log_config.py         # Configuration for logging system activity
│   ├── main.py               # Entry point for the chatbot application
│   ├── model.py              # Defines the AI model and its architecture
│   ├── prompt.py             # Contains predefined prompts for generating responses
│   ├── splitter.py           # Handles splitting of user input for processing
│   └── vectorestore.py       # Manages storage and retrieval of vector representations of data
├── requirements.txt           # Lists the required packages for the project
└── README.md                  # Documentation for the project
```

### File Descriptions

- `data/`: Directory containing data files used by the chatbot.
- `src/__pycache__/`: Caches for compiled Python files for optimization.
- `app.log`: Log file for capturing runtime events.
- `chain.py`: Contains logic for handling user interactions and managing conversation flow.
- `loader.py`: Responsible for loading models and data required by the chatbot.
- `log_config.py`: Configuration for logging system activity.
- `main.py`: Entry point for the chatbot application.
- `model.py`: Defines the AI model and its architecture.
- `prompt.py`: Contains predefined prompts for generating responses.
- `splitter.py`: Handles splitting of user input for processing.
- `vectorestore.py`: Manages storage and retrieval of vector representations of data.
- `requirements.txt`: Lists all the necessary packages and their versions required to run the project.

## Logging

Logging is configured to record important events and errors in the `app.log` file. This helps in monitoring and debugging the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out to me at [your.email@example.com](mailto:your.email@example.com).
