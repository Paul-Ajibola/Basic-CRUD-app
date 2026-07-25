from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="CRUD App", version="1.0", description="A simple CRUD Task API")


class RequestBody(BaseModel):
    title: str= Field(..., min_length=1)


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


             
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def new_order(payload: RequestBody):

    if not payload.title.strip():
        raise HTTPException(
            status_code=400,
            detail={"error": "Title cannot be empty"}
        )
    
    new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "title": payload.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


@app.put("/tasks/{id}")
def update_task(title: str, id: int):

    for task in tasks:
        if task["id"] == id:

            if not title.strip():
                raise HTTPException(
                    status_code=400,
                    detail="Title cannot be empty"
                )

            task["title"] = title
            task["done"] = True

            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found!"
    )


@app.delete("/tasks/{id}")
def delete_task(id: int):

    for task in tasks:
        if task["id"] == id:

            tasks.remove(task)

            return f"Task successfully removed!"

    raise HTTPException(
        status_code=404,
        detail="Unknown Task"
    )


           
        

        

