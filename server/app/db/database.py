import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text
from app.core.config import Settings
from sqlalchemy.orm import declarative_base

DATABASE_URL = Settings.database_url

# Ассинхронный движок SQLAlchemy 
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()

async def test_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT VERSION()"))
        version = result.scalar()
        print(f"Успешное подключение к базе данных! Версия: {version}")

asyncio.run(test_connection())