# Research Agent

An AI-powered research agent built with Pydantic AI.

## Features

- Automated research capabilities
- Asynchronous operations
- Structured logging with Logfire
- Modular architecture

## Installation

Install dependencies:

```bash
python -m pip install pydantic-ai logfire aiohttp httpx tenacity python-dotenv
```

Or using the project file:

```bash
python -m pip install -e .
```

## Configuration

Create a `.env` file in the project root with your configuration:

```env
# Add your API keys and configuration here
```

## Usage

Run the research agent:

```bash
python agent_main.py
```

## Project Structure

- `agent_main.py` - Main entry point for the agent
- `tools.py` - Research tools and utilities
- `models.py` - Pydantic data models
- `log_config.py` - Logging configuration
- `pyproject.toml` - Project dependencies and metadata

## Development

TODO: Add development instructions

## License

TODO: Add license information
