# main.py
# =============================================================
# 🔐 Cybersecurity AI Workshop: Automated Vulnerability Detection & Response
#
# This script demonstrates a multi-agent AI system for cybersecurity.
# It runs vulnerability scans (Bandit + Semgrep), uses an LLM (via Hugging Face)
# to analyze and summarize vulnerabilities, and generates remediation steps.
#
# A Streamlit UI is provided to run the workflow interactively.
# =============================================================

import os
import subprocess
import json
import streamlit as st
from huggingface_hub import InferenceClient

# =============================================================
# 🔑 Environment Setup
# =============================================================
# Read tokens from environment variables.
# Make sure to set them before running:
#   export HF_TOKEN="your_huggingface_token"
#   (Optional) export NGROK_AUTH_TOKEN="your_ngrok_token"

HF_TOKEN = os.getenv("HF_TOKEN")
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

if not HF_TOKEN:
    raise ValueError("❌ Missing Hugging Face API token. Set HF_TOKEN as an environment variable.")

# Hugging Face model (Zephyr-7B used here)
MODEL = "HuggingFaceH4/zephyr-7b-beta"
client = InferenceClient(model=MODEL, token=HF_TOKEN)

# =============================================================
# 🐍 Sample Vulnerable Application
# =============================================================
# For demo purposes, we generate a Python file with known vulnerabilities:
# - Hardcoded secrets
# - Command injection
# This ensures Bandit and Semgrep always produce findings.

os.makedirs("sample_app", exist_ok=True)
vuln_code = """
import os

def insecure_code(user_input):
    # Command injection vulnerability
    os.system("echo " + user_input)

# Hardcoded secret (Bad Practice)
API_KEY = "12345-SECRET"

print("Hello World")
"""
with open("sample_app/vulnerable.py", "w") as f:
    f.write(vuln_code)

# =============================================================
# 🤖 Agents
# =============================================================

def scanner_agent():
    """Run Bandit + Semgrep on vulnerable.py and return JSON findings."""
    bandit_out = subprocess.getoutput("bandit -r sample_app -f json")
    semgrep_out = subprocess.getoutput("semgrep --config p/ci sample_app --json")

    bandit = json.loads(bandit_out) if bandit_out else {}
    semgrep = json.loads(semgrep_out) if semgrep_out else {}
    return bandit, semgrep


def analyst_agent(bandit, semgrep):
    """Use LLM to analyze raw findings from Bandit and Semgrep."""
    prompt = f"""
    You are a security analyst.
    Summarize, prioritize, and explain vulnerabilities found by Bandit and Semgrep:

    Bandit Findings: {json.dumps(bandit, indent=2)}
    Semgrep Findings: {json.dumps(semgrep, indent=2)}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )
    return response.choices[0].message["content"]


def responder_agent(analysis):
    """Use LLM to propose remediation steps for developers."""
    prompt = f"""
    Based on this vulnerability analysis, propose remediation steps.
    Provide developer-friendly fixes and ticket metadata.

    Analysis: {analysis}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )
    return response.choices[0].message["content"]


def coordinator():
    """Orchestrate the multi-agent workflow."""
    bandit, semgrep = scanner_agent()
    analysis = analyst_agent(bandit, semgrep)
    response = responder_agent(analysis)
    return bandit, semgrep, analysis, response

# =============================================================
# 🌐 Streamlit UI
# =============================================================
# A simple web app where users can run scans and review results.

def main():
    st.title("🔐 Cybersecurity AI Workshop")
    st.write("Multi-Agent AI for Automated Vulnerability Detection & Response")

    if st.button("Run Multi-Agent Scan"):
        with st.spinner("Running security scan..."):
            bandit, semgrep, analysis, response = coordinator()

        st.subheader("📋 Raw Findings (Bandit)")
        st.json(bandit)

        st.subheader("📋 Raw Findings (Semgrep)")
        st.json(semgrep)

        st.subheader("🧠 Analyst Agent (AI Summary)")
        st.write(analysis)

        st.subheader("🛠️ Responder Agent (AI Remediation)")
        st.write(response)


if __name__ == "__main__":
    main()
