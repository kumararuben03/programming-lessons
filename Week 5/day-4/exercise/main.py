from fastapi import FastAPI, Depends, Path, HTTPException
import models
from models import Todos
from databases import engine, SessionLocal
from typing import Annotated, Optional
from pydantic import BaseModel, StrictInt, Field
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    task_id: Optional[StrictInt] = None
    date: str = Field(min_length=3)
    user: str=Field(min_length=3)
    task: str=Field(min_length=3)
    priority: StrictInt = Field(gt=0, lt=6)

@app.get("/todos")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todos/{task_id}")
async def get_task_by_id(db: db_dependency, task_id:int = Path(gt=0)):
    todo_result = db.query(Todos).filter(Todos.task_id == task_id).first()

    if todo_result is not None:
        return todo_result
    
    raise HTTPException(status_code=404, details="Task not found")

@app.post("/todos")
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo = Todos(**todo_request.model_dump())
    db.add(todo)
    db.commit()

@app.put("/todos/{task_id}")
async def update_todo(db: db_dependency,
                      task_id: int,
                      todo_request: TodoRequest):
    todo_result = db.query(Todos).filter(Todos.task_id == task_id).first()
    if todo_result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    todo_result.date = todo_request.date
    todo_result.user = todo_request.user
    todo_result.task = todo_request.task
    todo_result.priority = todo_request.priority

    db.add(todo_result)
    db.commit()

@app.delete("/todos/{task_id}")
async def delete_todo(db: db_dependency, task_id: int=Path(gt=0)):
    todo_result = db.query(Todos).filter(Todos.task_id == task_id).first()

    if todo_result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        db.query(Todos).filter(Todos.task_id == task_id).delete()

    db.commit()