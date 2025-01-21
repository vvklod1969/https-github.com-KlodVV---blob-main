from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def welcome_page():
    return "Главная страница"


@app.get("/user/admin", response_class=PlainTextResponse)
async def admin_page():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}", response_class=PlainTextResponse)
async def user_page(user_id: str):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user", response_class=PlainTextResponse)
async def user_query(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/users/{user_id}", response_class=PlainTextResponse)
async def users_page(user_id: str):
    return f"Информация о пользователе № {user_id}"