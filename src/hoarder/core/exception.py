class ProblemException(Exception):
    def __init__(self, status: int, title: str, detail: str,
                 type_uri: str = "about:blank", **kwargs):
        super().__init__(detail)
        self.status = status
        self.title = title
        self.detail = detail
        self.type_uri = type_uri
        self.extensions = kwargs

    def to_problem(self, instance: str | None = None) -> dict:
        problem = {
            "type": self.type_uri,
            "title": self.title,
            "status": self.status,
            "detail": self.detail,
            **self.extensions,
        }
        if instance is not None:
            problem["instance"] = instance
        return problem

from http import HTTPStatus
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def status_phrase(status: int) -> str:
    try:
        return HTTPStatus(status).phrase
    except ValueError:
        return "Error"


def problem_response(
    status: int,
    title: str,
    detail: str,
    type_uri: str = "about:blank",
    instance: str | None = None,
    headers: dict | None = None,
    **extensions,
) -> JSONResponse:
    problem = {
        "type": type_uri,
        "title": title,
        "status": status,
        "detail": detail,
        **extensions,
    }
    if instance is not None:
        problem["instance"] = instance
    return JSONResponse(
        jsonable_encoder(problem),
        status_code=status,
        media_type="application/problem+json",
        headers=headers,
    )
