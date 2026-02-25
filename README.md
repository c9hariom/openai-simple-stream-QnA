# Python LLM Chat Application

A FastAPI-based chat application that integrates with OpenAI's language models for intelligent conversation capabilities.

## Features

- **FastAPI Web Server** - Fast, modern Python web framework
- **OpenAI Integration** - Powered by OpenAI's advanced language models
- **Async Streaming** - Real-time streaming responses for interactive chat
- **LangChain Integration** - Leverages LangChain for LLM orchestration

## Prerequisites

- Python 3.8 or higher
- Virtual environment (venv)
- OpenAI API key

## Installation

1. **Clone or download the project**
   ```bash
   cd "c:\Users\c9har\Desktop\Learning\Python - Andre"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows PowerShell
   # or
   source venv/bin/activate     # On Linux/macOS
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API credentials:
   ```
   OPENAI_ENDPOINT=https://api.openai.com/v1
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL_NAME=gpt-4-turbo
   OPENAI_MODEL_4_1_NANO=gpt-4-mini
   ```

## Running the Application

Start the development server:
```bash
python launcher.py
```

The server will run on `http://localhost:8000`

## API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI (Docs)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc (Alternative Docs)**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Both endpoints provide interactive API exploration and testing capabilities.

## Project Structure

```
.
├── launcher.py              # Application entry point
├── requirements.txt         # Project dependencies
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore rules
├── ftp.py                  # FTP utilities
├── api/                    # API endpoints
│   └── chat.py            # Chat endpoint
├── app/                    # Application core
│   └── main.py            # FastAPI app initialization
├── core/                   # Core configuration
│   └── config.py          # Settings and environment variables
├── model/                  # Data models
│   └── chat.py            # Chat-related models
└── service/                # Business logic
    └── llm_service.py     # LLM integration service
```

## Dependencies

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **langchain** - LLM orchestration framework
- **langchain-openai** - OpenAI integration for LangChain
- **pydantic** - Data validation
- **pydantic-settings** - Settings management
- **httpx** - Async HTTP client
- **python-dotenv** - Environment variable management

## Development

The application runs in development mode with auto-reload enabled. Any changes to the core, api, app, service, or model directories will trigger a server restart.

## License

Add your license information here.
