from fastapi import FastAPI

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
async def user_page(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# 5. Маршрут к страницам пользователей с данными в адресной строке - "/user"
@app.get("/user")
async def user_query(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
