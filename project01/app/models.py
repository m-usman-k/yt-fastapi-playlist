from pydantic import BaseModel, Field

from enum import Enum
from typing import Optional
from datetime import datetime, timezone


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    complete = "complete"
    
    
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    
    
class TaskModel(BaseModel):
    id: int = Field(..., example=1)
    title: str  = Field(..., example="FastAPI Title")
    description: Optional[str] = Field(None, example="FastAPI Description")
    status: TaskStatus  = Field(default=TaskStatus.pending)
    priority: Priority  = Field(default=Priority.low)
    created_at: datetime = Field(..., default_factory=lambda: datetime.now(timezone.utc))