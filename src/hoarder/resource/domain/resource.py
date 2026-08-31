from sqlmodel import SQLModel, Field, Relationship
from pydantic import HttpUrl
from enum import Enum


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hoarder.course.domain.course import UniversityCourse


class ResourceType(str, Enum):
    FILE = "file"
    LINK = "link"

class BaseResource(SQLModel):
    name: str = Field(nullable=False)
    author: str = Field(nullable=False)
    type: ResourceType
    path: str | None = Field(default=None)
    url: str | None = Field(default=None)
    course_id: int = Field(foreign_key="university_courses.id", gt=0)

class ResourceLinkCreate(SQLModel):
    name: str = Field(nullable=False)
    author: str = Field(nullable=False)
    url: HttpUrl
    course_id: int = Field(gt=0)

class ResourceFileCreate(SQLModel):
    name: str = Field(nullable=False)
    author: str = Field(nullable=False)
    course_id: int = Field(gt=0)


class Resource(BaseResource, table = True):
    __tablename__ = "resources"
    id: int | None = Field(primary_key=True, index=True, default=None)
    course: "UniversityCourse" = Relationship(back_populates="resources")


class ResourcePublic(SQLModel, table = False):
    id: int
    name: str
    author: str

    type: ResourceType
    path: str | None = None
    url: str | None = None
    
    course_id: int