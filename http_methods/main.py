from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class UserModel(BaseModel):
    username: str
    age: int


@app.get("/", tags=["users", "data"],
         summary="Fetches all users",
         description="This endpoint fetches all users from our database.",
         deprecated=True)
async def all_users():
    return [{"username": "simpleprog"}]


@app.get("/users/{user_id}",
         responses={
             200: {"description": "User successfully fetched."},
             404: {
                 "description": "User not found.",
                 "content": {
                     "application/json": {
                         "example": ["simpleprog", "vornacs"]}}},
             422: {"description": "Kuch bhi."}
         })
async def fetch_user(user_id: int):
    return {"user": "usman"}


@app.post("/", tags=["users"])
async def add_users(all_users: list[UserModel]):
    return all_users


@app.put("/{user_id}", tags=["users"])
async def put_user(user_id: int):
    return {"username": "simpleprog"}

@app.patch("/{user_id}", tags=["users"])
async def patch_user(user_id: int):
    return {"username": "simpleprog"}


@app.delete("/{user_id}", tags=["users"])
async def patch_user(user_id: int):
    return {"username": "simpleprog"}