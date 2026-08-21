from enum import Enum
from sqlmodel import SQLModel, Column, Field, Text, Relationship
from hoarder.resource.domain.resource import Resource

class Semester(str, Enum):
    FIRST = "first"
    SECOND = "second"

class UniversityCourse(SQLModel, table = True):
    __tablename__ = "university_courses"
    id: int | None = Field(primary_key=True, default=None)
    name: str = Field(nullable=False)
    description: str = Field(sa_column=Column(Text, nullable=False, default=""))
    semester: Semester
    resources: list['Resource'] = Relationship(back_populates="course")

class CoursePublic(SQLModel, table = False):
    id: int
    name: str
    description: str
    semester: Semester