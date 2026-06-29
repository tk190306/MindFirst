from fastapi import FastAPI
from app.models import *
from app.routers.auth import router as auth_router

app=FastAPI()
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message":"MindFirst running backend"}
