
from app.router import classify_prompt, select_model


def test_simple_prompt():
    """Check classification of a simple prompt."""
    assert classify_prompt("Hello") == "simple"


def test_medium_prompt():
    """Check classification of a medium prompt."""
    assert classify_prompt("Explain Python functions") == "medium"


def test_complex_prompt():
    """Check classification of a complex prompt."""
    assert classify_prompt("Design a secure API architecture") == "complex"


def test_model_selection():
    """Check automatic model selection."""
    result = select_model("Hello")

    assert result["complexity"] == "simple"
    assert result["model"] == "gemma3:1b"
