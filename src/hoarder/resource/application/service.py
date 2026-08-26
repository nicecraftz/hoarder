from ..domain.resource import Resource, ResourceType
from hoarder.core.exception import ProblemException
from sqlmodel import Session, select

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