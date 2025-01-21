from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users: List = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User, status_code=201)
async def create_user(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples=["UrbanUser"])],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples=[24])],
):
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", examples=[1])],
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples=["UrbanUser"])],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples=[24])],
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: Annotated[int, Path(title="Enter User ID", examples=[1])],
):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
