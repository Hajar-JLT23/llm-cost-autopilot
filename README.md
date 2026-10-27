# LLM Cost Autopilot

### Local LLM Routing, Inference Performance Monitoring & Hypothetical API Cost Simulation

**LLM Cost Autopilot** is a personal, educational AI engineering project developed in Python. It demonstrates how to route prompts automatically between locally hosted Large Language Models (LLMs), monitor inference performance, and simulate hypothetical API costs.

The project integrates **Ollama, FastAPI, Gradio, SQLite, and Python** into a modular application that can be run entirely on a local computer.

**No paid AI API, API key, subscription, or credit card is required.**

> **Important:** This is a personal portfolio and learning project. All monetary estimates are based on fictional example prices. They are not actual API charges, verified provider prices, or demonstrated financial savings.

---

## 1. Project Overview

Large Language Models have different capabilities, sizes, and computational requirements. A small model may be sufficient for a straightforward question, while a more demanding task may benefit from a larger model.

This project explores a simple idea:

**Can a local application automatically select a language model based on the estimated complexity of a prompt, while recording its inference performance?**

LLM Cost Autopilot implements a rule-based routing mechanism that classifies user prompts into three categories:

- **Simple:** Short questions or basic requests.
- **Medium:** Explanations, comparisons, summaries, and moderately detailed tasks.
- **Complex:** Software architecture, security, debugging, optimization, and more demanding tasks.

Each category is associated with a local language model.

The application then generates a response, collects performance metrics, calculates a hypothetical token-based cost, and stores the results in SQLite.

### Project Objectives

The main objectives are to:

1. Understand local LLM inference with Ollama.
2. Implement automatic model selection using Python.
3. Design reusable and modular backend components.
4. Collect inference latency and token usage metrics.
5. Explore hypothetical token-based API pricing calculations.
6. Build a REST API using FastAPI.
7. Develop an interactive interface using Gradio.
8. Store and retrieve inference history with SQLite.
9. Apply basic automated testing practices.

---

## 2. Main Features

### Automatic Model Routing

The application analyzes a user's prompt and selects a model based on predefined rules.

| Prompt Complexity | Selected Model | Example |
|---|---|---|
| Simple | `gemma3:1b` | "What is Python?" |
| Medium | `phi3:mini` | "Explain the difference between REST and GraphQL" |
| Complex | `llama3.2:3b` | "Design a secure and scalable REST API architecture" |

The routing mechanism uses keyword detection and prompt length.

**This is a heuristic classifier, not a trained machine learning model.**

The complexity categories are approximate and do not guarantee that the selected model is the most accurate or efficient for every request.

### Local LLM Inference

The application uses Ollama to run language models locally.

This approach provides several advantages for experimentation:

- No paid inference API is required.
- No external API key is needed.
- Models can run without sending prompts to a paid cloud LLM service.
- Developers can experiment with different local models.

Performance depends on the computer's hardware and the size of the selected model.

### Performance Monitoring

For each inference request, the application records:

| Metric | Description |
|---|---|
| Latency | Total time required to process the inference request |
| Input Tokens | Number of tokens processed in the input prompt |
| Output Tokens | Number of tokens generated in the response |
| Tokens per Second | Approximate output generation throughput |
| Hypothetical API Cost | Fictional token-based monetary estimate |

Latency and token measurements are obtained from the local Ollama execution.

### Hypothetical API Cost Simulation

The application uses configurable fictional token prices to demonstrate how token-based pricing calculations work.

These calculations are intended exclusively for educational purposes.

They do not represent real API expenses, market pricing, or proven financial savings.

### SQLite Inference History

Each completed inference is saved in a local SQLite database.

The history includes the prompt, selected model, complexity category, generated response, timestamp, performance metrics, and hypothetical cost.

This makes it possible to inspect previous requests and compare recorded measurements.

### REST API

FastAPI provides endpoints for model routing, response generation, health checks, and inference history.

The API also provides interactive documentation through Swagger UI.

### Gradio Web Interface

The Gradio interface allows users to:

- Enter a prompt.
- Generate a response using the selected local model.
- View the chosen model and complexity category.
- Inspect latency, token counts, and generation speed.
- View the fictional cost estimate.
- Consult previously recorded inference results.

