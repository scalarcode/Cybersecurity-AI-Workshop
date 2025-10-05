# 🔐 Cybersecurity AI Workshop: Automated Vulnerability Detection & Response

This repository contains a hands-on **Cybersecurity AI (CAI)** demo that runs in **Google Colab**.  
The workshop introduces participants to **multi-agent AI for security**:

- **Scanner Agent** → Collects raw vulnerabilities with Bandit & Semgrep  
- **Analyst Agent (AI)** → Uses an LLM to summarize & prioritize issues  
- **Responder Agent (AI)** → Generates remediation steps & ticket metadata  
- **Coordinator** → Orchestrates the workflow  
- **Streamlit UI** → A simple dashboard to trigger scans & review results  

---

## ⚡ Quickstart (3 Steps)

1. **Open in Colab**  
   Upload and open `final_multiagent_workshop.ipynb` in [Google Colab](https://colab.research.google.com/).  

2. **Paste API Keys**  
   - Get a free **Hugging Face token** → [link](https://huggingface.co/settings/tokens)  
   - Get a free **ngrok token** → [link](https://dashboard.ngrok.com/get-started/your-authtoken)  
   Paste both in the notebook cells when prompted.  

3. **Launch Streamlit UI**  
   Run all cells → copy the **public ngrok URL** → open in your browser → click **Run Multi-Agent Scan**.  

That’s it 🎉! You’ll see raw findings, AI summaries, and automated remediation steps.  

---

## 🛠️ Environment Setup (Google Colab)

This workshop is designed to be run entirely in **Google Colab**.  
No local installation is needed.

1. Open [Google Colab](https://colab.research.google.com/)  
2. Upload the provided notebook (`final_multiagent_workshop.ipynb`)  
3. Run each cell in order (Shift + Enter)  

---

## 🔑 Required API Keys

### 1. Hugging Face Inference API
We use Hugging Face models (Zephyr-7B) for **Analyst** and **Responder agents**.

1. Sign up at [Hugging Face](https://huggingface.co/join)  
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)  
3. Create a new token:  
   - **Role**: `Read`  
   - Copy the token (looks like `hf_abc123XYZ...`)  

👉 Paste this token into the Colab cell that asks for **`HF_TOKEN`**.

---

### 2. Ngrok (for Streamlit UI sharing)
We use **ngrok** to expose the Streamlit app running inside Colab to the web.

1. Sign up at [ngrok](https://dashboard.ngrok.com/signup)  
2. Go to [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)  
3. Copy the authtoken  

👉 Paste this token into the Colab cell that asks for **`NGROK_AUTH_TOKEN`**.

---

## 🚀 Running the Workshop

### 1. Install dependencies
The notebook will install all required packages:
```bash
!pip install --quiet streamlit pyngrok huggingface_hub bandit semgrep
```
### 2. Enter API keys

   - ##Paste your Hugging Face token (HF_TOKEN)
   - ##Paste your ngrok authtoken (NGROK_AUTH_TOKEN)

### 3. Create vulnerable app
   The notebook generates a sample_app/vulnerable.py file with insecure code (hardcoded secrets, command injection).
   This ensures Bandit & Semgrep always produce findings.

### 4. Run the Streamlit UI
   The notebook launches:
   ```python
   streamlit run app.py --server.port 10000
   ```
   and opens an ngrok tunnel. Copy the public URL printed in the notebook (e.g., https://xxxx.ngrok-free.app) and open it in your browser.

### 5. Run the scan
   Click “Run Multi-Agent Scan” In the Streamlit UI, 
   you’ll see:
   1. Raw Bandit + Semgrep findings
   2. Analyst Agent (AI) summary
   3. Responder Agent (AI) remediation plan
   
🧩 Architecture (CAI Workflow)
```bash
                ┌──────────────────────────────┐
                │  sample_app/vulnerable.py     │
                │  (Target codebase to scan)    │
                └──────────────┬───────────────┘
                               │
                               ▼
        ┌──────────────────────────────────────────────┐
        │          🔍 Scanner Agents                   │
        │----------------------------------------------│
        │ • Bandit  → Python static security analyzer  │
        │ • Semgrep → Pattern-based code analyzer      │
        └──────────────┬───────────────────────────────┘
                       │  (Raw JSON findings)
                       ▼
        ┌──────────────────────────────────────────────┐
        │          🧠 AI Analyst Agent                 │
        │----------------------------------------------│
        │ • Uses Hugging Face Zephyr-7B LLM            │
        │ • Summarizes vulnerabilities                 │
        │ • Prioritizes by severity                    │
        │ • Adds rationale & quick fixes               │
        └──────────────┬───────────────────────────────┘
                       │  (Structured analysis JSON)
                       ▼
        ┌──────────────────────────────────────────────┐
        │         💡 AI Recommendation Agent           │
        │----------------------------------------------│
        │ • Reads Analyst output                       │
        │ • Suggests concrete code fixes               │
        │ • Adds secure coding examples                │
        │ • Prioritizes remediation order              │
        │ • Generates ticket metadata (title, labels)  │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │           📄 PDF Report Generator            │
        │----------------------------------------------│
        │ • Combines scanner + AI outputs              │
        │ • Produces "CyberAI_Report.pdf"              │
        │ • Ready to attach to tickets / share         │
        └──────────────┬───────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────────────────────┐
        │            🌐 Streamlit UI (Colab)           │
        │----------------------------------------------│
        │ • Runs via ngrok for public sharing          │
        │ • Click "Run Multi-Agent Scan" to execute    │
        │ • View Bandit/Semgrep + AI insights          │
        └──────────────────────────────────────────────┘

```
### 📚 References

- Bandit (Python Security Linter) https://bandit.readthedocs.io/en/latest/
- Semgrep (Static Analysis) https://semgrep.dev/
- Hugging Face Inference API https://huggingface.co/docs/api-inference/index
- Ngrok https://ngrok.com/
