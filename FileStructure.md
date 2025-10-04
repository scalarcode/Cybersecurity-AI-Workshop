# Project: Cybersecurity AI Workshop — Folder Structure

This repository contains a compact demo for a **multi-agent Cybersecurity AI (CAI)** workflow: scanners (Bandit & Semgrep), LLM-powered analyst/responder agents, a Streamlit UI, and automated PDF report generation.

## Folder structure

```bash
/content/
│
├── main.py # Core logic: scanner + analyst + responder agents, coordinator, and PDF generation
├── app.py # Streamlit UI: interactive web front-end to run the pipeline and download the report
├── sample_app/
│ └── vulnerable.py # Intentionally vulnerable sample application used for scanning (for training/demo only)
└── requirements.txt # Python dependencies for the project (use pip install -r requirements.txt)
```
## File descriptions

- **main.py**  
  - Implements the multi-agent orchestration:
    - `scanner_agent` (runs Bandit & Semgrep on `sample_app/`)
    - `analyst_agent` (calls an LLM via Hugging Face to summarize & prioritize findings)
    - `responder_agent` (calls the LLM to generate remediation steps and ticket metadata)
    - `coordinator()` (runs the pipeline and returns all outputs)
    - `generate_pdf_report(...)` (creates a downloadable PDF summarizing findings, analysis, and recommendations)
  - Intended for both local and Colab usage (reads API tokens from environment variables when run locally).

- **app.py**  
  - Streamlit-powered UI:
    - One-click button to run the multi-agent scan (`coordinator()`).
    - Displays raw scanner output, AI analysis, and remediation suggestions.
    - Generates and provides a downloadable PDF report for sharing with ticketing or dev teams.

- **sample_app/vulnerable.py**  
  - A purposely insecure Python script (e.g., hardcoded secrets, command injection patterns) used to produce demonstrable Bandit & Semgrep findings in the workshop.
  - **Important:** This file is intentionally insecure — do **not** run against production systems or expose real secrets.

- **requirements.txt**  
  - List of required Python packages. Example contents:
    ```
    streamlit
    pyngrok
    huggingface_hub
    bandit
    semgrep
    reportlab
    ```
  - Install with:
    ```bash
    pip install -r requirements.txt
    ```

## Quickstart (local)

1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\Scripts\activate       # Windows (PowerShell)
