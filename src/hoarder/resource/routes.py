from fastapi import APIRouter, Depends
from hoarder.core.db import get_session
from sqlmodel import Session

import hoarder.resource.application.service as service
from hoarder.resource.domain.resource import ResourcePublic

resources = APIRouter(prefix="/resources", tags=["resources"])

@resources.get("/", response_model=list[ResourcePublic])
def get_all_resources(session: Session = Depends(get_session)):
    return service.get_all_resources(session)


@resources.get("/{id}", response_model=ResourcePublic)
def get_resource_by_id(id: int, session: Session = Depends(get_session)):
    return service.get_resource_with_id(session, id)

@resources.post("/", response_model=ResourcePublic)
def create_resource():
    return service.create_resource()