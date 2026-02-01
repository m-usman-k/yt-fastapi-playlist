from fastapi import APIRouter, HTTPException
from app.models import TaskModel, TaskStatus, Priority
from app.db_utils import read_json, write_json

FILENAME = "tasks.json"


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)



@tasks_router.get(path="/")
async def get_tasks(status, priority):
    tasks = read_json(FILENAME)
    
    tasks = [t for t in tasks if t["status"] == status]
    tasks = [t for t in tasks if t["priority"] == priority]

    return tasks
    


@tasks_router.get(path="/{task_id}")
async def get_task(task_id: int):
    tasks = read_json(FILENAME)
    
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task
    
    
@tasks_router.post(path="/")
async def add_task(task: TaskModel):
    tasks = read_json(FILENAME)
    
    if any(t["id"] == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="ID already exists")

    tasks.append(task.model_dump(mode="json"))
    write_json(FILENAME, tasks)
    return task
    
    
@tasks_router.put(path="/{task_id}")
async def put_task(task_id: int, task: TaskModel):
    tasks = read_json(FILENAME)
    
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i] = task.model_dump(mode="json")
            write_json(FILENAME, tasks)
            return tasks
        
    raise HTTPException(status_code=404, detail="Task not found")
    
    
@tasks_router.patch(path="/{task_id}")
async def patch_task(task_id: int, status: TaskStatus, priority: Priority):
    tasks = read_json(FILENAME)
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["status"] = status
    task["priority"] = priority
    
    
    write_json(FILENAME, tasks)
    return task


@tasks_router.delete(path="/{task_id}")
async def delete_task(task_id: int):
    tasks = read_json(FILENAME)
    
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            write_json(FILENAME, tasks)
            return tasks
        
    raise HTTPException(status_code=404, detail="Task not found")
    
    

@tasks_router.patch(path="/{task_id}/start")
async def start_task(task_id: int):
    tasks = read_json(FILENAME)
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["status"] = "in_progress"
    
    
    write_json(FILENAME, tasks)
    return task
    
    
@tasks_router.patch(path="/{task_id}/complete")
async def complete_task(task_id: int):
    tasks = read_json(FILENAME)
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["status"] = "complete"
    
    
    write_json(FILENAME, tasks)
    return task
    
    
@tasks_router.patch(path="/{task_id}/reopen")
async def reopen_task(task_id: int):
    tasks = read_json(FILENAME)
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task["status"] = "in_progress"
    
    
    write_json(FILENAME, tasks)
    return task
    
    
@tasks_router.delete(path="/cleanup/completed")
async def clear_completed_tasks():
    tasks = read_json(FILENAME)
    
    tasks = [t for t in tasks if t["status"] != "complete"]

    write_json(FILENAME, tasks)
    return tasks