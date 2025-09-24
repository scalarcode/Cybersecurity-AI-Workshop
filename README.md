# 🔐 Cybersecurity AI Workshop: Automated Vulnerability Detection & Response

This repository contains a hands-on **Cybersecurity AI (CAI)** demo that runs in **Google Colab**.  
The workshop introduces participants to **multi-agent AI for security**:
- **Scanner Agent** → Collects raw vulnerabilities with Bandit & Semgrep  
- **Analyst Agent (AI)** → Uses an LLM to summarize & prioritize issues  
- **Responder Agent (AI)** → Generates remediation steps & ticket metadata  
- **Coordinator** → Orchestrates the workflow  
- **Streamlit UI** → A simple dashboard to trigger scans & review results  

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

👉 You will paste this token into the Colab cell that asks for **HF_TOKEN**.

---

### 2. Ngrok (for Streamlit UI sharing)
We use **ngrok** to expose the Streamlit app running inside Colab to the web.

1. Sign up at [ngrok](https://dashboard.ngrok.com/signup)  
2. Go to [Your Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)  
3. Copy the authtoken  

👉 You will paste this token into the Colab cell that asks for **NGROK_AUTH_TOKEN**.

---

## 🚀 Running the Workshop

1. **Install dependencies**  
   The notebook will run:  
   ```bash
   !pip install --quiet streamlit pyngrok huggingface_hub bandit semgrep
