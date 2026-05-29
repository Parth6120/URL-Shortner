from fastapi import FastAPI, HTTPException
from api.v1 import input_url, read_url

app = FastAPI()

app.include_router(input_url.router)
app.include_router(read_url.router)

@app.get("/")
def root():
    return {"status": "healthy", "message": "Welcome to the URL Shortener API"}
