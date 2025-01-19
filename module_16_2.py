from fastapi import FastAPI, Path
from typing import Annotated

# 1. Создаем экземпляр приложения FastAPI
app = FastAPI()

# 2. Маршрут к главной странице - "/"
@app.get("/")
async def welcome_page():
    return {"message": "Главная страница"}

# 3. Маршрут к странице администратора - "/user/admin"
@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

# 4. Маршрут к страницам пользователей с параметром в пути - "/user/{user_id}"
@app.get("/user/{user_id}")
async def user_page(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples=[1])]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# 5. Маршрут к страницам пользователей с данными в адресной строке - "/user/{username}/{age}"
@app.get("/user/{username}/{age}")
async def user_query(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples=["UrbanUser"])],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples=[24])]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}