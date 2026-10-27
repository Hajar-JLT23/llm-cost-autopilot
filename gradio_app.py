
import gradio as gr
import pandas as pd

from app.service import process_prompt
from app.database import init_database, get_inference_history


def run_inference(prompt):
    """Execute the LLM pipeline and return UI results."""

    if not prompt.strip():
        raise gr.Error("Please enter a prompt.")

    try:
        result = process_prompt(prompt)
    except Exception:
        raise gr.Error(
            "Inference failed. Check that Ollama is running."
        )

    metrics = result["metrics"]

    return (
        result["response"],
        result["model"],
        result["complexity"],
        metrics["latency_seconds"],
        metrics["tokens_per_second"],
        metrics["input_tokens"],
        metrics["output_tokens"],
        f"${metrics['simulated_cost_usd']:.8f}",
        load_history()
    )


def load_history():
    """Load inference history from SQLite."""

    records = get_inference_history()

    columns = [
        "timestamp",
        "model",
        "complexity",
        "latency_seconds",
        "input_tokens",
        "output_tokens",
        "simulated_cost_usd"
    ]

    return pd.DataFrame(records, columns=columns)


# Initialize database before launching the interface
init_database()


with gr.Blocks(title="LLM Cost Autopilot") as demo:

    gr.Markdown(
        "# LLM Cost Autopilot\n"
        "### Local AI Model Routing & Performance Monitoring\n"
        "Route prompts across local LLMs, measure inference "
        "performance, and estimate hypothetical API costs."
    )

    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(
                label="Enter your prompt",
                placeholder="Ask a question...",
                lines=5
            )

            generate_button = gr.Button(
                "Generate Response",
                variant="primary"
            )

        with gr.Column():
            response_output = gr.Textbox(
                label="Generated Response",
                lines=10,
                interactive=False
            )

    gr.Markdown("## Model Selection")

    with gr.Row():
        model_output = gr.Textbox(
            label="Selected Model"
        )

        complexity_output = gr.Textbox(
            label="Prompt Complexity"
        )

    gr.Markdown("## Performance Metrics")

    with gr.Row():
        latency_output = gr.Number(
            label="Latency (seconds)"
        )

        speed_output = gr.Number(
            label="Generation Speed (tokens/s)"
        )

    with gr.Row():
        input_tokens_output = gr.Number(
            label="Input Tokens"
        )

        output_tokens_output = gr.Number(
            label="Output Tokens"
        )

        cost_output = gr.Textbox(
            label="Hypothetical API Cost (USD) — Example Only"
        )

    
    gr.Markdown(
        """
        ### Important Disclaimer — Educational Project

        **LLM Cost Autopilot is a personal, educational portfolio project.**

        All monetary amounts displayed in this application are
        **hypothetical simulations based on fictional token prices**.

        - **Not real costs:** The displayed amounts do not represent
          actual API charges, invoices, or payments.
        - **Not real market prices:** The example prices are invented
          for educational purposes and are not verified provider rates.
        - **Local inference:** Models run locally through Ollama,
          without paid per-token API calls.
        - **No verified savings:** The project does not demonstrate
          actual financial savings or proven cost optimization.
        - **Real performance measurements:** Latency, token counts,
          and generation speed come from local Ollama executions.
        - **Excluded expenses:** Electricity and hardware costs
          are not included in the simulation.

        **Project purpose:** Demonstrate LLM routing, local inference,
        performance monitoring, and hypothetical cost calculations.

        This is not a commercial product or a production-ready
        financial cost management service.
        """
    )


    gr.Markdown("## Inference History")

    history_table = gr.Dataframe(
        value=load_history(),
        label="Recent Inferences",
        interactive=False
    )

    refresh_button = gr.Button("Refresh History")

    generate_button.click(
        fn=run_inference,
        inputs=prompt_input,
        outputs=[
            response_output,
            model_output,
            complexity_output,
            latency_output,
            speed_output,
            input_tokens_output,
            output_tokens_output,
            cost_output,
            history_table
        ]
    )

    refresh_button.click(
        fn=load_history,
        outputs=history_table
    )


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False
    )

