import sqlite3
from pathlib import Path


# Database file location
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "llm_autopilot.db"


def init_database():
    """Create the database table if it does not exist."""

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS inference_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                prompt TEXT NOT NULL,
                complexity TEXT NOT NULL,
                model TEXT NOT NULL,
                response TEXT,
                latency_seconds REAL,
                input_tokens INTEGER,
                output_tokens INTEGER,
                tokens_per_second REAL,
                simulated_cost_usd REAL
            )
        """)


def save_inference(prompt, routing, result, metrics):
    """Save an LLM inference result to SQLite."""

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            INSERT INTO inference_logs (
                prompt,
                complexity,
                model,
                response,
                latency_seconds,
                input_tokens,
                output_tokens,
                tokens_per_second,
                simulated_cost_usd
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            prompt,
            routing["complexity"],
            routing["model"],
            result["response"],
            metrics["latency_seconds"],
            metrics["input_tokens"],
            metrics["output_tokens"],
            metrics["tokens_per_second"],
            metrics["simulated_cost_usd"]
        ))


def get_inference_history():
    """Retrieve saved inference results."""

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute("""
            SELECT *
            FROM inference_logs
            ORDER BY id DESC
        """).fetchall()

    return [dict(row) for row in rows]