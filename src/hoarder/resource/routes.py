from fastapi import APIRouter

resource = APIRouter(prefix="resource")

@resource.get("/")
async def get_added_resources():
    return {"hello": "world"}

@resource.get("/static/{id}")
async def static_serve(id: int):
    return {"hello": "world-static"}

