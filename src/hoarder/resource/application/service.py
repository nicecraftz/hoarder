from ..domain.resource import Resource
from sqlmodel import Session, select

def get_all_resources(session: Session) -> list[Resource]:
    return session.exec(select(Resource)).all()

def get_resource_with_id(session: Session, id: int) -> Resource:
    return session.exec(select(Resource).where(Resource.id == id)).first()

def get_resources_by_name(session: Session, name: str, limit = 10) -> list[Resource]:
    return session.exec(select(Resource).where(Resource.name == name).limit(limit)).all()