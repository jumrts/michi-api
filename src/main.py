"""The main entry point for the API."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API working!"}