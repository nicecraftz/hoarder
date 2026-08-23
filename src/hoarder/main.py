from .core import config
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from contextlib import asynccontextmanager

from hoarder.core.exception import ProblemException, problem_response, status_phrase
from hoarder.core.db import create_db_and_tables
from hoarder.course.routes import course

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.router.prefix = "/api/v1"
origins = [config.CORS_ALLOWED]

@app.exception_handler(ProblemException)
async def problem_exception_handler(request: Request, exc: ProblemException):
    return problem_response(
        status=exc.status,
        title=exc.title,
        detail=exc.detail,
        type_uri=exc.type_uri,
        instance=request.url.path,
        **exc.extensions,
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    detail = exc.detail if isinstance(exc.detail, str) else str(exc.detail)
    return problem_response(
        status=exc.status_code,
        title=status_phrase(exc.status_code),
        detail=detail,
        instance=request.url.path,
        headers=exc.headers,
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return problem_response(
        status=422,
        title="Unprocessable Entity",
        detail="Request validation failed.",
        instance=request.url.path,
        errors=jsonable_encoder(exc.errors()),
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE"],
    allow_headers=["*"],
)

app.include_router(course)

def main():
    if config.ADMIN_PASSWORD == config.DEFAULT_ADMIN_PASSWORD:
        logging.warning("You are currently using the default ADMIN password, please consider switching.")
    uvicorn.run("hoarder.main:app", host="127.0.0.1", port=8000, reload=True)