# AI Agent

## 🧠 Introduction
This project is a lightweight Python-based AI research assistant that uses LangChain and Groq LLM to gather, summarize, and save up-to-date information. It provides a simple interactive CLI experience where users type a query and the agent uses tools to fetch data from the web and Wikipedia, then outputs a structured response.

## 🎯 Objective
The goal of this project is to demonstrate how to build an agent that:
- Uses a large language model (LLM) for natural language understanding and response generation.
- Integrates tool usage (web search, Wikipedia lookup, file output) to provide factual and current information.
- Returns a structured JSON-style response and optionally saves the results to a file.

## 🧰 Tools Used
The project uses the following libraries and tools:

- **[LangChain](https://python.langchain.com/)**: Agent orchestration and LLM integration.
- **[LangChain-Groq](https://www.groq.com/)**: LLM provider integration (Groq LLM).
- **[LangChain Community](https://github.com/langchain-ai/langchain-community)**: Tool wrappers for web search and Wikipedia.
- **[DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)**: Web search tool used for retrieving current information.
- **[Wikipedia](https://pypi.org/project/wikipedia/)**: Library to query Wikipedia content.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Load environment variables from a `.env` file.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Structured response schemas.

## 🚀 Getting Started
1. Clone the repository.
2. Create and activate a Python virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your `.env` file with any required credentials for the chosen LLM provider (Groq, OpenAI, Claude, etc.).

5. Run the agent:

```bash
python main.py
```

6. Follow the prompt and type your research query.

## 📁 Project Structure
- `main.py` — The main entry point that initializes the agent and prompts for user input.
- `tools.py` — Custom tools exposed to the agent:
  - `web_search` (DuckDuckGo)
  - `wiki_tool` (Wikipedia lookup)
  - `save_to_file` (append the research output to a file)
- `requirements.txt` — Python dependencies.
- `research_output.txt` — Example output file where research summaries are saved.

## ✅ How It Works
1. The agent is created with a system prompt that instructs it to be a factual, concise research assistant.
2. User input is captured and passed as a query to the agent.
3. The agent uses tools (`web_search`, `wiki_tool`, `save_to_file`) as needed to gather information.
4. The agent returns a structured response (`ResearchResponse`) that includes:
   - `topic`
   - `summary`
   - `sources`
   - `tools_used`
5. The response is printed on the console and can optionally be saved to a file.

## 🎛️ Customization
- Update `main.py` to switch LLM providers (e.g., OpenAI, Anthropic, Groq).
- Modify the `system_prompt` in `main.py` to adjust tone, output format, or tool usage.
- Add new tools in `tools.py` and register them with the agent.

## 📌 Notes
- This project currently uses **Groq LLM** by default; depending on your setup you may need API keys or credentials.
- The agent expects a structured JSON response; if the model outputs freeform text, the `structured_response` may be `None`.