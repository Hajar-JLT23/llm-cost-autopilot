
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.config import APP_NAME
from app.router import select_model
from app.service import process_prompt
from app.database import init_database, get_inference_history


app = FastAPI(
    title=APP_NAME,
    description="Local LLM routing and performance monitoring API.",
    version="1.0.0"
)


class PromptRequest(BaseModel):
    prompt: str = Field(min_length=1)


init_database()


@app.get("/health")
def health_check():
    """Check whether the API server is running."""
    return {
        "status": "ok",
        "application": APP_NAME
    }


@app.post("/route")
def route_prompt(request: PromptRequest):
    """Select a local LLM based on prompt complexity."""
    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt cannot be empty."
        )

    return select_model(request.prompt)


@app.post("/generate")
def generate(request: PromptRequest):
    """Generate a response using the selected local LLM."""
    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Prompt cannot be empty."
        )

    try:
        return process_prompt(request.prompt)
    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail="Local LLM inference is currently unavailable."
        ) from error


@app.get("/history")
def get_history():
    """Retrieve previous LLM inference results."""
    return get_inference_history()
