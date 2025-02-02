from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users: List = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(
    request: Request, user_id: Annotated[int, Path(title="Enter User ID", examples=[1])]
):
    print(f"Searching for user with ID: {user_id}")  # Добавили отладочную печать
    for user in users:
        if user.id == user_id:
            print(f"User found: {user}")  # Добавили отладочную печать
            return templates.TemplateResponse("users.html", {"request": request, "users":[user]})
    print(f"User with ID: {user_id} not found")  # Добавили отладочную печать
    raise HTTPException(status_code=404, detail="User was not found")


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