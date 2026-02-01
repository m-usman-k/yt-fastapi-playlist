from fastapi import FastAPI, Request, status, HTTPException


from pydantic import BaseModel


app = FastAPI()


class Message(BaseModel):
    message_id: int
    message_body: str


@app.post("/", response_model=list[Message], status_code=status.HTTP_201_CREATED)
async def home(user_id: int):
    try:
        all_messages = [
            {"message_id": 1, "message_body": "body 1"},
            {"message_id": 2, "message_body": "body 2"},
            {"message_id": 3, "message_body": "body 3"},
            {"message_id": 4, "message_body": "body 4"},
        ]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    return all_messages