# llm

Workspace holding multiple standalone LLM demo projects. Each project lives in its own
folder with its own `requirements.txt`, `.env`, and README — run them independently.

## Concepts

- [concepts/](concepts/) — plain-English explanations, architecture diagrams, and
  real-world scenarios for: [Prompt Engineering](concepts/01-prompt-engineering.md),
  [LLM](concepts/02-llm.md), [RAG](concepts/03-rag.md), [Fine-tuning](concepts/04-fine-tuning.md),
  [Embeddings](concepts/05-embeddings.md), [MCP Server](concepts/06-mcp-server.md).

## Projects

- [demo1-fastapi-ollama-chat](demo1-fastapi-ollama-chat/README.md) — FastAPI app that asks
  questions to a local Ollama model.

## Adding a new project

Create a new folder named `demoN-<short-description>` (e.g. `demo2-rag-chatbot`) with its
own dependencies and README, following the pattern of demo1.
