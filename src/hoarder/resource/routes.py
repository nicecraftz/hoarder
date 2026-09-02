from fastapi import APIRouter, Depends, File, UploadFile, Form
from typing import Annotated
from fastapi.responses import FileResponse
from sqlmodel import Session

from hoarder.core.db import get_session
import hoarder.resource.application.service as service
from hoarder.resource.domain.resource import ResourcePublic, ResourceLinkCreate, ResourceFileCreate

resources = APIRouter(prefix="/resources", tags=["resources"])

@resources.get("/", response_model=list[ResourcePublic])
async def get_all_resources(session: Session = Depends(get_session)):
    return service.get_all_resources(session)

@resources.get("/{id}", response_model=ResourcePublic)
async def get_resource_by_id(id: int, session: Session = Depends(get_session)):
    return service.get_resource_with_id(session, id)

@resources.get("/{id}/static", response_model=FileResponse)
async def serve_static_resource_by_id(id: int, session: Session = Depends(get_session)):
    path = service.get_resource_path_by_id(session, id)
    return FileResponse(path=path, status_code=200)

@resources.post("/", response_model=ResourcePublic)
async def create_link_resource(link_payload: ResourceLinkCreate, session: Session = Depends(get_session)):
    return service.create_link_resource(session, link_payload)

@resources.post("/upload", response_model=ResourcePublic)
async def create_file_resource(payload: Annotated[ResourceFileCreate, Form()], file: UploadFile = File(), session: Session = Depends(get_session)):
    return service.create_file_resource(session, payload, file)
