from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="CRUD App", version="1.0", description="A simple CRUD Task API")



tasks = [
    {"id": 1, "title": "throw out the trash", "done": False},
    {"id": 2, "title": "visit the supermarket", "done": False},
    {"id": 3, "title": "feed the dogs", "done": False}
]


@app.get("/tester")
def home():
    return f"Hello There! Welcome to My Task Homepage"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def describe_api():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/tasks")
def check_task():
    return tasks


@app.get("/tasks/{id}")
def check_task_state(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
        else:
            raise HTTPException(status_code=404, detail={"error": "Task 99 not found"}) 

              

