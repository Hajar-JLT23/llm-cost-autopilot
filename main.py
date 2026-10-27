
from app.service import process_prompt
from app.database import get_inference_history


def main():
    print("=== LLM Cost Autopilot ===")

    prompt = input("\nEnter your prompt: ")

    if not prompt.strip():
        print("Error: Prompt cannot be empty.")
        return

    print("\nGenerating response...")

    result = process_prompt(prompt)

    print("\n=== Model Selection ===")
    print("Complexity:", result["complexity"])
    print("Selected model:", result["model"])

    print("\n=== AI Response ===")
    print(result["response"])

    metrics = result["metrics"]

    print("\n=== Performance Metrics ===")
    print("Latency:", metrics["latency_seconds"], "seconds")
    print("Generation speed:", metrics["tokens_per_second"], "tokens/s")
    print("Input tokens:", metrics["input_tokens"])
    print("Output tokens:", metrics["output_tokens"])
    print(f"Simulated API cost: ${metrics['simulated_cost_usd']:.8f}")

    print("\nInference saved successfully!")

    history = get_inference_history()

    print("\n=== Recent Inference History ===")

    for record in history[:5]:
        print(
            f"ID: {record['id']} | "
            f"Model: {record['model']} | "
            f"Latency: {record['latency_seconds']}s"
        )


if __name__ == "__main__":
    main()
