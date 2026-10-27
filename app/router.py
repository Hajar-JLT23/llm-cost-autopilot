from app.config import MODELS


COMPLEX_KEYWORDS = {
    "architecture",
    "design",
    "optimize",
    "optimization",
    "algorithm",
    "security",
    "scalability",
    "debug",
    "implement",
    "refactor",
}

MEDIUM_KEYWORDS = {
    "explain",
    "compare",
    "difference",
    "summarize",
    "describe",
    "analyze",
}


def classify_prompt(prompt: str) -> str:
    """Classify a prompt using simple heuristic rules."""

    words = set(prompt.lower().split())
    word_count = len(prompt.split())

    if words.intersection(COMPLEX_KEYWORDS) or word_count > 60:
        return "complex"

    if words.intersection(MEDIUM_KEYWORDS) or word_count > 15:
        return "medium"

    return "simple"


def select_model(prompt: str) -> dict:
    """Select a local LLM based on prompt complexity."""

    complexity = classify_prompt(prompt)

    return {
        "complexity": complexity,
        "model": MODELS[complexity],
    }