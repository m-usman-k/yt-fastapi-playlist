from fastapi import FastAPI, Path, Query



app = FastAPI()



@app.get("/users")
async def fetch_users(age: int, account_age: float = 1000):
    return {
        "age": age,
        "account_age": account_age
    }
    
    
@app.get("/users/{user_id}/posts")
async def fetch_posts(user_id: int, category: str, creation_date: float = Query(..., )):
    return {
        "user_id": user_id,
        "category": category,
        "creation_date": creation_date
    }