---

## 3. Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Programming language | Python | Application development |
| Local model runtime | Ollama | Execute LLMs locally |
| Language models | Gemma 3 1B, Phi-3 Mini, Llama 3.2 3B | Generate responses |
| API framework | FastAPI | Provide REST endpoints |
| ASGI server | Uvicorn | Run the FastAPI application |
| Web interface | Gradio | Interactive user interface |
| Database | SQLite | Store inference history |
| Data processing | pandas | Display structured history data |
| Automated testing | pytest | Verify routing and metric calculations |
| Version control | Git | Track source code changes |
| Repository hosting | GitHub | Share project documentation and code |

---

## 4. System Architecture

The project follows a modular architecture in which each component has a specific responsibility.

```text
                        USER
                          |
                          v
               +---------------------+
               |  Gradio / CLI / API |
               +---------------------+
                          |
                          v
               +---------------------+
               |      service.py     |
               |  Request Processing |
               +---------------------+
                          |
                          v
               +---------------------+
               |      router.py      |
               | Prompt Classification|
               +---------------------+
                          |
               +----------+----------+
               |          |          |
               v          v          v
             SIMPLE     MEDIUM     COMPLEX
               |          |          |
               v          v          v
            Gemma 3     Phi-3      Llama 3.2
              1B        Mini          3B
               |          |          |
               +----------+----------+
                          |
                          v
               +---------------------+
               |    llm_client.py    |
               |   Ollama Inference  |
               +---------------------+
                          |
                          v
               +---------------------+
               |     metrics.py      |
               | Performance Metrics |
               |  Fictional Pricing  |
               +---------------------+
                          |
                          v
               +---------------------+
               |     database.py     |
               |    SQLite Storage   |
               +---------------------+
                          |
                          v
                  RESPONSE + METRICS
```

### How a Request Is Processed

1. The user submits a prompt through Gradio, the CLI, or the REST API.
2. The service layer receives the prompt.
3. The router estimates the prompt's complexity.
4. The application selects the model assigned to that complexity level.
5. Ollama executes the selected model locally.
6. The metrics module processes the inference measurements.
7. A fictional monetary estimate is calculated.
8. The inference result is saved in SQLite.
9. The application returns the generated response and metrics.

The Gradio interface and FastAPI endpoints reuse the same Python service layer. The Gradio interface does not need to make HTTP requests to the FastAPI server.

---

## 5. Project Structure

```text
llm-cost-autopilot/
|
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- router.py
|   |-- llm_client.py
|   |-- metrics.py
|   |-- database.py
|   |-- service.py
|
|-- tests/
|   |-- test_router.py
|   |-- test_metrics.py
|
|-- main.py
|-- api.py
|-- gradio_app.py
|-- requirements.txt
|-- .gitignore
|-- README.md
```

### Explanation of Each File

**`app/config.py`**

Defines application settings, model assignments, the local Ollama host, and fictional example token prices.

**`app/router.py`**

Contains the prompt complexity classification rules and automatic model selection logic.

**`app/llm_client.py`**

Communicates with Ollama, submits prompts to the selected model, and retrieves responses and inference metadata.

**`app/metrics.py`**

Calculates latency, generation throughput, token counts, and hypothetical API costs.

**`app/database.py`**

Creates the SQLite database, saves inference results, and retrieves historical records.

**`app/service.py`**

Coordinates routing, inference, metrics calculation, and database persistence.

**`main.py`**

Provides a command-line interface for testing the application.

**`api.py`**

Exposes the application's functionality through FastAPI endpoints.

**`gradio_app.py`**

Implements the interactive web interface.

**`tests/`**

Contains automated tests for prompt routing and performance calculations.

**`requirements.txt`**

Lists the Python dependencies required to run the project.

**`.gitignore`**

Prevents temporary files, virtual environments, and local databases from being included in Git commits.

---

## 6. Installation Guide

This section explains how to install and run the application on a local computer.

### Step 1 — Install Python

Install Python 3.12 from:

https://www.python.org/downloads/

Python 3.12 is the version used during development. Other versions may work but have not been validated for this project.

Verify your installation:

```powershell
python --version
```

