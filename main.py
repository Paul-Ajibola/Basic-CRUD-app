from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="CRUD App", version="1.0", description="A simple CRUD Task API")


@app.get("/tester")
def home():
    return f"Hello There! Welcome to My Task Homepage"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def describe_api():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

