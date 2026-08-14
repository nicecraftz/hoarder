from .core import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

app = FastAPI()
app.router.prefix = "api/v1"
origins = [config.CORS_ALLOWED]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


def main():
    if config.ADMIN_PASSWORD == config.DEFAULT_ADMIN_PASSWORD:
        logging.warning("You are currently using the default ADMIN password, please consider switching.")
    uvicorn.run("hoarder.main:app", host="127.0.0.1", port=8000, reload=True)