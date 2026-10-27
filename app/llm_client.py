from ollama import Client
from app.config import OLLAMA_HOST


client = Client(host=OLLAMA_HOST)


def generate_response(prompt: str, model: str) -> dict:
    """Generate a response using a local Ollama model."""

    response = client.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 150
        }
    )

    return {
        "model": model,
        "response": response.message.content,
        "total_duration": response.total_duration,
        "input_tokens": response.prompt_eval_count,
        "output_tokens": response.eval_count,
        "eval_duration": response.eval_duration
    }