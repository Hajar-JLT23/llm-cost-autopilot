# Configuration for LLM Cost Autopilot

APP_NAME = "LLM Cost Autopilot"

OLLAMA_HOST = "http://localhost:11434"

MODELS = {
    "simple": "gemma3:1b",
    "medium": "phi3:mini",
    "complex": "llama3.2:3b"
}
# Hypothetical API prices in USD per 1 million tokens.
# These prices are fictional examples used only for demonstration 
#They do not refelct actual and real market prices or actual ollama charges

SIMULATED_PRICES = {
    "gemma3:1b": {
        "input": 0.10,
        "output": 0.40
    },
    "phi3:mini": {
        "input": 0.20,
        "output": 0.80
    },
    "llama3.2:3b": {
        "input": 0.30,
        "output": 1.20
    }
}