Expected example:

```text
Python 3.12.7
```

### Step 2 — Install Git

Download Git from:

https://git-scm.com/downloads

Verify the installation:

```powershell
git --version
```

### Step 3 — Install Ollama

Download and install Ollama:

https://ollama.com/download

Ollama is required to run the language models locally.

Verify the installation:

```powershell
ollama --version
```

### Step 4 — Clone the Repository

Open PowerShell or the VS Code terminal.

Run:

```powershell
git clone https://github.com/Hajar-JLT23/llm-cost-autopilot.git
cd llm-cost-autopilot
```



### Step 5 — Create a Python Virtual Environment

A virtual environment isolates the Python packages used by this project from other Python projects.

Create one:

```powershell
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Once activated, the terminal should display `(.venv)`.

### Step 6 — Install Python Dependencies

Run:

```powershell
python -m pip install -r requirements.txt
```

This installs the Python libraries required by the application.

### Step 7 — Download the Language Models

Run the following commands:

```powershell
ollama pull gemma3:1b
ollama pull phi3:mini
ollama pull llama3.2:3b
```

The models are downloaded to your computer.

Download times and storage requirements depend on your internet connection and available disk space.

Verify the available models:

```powershell
ollama list
```

### Step 8 — Start the Ollama Server

Run:

```powershell
ollama serve
```

Keep the server running while using the application.

If Ollama is already running in the background, starting another server may produce a port-in-use message. In that case, use the existing server.

**Optional CPU-only configuration on Windows**

If your GPU is unsupported or causes inference errors, you can try running Ollama in CPU-only mode.

First, close any existing Ollama server process. Then open PowerShell and run:

```powershell
$env:CUDA_VISIBLE_DEVICES="-1"
ollama serve
```

This is a troubleshooting option used during development, not a universal requirement.

### Step 9 — Run the Command-Line Application

Open a terminal in the project directory with the virtual environment activated.

Run:

```powershell
python main.py
```

Enter a prompt and inspect the selected model, generated response, and performance measurements.

### Step 10 — Run the REST API

Start FastAPI:

```powershell
python -m uvicorn api:app --reload
```

Open:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI documentation.

### Step 11 — Run the Gradio Web Interface

Open another terminal in the project directory.

Activate the virtual environment if necessary, then run:

```powershell
python gradio_app.py
```

Open:

http://127.0.0.1:7860

You can now enter prompts, generate responses, and inspect the inference metrics.

**Note:** The application runs locally. The Gradio and FastAPI servers do not need to be exposed publicly.

---

## 7. REST API Documentation

The FastAPI application provides the following endpoints.

| HTTP Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check API availability |
| POST | `/route` | Classify a prompt and select a model |
| POST | `/generate` | Run inference and record metrics |
| GET | `/history` | Retrieve saved inference history |

### Example: Model Routing

Endpoint:

```text
POST /route
```

Request body:

```json
{
  "prompt": "Explain the difference between Python lists and tuples"
}
```

The API returns a complexity category and the corresponding selected model.

### Example: Text Generation

Endpoint:

```text
POST /generate
```

Request body:

```json
{
  "prompt": "What is machine learning?"
}
```

The application generates a response through Ollama, calculates performance metrics, and stores the result.

### Example: Inference History

Endpoint:

```text
GET /history
```

Returns previously saved inference records from the local SQLite database.

**Privacy note:** Inference history can contain user prompts and model-generated responses. Avoid entering confidential information when demonstrating the application, and do not commit the local database to a public repository.

---

## 8. Understanding the Performance Metrics

### Latency

Latency measures the total duration of an inference request.

The application converts Ollama's duration measurement from nanoseconds to seconds:

```text
Latency (seconds) = Total Duration (nanoseconds) / 1,000,000,000
```

Lower latency means the request completed faster in that particular execution.

### Input Tokens

Input tokens represent the number of tokens processed by the model from the input request.

Token counts may vary across models because tokenization methods differ.

### Output Tokens

Output tokens represent the number of tokens generated by the model.

The application currently limits generation to a configured maximum number of predicted tokens, so some responses may be truncated.

### Tokens per Second

Generation throughput measures the approximate number of output tokens produced per second during the generation phase.

```text
Tokens per Second = Output Tokens / Generation Duration (seconds)
```

This metric can help compare local inference performance, but results depend on the hardware, model, prompt, and execution conditions.

---

## 9. Hypothetical API Cost Calculation

### Educational Simulation Only

The application uses fictional input and output token prices.

These values are defined in `app/config.py`.

They are not actual provider rates.

### Formula

```text
Hypothetical Cost =
    (Input Tokens / 1,000,000 × Fictional Input Price)
  + (Output Tokens / 1,000,000 × Fictional Output Price)
