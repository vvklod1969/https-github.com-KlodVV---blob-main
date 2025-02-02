from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Путь к базе данных SQLite
DATABASE_URL = 'sqlite:///taskmanager.db'

# Создание движка базы данных
engine = create_engine(DATABASE_URL)

# Создание локальной сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
