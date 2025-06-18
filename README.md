# 🧠 AgentVerse

AgentVerse is a modular AI agent framework designed for rapid development and deployment of autonomous LLM-based agents. From scraping and summarizing to email automation, plug your tools, pick your agent, and automate workflows.

---

## 🚀 Features

- 🧩 Modular agent architecture
- 📡 FastAPI backend API
- 🔧 Built-in tools (search, summarize, email, etc.)
- 🧠 GPT-4/3.5 + Langchain support
- 🗂️ Easy to extend with your own agents/tools

---

## 📂 Folder Structure

- `agents/` - Custom agents (e.g., EmailAgent, ScraperAgent)
- `tools/` - Reusable tools for agents
- `api/` - FastAPI routes
- `core/` - Configs and agent manager
- `main.py` - App entrypoint
- `.env.example` - Template for environment variables

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/AgentVerse.git
cd AgentVerse
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --reload
