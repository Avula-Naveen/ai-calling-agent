# placeholder for FastAPI entrypoint
from fastapi import FastAPI

app = FastAPI(title="AI Calling Agent")

@app.get("/health")
def health():
    return {"status": "ok"}
