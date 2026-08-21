from sqlmodel import SQLModel, create_engine, Session
from hoarder.core import config

import hoarder.course.domain.course
import hoarder.resource.domain.resource

engine = create_engine(
    config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session