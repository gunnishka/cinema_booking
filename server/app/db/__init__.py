import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .base import Base

# Загружаем переменные окружения из файла .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. Add it to server/.env, e.g. "
        "DATABASE_URL=postgresql://postgres:password@localhost:5432/cinema_db"
    )

# Синхронный движок для PostgreSQL
engine = create_engine(DATABASE_URL, echo=False, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session, None, None]:
    """Возвращает сессию базы данных для зависимостей FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

__all__ = ["Base", "engine", "SessionLocal", "get_db"]


