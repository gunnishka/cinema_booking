from fastapi import FastAPI 
from .api.v1 import router as auth_router

app = FastAPI(title="Cinema Booking API")
app.include_router(auth_router)  

@app.get("/")
def root():
    return {"message": "Backend работает"}
