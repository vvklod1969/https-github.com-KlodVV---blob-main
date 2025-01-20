from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples=["UrbanUser"])],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples=[24])],
):
    user_id = str(max(int(k) for k in users.keys()) + 1) if users else "1"
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(title="Enter User ID", examples=["1"])],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples=["UrbanUser"])],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples=[24])],
):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        return {"message": "User not found"}


@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[str, Path(title="Enter User ID", examples=["1"])],
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        return {"message": "User not found"}