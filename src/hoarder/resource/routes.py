from fastapi import APIRouter
from fastapi.responses import FileResponse, Response
from .application import fs_service as fs

resource_router = APIRouter(prefix="/resource")

@resource_router.get("/")
async def get_added_resources():
    return {"hello": "world"}

@resource_router.get("/static/{id}")
async def static_serve(id: int):
    return {"hello": "world-static"}


@resource_router.get("/static/file/{resource}")
async def static_serve_file(resource: str):
    path_result = fs.get_file(resource)
    if path_result == False:
        return Response(content=None, status_code=404)
    return FileResponse(path=path_result, status_code=200)
    
