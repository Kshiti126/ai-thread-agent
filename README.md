# 🤖 AI Twitter/X Thread Generator (Multi-Agent System)

This project is a deployable multi-agent AI system that automatically generates structured and engaging Twitter/X threads from a simple user input.

## 🚀 Features

- 🧠 Planner Agent – breaks topic into structured thread plan  
- 🔎 Research Agent – uses Tavily API for real-time information  
- ✍️ Writer Agent – generates thread content  
- 🧪 Evaluator (LLM-as-Judge) – assesses output quality  
- 🔁 Iterative improvement loop  
- 🌐 FastAPI backend with API endpoint  

## ⚙️ Tech Stack

- Python  
- FastAPI  
- Ollama (local LLM)  
- Tavily Search API  

## 🔗 API Usage

Run locally:

```bash
python -m uvicorn app:app --reload
http://127.0.0.1:8000/generate?topic=AI
