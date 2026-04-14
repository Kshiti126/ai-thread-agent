from fastapi import FastAPI
import requests
import os

app = FastAPI()

TAVILY_API_KEY = "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"


def call_ollama(prompt):
    return "Generated Twitter thread about: " + prompt[:60]


def planner_agent(topic):
    return call_ollama(f"Create a Twitter thread plan for: {topic}")


def research_agent(topic):
    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": topic,
                "max_results": 2
            },
            timeout=5
        )
        data = response.json()
        return " ".join([r.get("content", "") for r in data.get("results", [])])
    except:
        return ""


def writer_agent(plan, research):
    return call_ollama(f"Write 3 tweets:\n{plan}\n{research}")


@app.get("/generate")
def generate(topic: str):
    plan = planner_agent(topic)
    research = research_agent(topic)
    thread = writer_agent(plan, research)

    return {"thread": thread}


@app.get("/")
def home():
    return {"message": "AI Thread Generator is running 🚀"}


# 🚀 IMPORTANT: dynamic port for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
