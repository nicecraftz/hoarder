from enum import Enum
from sqlmodel import SQLModel, Column, Field, Text, Relationship
from hoarder.resource.domain.resource import Resource

class Semester(str, Enum):
    FIRST = "first"
    SECOND = "second"

class CourseBase(SQLModel, table = False):
    name: str = Field(nullable=False, unique=True, index=True)
    description: str = Field(sa_column=Column(Text, nullable=False, default=""))
    semester: Semester

class UniversityCourse(CourseBase, table = True):
    __tablename__ = "university_courses"
    id: int | None = Field(primary_key=True, default=None)
    resources: list['Resource'] = Relationship(back_populates="course")

class CoursePublic(CourseBase):
    id: int
    name: str
    description: str
    semester: Semester

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass