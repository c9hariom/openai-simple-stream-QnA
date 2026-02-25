from core.config import Settings
from fastapi import FastAPI
import uvicorn
from api import chat

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Live and working"}


app.include_router(chat.router, prefix="/chat")
