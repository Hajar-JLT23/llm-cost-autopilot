
from app.metrics import calculate_metrics


def test_metrics_calculation():
    """Check latency, throughput, and simulated API cost."""

    result = {
        "model": "gemma3:1b",
        "total_duration": 5_000_000_000,
        "eval_duration": 4_000_000_000,
        "input_tokens": 100,
        "output_tokens": 40
    }

    metrics = calculate_metrics(result)

    assert metrics["latency_seconds"] == 5.0
    assert metrics["tokens_per_second"] == 10.0
    assert metrics["input_tokens"] == 100
    assert metrics["output_tokens"] == 40
    assert metrics["simulated_cost_usd"] == 0.000026
