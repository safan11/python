import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from config import settings

app = FastAPI(title="LLM Chat API", description="Ask a question, get an answer from an Ollama-hosted LLM")


class AskRequest(BaseModel):
    question: str
    model: str | None = None


class AskResponse(BaseModel):
    answer: str
    model: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    model = request.model or settings.ollama_model

    headers = {}
    if settings.ollama_api_key:
        headers["Authorization"] = f"Bearer {settings.ollama_api_key}"

    payload = {
        "model": model,
        "prompt": request.question,
        "stream": False,
    }

    url = f"{settings.ollama_base_url}/api/generate"

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
    except httpx.ConnectError:
        raise HTTPException(status_code=502, detail=f"Could not connect to Ollama at {settings.ollama_base_url}. Is the container running?")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)

    data = response.json()
    return AskResponse(answer=data.get("response", ""), model=model)
