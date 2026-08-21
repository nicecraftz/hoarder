from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hoarder.course.domain.course import UniversityCourse


class ResourceType(str, Enum):
    FILE = "file"
    LINK = "link"

class Resource(SQLModel, table = True):
    __tablename__ = "resources"
    id: int | None = Field(primary_key=True, index=True, default=None)
    name: str = Field(nullable=False, index=True)
    author: str = Field(nullable=False)

    type: ResourceType
    path: str | None = Field(default=None)
    url: str | None = Field(default=None)

    course_id: int = Field(foreign_key="university_courses.id")

    course: "UniversityCourse" = Relationship(back_populates="resources")


class ResourcePublic(SQLModel, table = False):
    id: int
    name: str
    author: str

    type: ResourceType
    path: str | None = None
    url: str | None = None
    
    course_id: int