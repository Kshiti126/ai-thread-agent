from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
TAVILY_API_KEY = "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"


def call_ollama(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            },
            timeout=10   # 🔥 very important (prevents hanging)
        )
        return response.json()["response"]
    except:
        return "Quick generated thread about " + prompt[:30]


def planner_agent(topic):
    return call_ollama(f"Give 3 points about {topic}")


def research_agent(topic):
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": topic,
                "max_results": 1
            },
            timeout=5
        )
        data = response.json()
        return data.get("results", [{}])[0].get("content", "")
    except:
        return ""


def writer_agent(plan, research):
    return call_ollama(f"Write 3 short tweets:\n{plan}\n{research}")


@app.get("/generate")
def generate(topic: str):
    plan = planner_agent(topic)
    research = research_agent(topic)
    thread = writer_agent(plan, research)

    return {"thread": thread}


@app.get("/")
def home():
    return {"message": "API running"}
