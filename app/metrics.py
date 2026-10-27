from app.config import SIMULATED_PRICES


def calculate_metrics(result: dict) -> dict:
    """Calculate inference performance and simulated API cost."""

    model = result["model"]

    total_duration_ns = result["total_duration"] or 0
    eval_duration_ns = result["eval_duration"] or 0

    input_tokens = result["input_tokens"] or 0
    output_tokens = result["output_tokens"] or 0

    # Convert nanoseconds to seconds
    latency_seconds = total_duration_ns / 1_000_000_000
    generation_seconds = eval_duration_ns / 1_000_000_000

    # Calculate output generation speed
    tokens_per_second = (
        output_tokens / generation_seconds
        if generation_seconds > 0
        else 0
    )

    # Calculate hypothetical API cost
    prices = SIMULATED_PRICES[model]

    input_cost = (
        input_tokens / 1_000_000
    ) * prices["input"]

    output_cost = (
        output_tokens / 1_000_000
    ) * prices["output"]

    total_cost = input_cost + output_cost

    return {
        "latency_seconds": round(latency_seconds, 2),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "tokens_per_second": round(tokens_per_second, 2),
        "simulated_cost_usd": round(total_cost, 8)
    }