from fastapi import FastAPI
from app.models import *

app=FastAPI()

@app.get("/")
def root():
    return {"message":"MindFirst running backend"}