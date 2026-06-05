from fastapi import FastAPI
from app.routers import chat

app = FastAPI(
    title="Inference Service",
    version="1.0.0"
)
app.include_router(chat.router)