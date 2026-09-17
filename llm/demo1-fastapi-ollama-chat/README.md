# LLM Chat API (FastAPI + Ollama)

A minimal FastAPI app that forwards a question to a local Ollama server and returns the answer.

## 1. Start Ollama in Docker

```powershell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama pull llama3
```

Ollama running locally does **not** require an API key — it's a plain HTTP server on
`http://localhost:11434`. Leave `OLLAMA_API_KEY` empty in `.env` unless you put Ollama
behind an authenticated proxy/gateway (in that case, paste that key there).

## 2. Configure

```powershell
copy .env.example .env
```

Edit `.env` if your model name or Ollama URL differs.

## 3. Install & run

```powershell
pip install -r requirements.txt
uvicorn main:app --reload
```

## 4. Try it

Open http://localhost:8000/docs, or:

```powershell
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d "{\"question\": \"What is the capital of France?\"}"
```
