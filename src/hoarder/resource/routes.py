from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlmodel import Session

from hoarder.core.db import get_session
import hoarder.resource.application.service as service
from hoarder.resource.domain.resource import ResourcePublic

resources = APIRouter(prefix="/resources", tags=["resources"])

@resources.get("/", response_model=list[ResourcePublic])
def get_all_resources(session: Session = Depends(get_session)):
    return service.get_all_resources(session)

@resources.get("/{id}", response_model=ResourcePublic)
def get_resource_by_id(id: int, session: Session = Depends(get_session)):
    return service.get_resource_with_id(session, id)

@resources.get("/{id}/static", response_model=FileResponse)
def serve_static_resource_by_id(id: int, session: Session = Depends(get_session)):
    path = service.get_resource_path_by_id(session, id)
    return FileResponse(path=path, status_code=200)

@resources.post("/", response_model=ResourcePublic)
def create_link_resource(session: Session = Depends(get_session)):
    return service.create_link_resource()

@resources.post("/upload", response_model=ResourcePublic)
def create_file_resource(session: Session = Depends(get_session)):
    return service.create_file_resource()
    