from fastapi import FastAPI
from app.tasks import tasks_router


app = FastAPI(
    title="Tasks Management System",
    description="Simple tasks management system using FastAPI and JSON",
    version="1.0.0"
)


app.include_router(tasks_router)