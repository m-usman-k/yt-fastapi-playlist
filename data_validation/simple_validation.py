from pydantic import BaseModel, Field, EmailStr, UUID1, HttpUrl, IPvAnyAddress
from typing import Optional

from fastapi import FastAPI


app = FastAPI()




class UserSchema(BaseModel):
    email: EmailStr
    
    
    class Config:
        extra = "forbid"
        json_schema_extra = {
            "example": {
                "testkey": "testvalue"
            }
        }
        validate_assignment = True
        
        
        
@app.post("/")
async def home(user: UserSchema):
    return {"message": "working"}