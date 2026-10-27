
from app.router import select_model
from app.llm_client import generate_response
from app.metrics import calculate_metrics
from app.database import init_database, save_inference


def process_prompt(prompt: str) -> dict:
    """Run the complete LLM inference pipeline."""

    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    
    init_database()

    
    routing = select_model(prompt)

    
    result = generate_response(
        prompt=prompt,
        model=routing["model"]
    )

    
    metrics = calculate_metrics(result)

    # Save the inference to SQLite
    save_inference(
        prompt=prompt,
        routing=routing,
        result=result,
        metrics=metrics
    )

    # Return the complete inference result
    return {
        "prompt": prompt,
        "complexity": routing["complexity"],
        "model": routing["model"],
        "response": result["response"],
        "metrics": metrics
    }
