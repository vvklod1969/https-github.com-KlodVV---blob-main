from fastapi import FastAPI
from routers.task import router as task_router
from routers.user import router as user_router
from sqlalchemy.schema import CreateTable
from app.models import Task, User
from app.backend.db import Base, engine

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

# Вывод SQL-запроса для создания таблиц
def print_sql_statements():
    print("SQL for creating tables:")
    print(CreateTable(User.__table__).compile(engine))
    print(CreateTable(Task.__table__).compile(engine))


if __name__ == "__main__":
    print_sql_statements()
    