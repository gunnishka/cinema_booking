from fastapi import FastAPI

from app.db import Base, engine
from app import models  

app = FastAPI(title="Cinema Booking API")

# Создаём таблицы при старте 
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Backend работает"}