```

### Example

Suppose an inference request uses:

- 100 input tokens
- 200 output tokens
- Fictional input price: $0.10 per million tokens
- Fictional output price: $0.40 per million tokens

The hypothetical cost is:

```text
Input cost  = 100 / 1,000,000 × 0.10 = $0.000010

Output cost = 200 / 1,000,000 × 0.40 = $0.000080

Total hypothetical cost = $0.000090
```

**This is a mathematical example, not an actual charge.**

Local Ollama inference does not generate paid per-token API charges. The simulation also excludes electricity, hardware, maintenance, and infrastructure expenses.

No actual cost savings have been measured or validated.

---

## 10. Automated Testing

The project includes automated tests using `pytest`.

The tests verify:

- Simple prompt classification.
- Medium prompt classification.
- Complex prompt classification.
- Automatic model selection.
- Performance metric calculations.

Run the test suite:

```powershell
python -m pytest -v
```

These tests do not require a running Ollama server because they test routing rules and mathematical calculations rather than model inference.

They do not evaluate the quality, factual accuracy, or safety of generated responses.

---

## 11. Screenshots

Screenshots of the application can be added to this section.

Suggested screenshots:

- Gradio main interface.
- Generated response and inference metrics.
- SQLite inference history displayed in Gradio.
- FastAPI Swagger UI documentation.

Screenshots should use demonstration prompts and avoid exposing private information.

---

## 12. Limitations

This project is an educational prototype and has several limitations.

**Heuristic Routing**

Prompt classification relies on keywords and word counts rather than a trained model. It may misclassify ambiguous requests.

**No Formal Quality Benchmarking**

The application does not automatically score response correctness, relevance, or factual accuracy.

**No Verified Cost Optimization**

Monetary estimates are fictional. No actual financial savings have been measured.

**Hardware-Dependent Performance**

Latency and generation throughput vary according to CPU, GPU, RAM, model size, and system load.

**Limited Model Selection**

The current implementation uses three predefined local models.

**Local Development Focus**

The application is intended for local experimentation and demonstration, not for production deployment.

**Generation Length Limit**

Responses may be truncated when they reach the configured maximum output token count.

---

## 13. Future Improvements

Possible improvements include:

1. Replacing heuristic routing with a trained prompt complexity classifier.
2. Introducing quality-aware routing based on benchmark results.
3. Comparing model performance on a standardized evaluation dataset.
4. Adding configurable routing policies for latency and quality.
5. Visualizing performance trends across inference requests.
6. Expanding automated test coverage.
7. Adding Docker support.
8. Improving model failure handling and configuration management.

These are potential future enhancements and are not currently implemented.

---

## 14. Learning Outcomes

This project provides practical experience with:

- Python application development.
- Local Large Language Model integration.
- LLM routing and orchestration.
- Inference performance monitoring.
- REST API development.
- Interactive AI application interfaces.
- SQLite database operations.
- Automated software testing.
- Modular software architecture.
- Technical documentation and Git version control.

---

## 15. Project Status

**Status: Educational prototype**

The project includes a local inference pipeline, heuristic model routing, performance metrics, SQLite persistence, a REST API, a Gradio interface, and automated unit tests.

It is intended for learning, experimentation, and portfolio demonstration.

---

## 16. Disclaimer

**LLM Cost Autopilot is an independent personal educational project.**

All monetary figures are fictional simulations created to demonstrate token-based calculations. They must not be interpreted as real AI service prices, actual expenses, or validated financial savings.

The project is not affiliated with or endorsed by the developers of the language models or frameworks used.

It is not intended to provide commercial financial estimates or production-ready cost management services.