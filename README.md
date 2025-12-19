# Emotion-Leila-V2: Fear-Focused Empathetic Chatbot

An AI-powered chatbot designed to help users explore and confront their fears in a safe, supportive environment. Built with Google's Gemini API, emotion detection models, and memory systems for adaptive, personalized conversations.

## Features

- **Emotion Detection**: Real-time emotion classification using state-of-the-art NLP models
- **Empathetic Responses**: Gemini-powered responses tailored to detected emotional states
- **Conversation Memory**: Maintains context across conversation turns
- **Self-Reflection**: Bot self-awareness and reflection capabilities
- **Fear-Focused Dialogue**: Specialized prompting for anxiety and fear management

## Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key
- Hugging Face token (for emotion models)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/talithea/emotion-agent-v2.git
cd emotion-agent-v2
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate  # Linux/macOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root:
```
API_KEY=your_google_gemini_api_key
HF_TOKEN=your_hugging_face_token
```

**Never commit `.env` to version control.** It's in `.gitignore` by default.

### Usage

Run the chatbot backend:
```bash
python src/agent/main.py
```

Or use the Jupyter notebook for interactive exploration:
```bash
jupyter notebook notebooks/backend.ipynb
```

## Project Structure

```
├── README.md                 <- This file
├── SECURITY.md              <- Security guidelines and secret rotation
├── requirements.txt         <- Project dependencies
├── LICENSE
│
├── data/                    <- Data directory
│   ├── external/           <- Third-party data
│   ├── interim/            <- Intermediate transformations
│   ├── processed/          <- Final datasets
│   └── raw/                <- Original, immutable data
│
├── models/                 <- Trained and serialized models
│
├── notebooks/              <- Jupyter notebooks
│   └── backend.ipynb      <- Backend configuration and testing
│
├── reports/                <- Generated analysis and reports
│   └── figures/           <- Generated graphics
│
├── src/                    <- Source code
│   ├── agent/             <- Core chatbot agent
│   │   ├── agent.py      <- Main agent logic
│   │   ├── main.py       <- Chatbot entry point
│   │   ├── memory.py     <- Conversation memory management
│   │   └── planning.py   <- Response planning
│   │
│   ├── dialogue/          <- Dialogue management
│   │   ├── prompts.py    <- System prompts and templates
│   │   └── response.py   <- Response generation
│   │
│   ├── emotion/           <- Emotion detection
│   │   └── emotion.py    <- Emotion classification models
│   │
│   ├── modeling/          <- ML models and training
│   │   ├── train.py      <- Model training pipeline
│   │   └── predict.py    <- Inference utilities
│   │
│   └── utils/             <- Utility functions
│       ├── api_client.py  <- API clients (Gemini, HF, etc.)
│       ├── config.py      <- Configuration management
│       └── logging.py     <- Logging setup
│
└── references/            <- Manuals and explanatory materials
```

## Environment Setup

### Required Environment Variables

```env
API_KEY              # Google Gemini API key
HF_TOKEN             # Hugging Face user access token
```

To get these:
- **Google Gemini API**: [Google AI Studio](https://aistudio.google.com/app/apikey)
- **Hugging Face Token**: [HF Account Settings](https://huggingface.co/settings/tokens)

### Secure Secret Management

Secrets should **never** be hardcoded or committed to version control. Always use environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
```

For detailed security practices, see `SECURITY.md`.

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

This project follows PEP 8. Format code with:
```bash
black src/
```

### Dependencies

Core dependencies:
- `torch` - Deep learning framework
- `transformers` - NLP models (Hugging Face)
- `nltk` - Natural language tools
- `requests` - HTTP client for APIs
- `python-dotenv` - Environment variable management
- `pandas`, `numpy`, `scikit-learn` - Data science tools
- `matplotlib`, `seaborn` - Visualization

See `requirements.txt` for complete list.

## Architecture

### Emotion Detection Pipeline
1. User input → Emotion classifier (DistilRoBERTa + Albert models)
2. Emotion label + confidence → Passed to dialogue system

### Response Generation
1. Emotion context + conversation history → System prompt builder
2. Prompt + history → Gemini API request
3. Gemini response → Memory storage + self-reflection
4. Response → User

### Memory System
- Stores conversation turns: (user_input, bot_response)
- Updates bot self-model with reflections
- Enables context-aware follow-ups

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -m "Add your feature"`
3. Push to branch: `git push origin feature/your-feature`
4. Open a pull request

## Security

**Important:** API keys and tokens are sensitive. Never commit them. See `SECURITY.md` for:
- Rotating exposed secrets
- Purging secrets from git history
- Best practices for environment management

## License

This project is licensed under the MIT License. See `LICENSE` file for details.

## Support

For issues, questions, or contributions, open an issue on [GitHub](https://github.com/talithea/emotion-agent-v2/issues).

## Acknowledgments

- Google Gemini API for core LLM capabilities
- Hugging Face for pre-trained emotion models
- NLTK for NLP utilities

--------
