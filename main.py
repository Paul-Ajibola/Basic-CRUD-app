from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="CRUD App", version="1.0", description="A simple CRUD Task API")


@app.get("/")
def home():
    return f"Welcome to My Task Homepage"

