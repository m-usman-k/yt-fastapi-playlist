from pydantic import BaseModel, field_validator, model_validator

from fastapi import FastAPI



app = FastAPI()



class UserSchema(BaseModel):
    username: str
    password: str
    
    @field_validator("username", "password")
    def validate_username(cls, v):
        if len(v) < 5:
            raise ValueError("Username is very small")
        
        return v
    
    
class SecondUser(BaseModel):
    username: str
    password: str
    confirm_password: str
    
    
    @field_validator("password", "confirm_password")
    def validate_username(cls, v):
        if len(v) < 5:
            raise ValueError("Username is very small")
        
        return v
    
    @model_validator(mode="after")
    def validate_user(self):
        if self.password != self.confirm_password:
            raise ValueError("Dono passwords match hi nahi kar rahe")

        return self
    
    
    
@app.post("/")
async def home(user: SecondUser):
    return {"message": "working"}