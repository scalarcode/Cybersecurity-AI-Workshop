# 🔐 Cybersecurity AI Workshop (Local Version)

This repository contains a **Cybersecurity AI (CAI) demo** that runs locally on your machine (instead of Google Colab).  
It introduces participants to **multi-agent AI for security**:

- **Scanner Agent** → Collects vulnerabilities with Bandit & Semgrep  
- **Analyst Agent (AI)** → Uses an LLM (via Hugging Face) to summarize & prioritize issues  
- **Responder Agent (AI)** → Generates remediation steps & ticket metadata  
- **Coordinator** → Orchestrates the workflow  
- **Streamlit UI** → A simple dashboard to trigger scans & review results  

---

## 🛠️ Local Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cybersecurity-ai-workshop.git
cd cybersecurity-ai-workshop
```

### 2. Create Python Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Required API Keys

### 1. Hugging Face Inference API
We use Hugging Face models (Zephyr-7B) for **Analyst** and **Responder agents**.

1. Sign up at [Hugging Face](https://huggingface.co/join)  
2. Go to [Settings → Access Tokens](https://huggingface.co/settings/tokens)  
3. Create a new token:  
   - **Role**: `Read`  
   - Copy the token (looks like `hf_abc123XYZ...`)  

👉 Save this token in your environment:  
```bash
export HF_TOKEN="your_token_here"
```

On Windows (PowerShell):  
```powershell
setx HF_TOKEN "your_token_here"
```

### 2. Ngrok (for Streamlit UI sharing)
We use **ngrok** to expose the Streamlit app.

1. Sign up at [ngrok](https://dashboard.ngrok.com/signup)  
2. Go to [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)  
3. Copy the authtoken  

👉 Save this token in your environment:  
```bash
export NGROK_AUTH_TOKEN="your_token_here"
```

On Windows (PowerShell):  
```powershell
setx NGROK_AUTH_TOKEN "your_token_here"
```

---

## 🚀 Running the Workshop Locally

1. Create a vulnerable sample app (auto-generated inside the script).  
2. Start the Streamlit app:
```bash
streamlit run main.py --server.port 10000
```

3. The app will:  
   - Run Bandit & Semgrep scanners  
   - Send results to Hugging Face LLMs  
   - Generate remediation plans  
   - Expose UI via ngrok  

4. Copy the **ngrok public URL** from the terminal (looks like `https://xxxx.ngrok-free.app`) and open it in your browser.

---

## 🧩 Architecture (CAI Workflow)

```text
┌───────────────┐
│ Sample App    │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│ Scanner Agent │  (Bandit, Semgrep)
└──────┬────────┘
       │ Findings (JSON)
       ▼
┌───────────────┐
│ Analyst Agent │  (LLM → Summarize/Prioritize)
└──────┬────────┘
       │ Analysis
       ▼
┌───────────────┐
│ Responder     │  (LLM → Remediation/Tickets)
└──────┬────────┘
       │ Plan
       ▼
┌───────────────┐
│ Streamlit UI  │
└───────────────┘
```

---

## 📌 Notes
- Designed for **educational/demo purposes only** (not production).  
- Works with Hugging Face free-tier models (may be rate-limited).  
- Vulnerable code is intentionally insecure for learning.  
