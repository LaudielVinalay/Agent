# Conversational Agent with LangChain, OpenRouter, and Tavily
This project implements an interactive conversational agent that combines LLMs, external tools, and conversation memory to answer questions, perform web searches, and evaluate mathematical expressions in real time.

## Key Features
- OpenRouter integration to leverage advanced language models (default: qwen/qwen3-coder:free).

- Online search powered by the Tavily API, with optimized and filtered results.

- Persistent conversation memory using MemorySaver, allowing dialogue continuity.

- Custom tool for evaluating mathematical expressions safely.

- Simple command-line interface for continuous sessions.

- Modular design with easy integration of additional tools.

## Technologies Used
- LangChain — LLM orchestration and tool integration.

- OpenRouter — Access to diverse language models.

- Tavily — Optimized search engine for AI agents.

- LangGraph — Agent workflows and memory handling.

- Python 3.10+

## How to Run
Clone the repository:
```
git clone https://github.com/username/conversational-agent.git
cd conversational-agent
```

Install dependencies:
```
pip install -r requirements.txt
```

Set your environment variables in .env:
```
OPENROUTER_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Run the agent:
```
python agent.py
```
## Example Usage

```
Enter a prompt: What is quantum computing?
[Agent responds with explanation and references]

Enter a prompt: 2+2*3
[Agent responds: 8]

Enter a prompt: Adios
[Session ends]

```

 ## Possible Future Improvements

- Integration with more OpenRouter models.
- Support for multimodal responses (text + images).
- Web interface with Flask or FastAPI.
- Database-backed memory persistence.
