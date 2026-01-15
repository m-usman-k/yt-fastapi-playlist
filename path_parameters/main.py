from fastapi import FastAPI, Path
import time

app = FastAPI()


@app.get("/")
async def home():
    print("Processing Request 1")
    time.sleep(3)
    return {"name": "usman"}


@app.get("/users/{user_id}/messages/{message_id}")
async def users_info(user_id: int, message_id: float = Path(..., ge=1, le=1000)):
    print(type(user_id))
    return {
        "id": user_id,
        "message_id": message_id
    }
    
    
@app.get("/users/{username}")
async def get_user(username: str = Path(..., max_length=5, min_length=3, title="Username", description="Tells about the name of our user.")):
    return {
        "username": username
    }