from ..domain.resource import Resource, ResourceType,ResourceFileCreate, ResourceLinkCreate
from hoarder.core.exception import ProblemException
from sqlmodel import Session, select
import hoarder.resource.application.storage_service as storage

def get_all_resources(session: Session) -> list[Resource]:
    return session.exec(select(Resource)).all()

def get_resource_with_id(session: Session, id: int) -> Resource:
    return session.exec(select(Resource).where(Resource.id == id)).first()

def get_resources_by_name(session: Session, name: str, limit = 10) -> list[Resource]:
    return session.exec(select(Resource).where(Resource.name == name).limit(limit)).all()

def get_resource_path_by_id(session: Session, id: int):
    resource = get_resource_with_id(session, id)
    if resource.type == ResourceType.LINK:
        raise ProblemException(status=400, title="Invalid Resource Type", detail="You tried fetching a LINK type resource as a file one.")
    if not resource.path:
        raise ProblemException(status=400, title="Invalid Resource Path", detail="You tried fetching a resource which has no file specfied.")
    return resource.path


def create_link_resource(session: Session, payload: ResourceLinkCreate):
    resource = Resource(name=payload.name, url=payload.url, author=payload.author, course_id=payload.course_id, type=ResourceType.LINK)
    session.add(resource)
    session.commit()
    session.refresh(resource)
    return resource

def create_file_resource(session: Session, payload: ResourceFileCreate, upload: UploadFile) -> Resource:
    key = storage.create_file(upload.file, upload.filename or "")
    try:
        resource = Resource(
            name=payload.name, author=payload.author, course_id=payload.course_id,
            type=ResourceType.FILE, path=key,
        )
        session.add(resource)
        session.commit()
        session.refresh(resource)
        return resource
    except BaseException:
        session.rollback()
        storage.delete_file(key)
        raise
